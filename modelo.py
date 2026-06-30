"""Capa de dominio: Evento, AgendaEventos y EventoDeportivo.

No depende de la interfaz (sin print/input), para poder reutilizarla desde
consola, Tkinter o web.
"""

from datetime import date


class Evento:
    """Evento individual de la agenda (EntidadBase del dominio)."""

    CATEGORIAS_VALIDAS = ("concierto", "conferencia", "deportivo", "taller", "otro")

    def __init__(self, nombre: str, fecha: str, lugar: str, categoria: str,
                 cupo_maximo: int, entradas_vendidas: int = 0,
                 confirmado: bool = False) -> None:
        self.nombre = nombre
        self.fecha = fecha # vía setter: valida el formato AAAA-MM-DD
        self.lugar = lugar
        self.categoria = categoria
        self.cupo_maximo = cupo_maximo # vía setter: valida desde la construcción
        if not 0 <= entradas_vendidas <= self.cupo_maximo:
            raise ValueError("Las entradas vendidas deben estar entre 0 y el cupo máximo.")
        self._entradas_vendidas = entradas_vendidas
        self.confirmado = confirmado

    @property
    def fecha(self) -> str:
        return self._fecha

    @fecha.setter
    def fecha(self, valor: str) -> None:
        # date.fromisoformat valida que el string sea una fecha AAAA-MM-DD real.
        try:
            date.fromisoformat(valor)
        except (ValueError, TypeError):
            raise ValueError("La fecha debe tener el formato AAAA-MM-DD (ej: 2026-08-15).")
        self._fecha = valor

    @property
    def cupo_maximo(self) -> int:
        return self._cupo_maximo

    @cupo_maximo.setter
    def cupo_maximo(self, valor: int) -> None:
        if valor <= 0:
            raise ValueError("El cupo máximo debe ser un entero mayor a 0.")
        self._cupo_maximo = valor

    @property
    def entradas_vendidas(self) -> int:
        # Solo lectura: las ventas solo cambian vía vender_entrada(), nunca por asignación directa.
        return self._entradas_vendidas

    @property
    def lugares_disponibles(self) -> int:
        return self._cupo_maximo - self._entradas_vendidas

    @property
    def esta_agotado(self) -> bool:
        return self.lugares_disponibles <= 0

    def vender_entrada(self, cantidad: int = 1) -> bool:
        """Vende entradas respetando el cupo. Devuelve True si concretó la venta."""
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor a 0.")
        if cantidad > self.lugares_disponibles:
            return False
        self._entradas_vendidas += cantidad
        return True

    def confirmar(self) -> None:
        self.confirmado = True

    def cancelar(self) -> None:
        self.confirmado = False

    def __str__(self):
        estado = "confirmado" if self.confirmado else "pendiente"
        return (f"{self.nombre} ({self.categoria}) — {self.fecha} en {self.lugar} "
                f"| {self._entradas_vendidas}/{self._cupo_maximo} entradas | {estado}")

    def __repr__(self):
        return (f"Evento(nombre={self.nombre!r}, fecha={self.fecha!r}, "
                f"categoria={self.categoria!r}, cupo_maximo={self._cupo_maximo})")


class AgendaEventos:
    """Colección de eventos. Centraliza alta, búsqueda, filtrado y estadísticas."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.items: list[Evento] = []

    def agregar(self, evento: "Evento") -> None:
        """Agrega un Evento validando el tipo para no contaminar la colección."""
        if not isinstance(evento, Evento):
            raise TypeError("Solo se pueden agregar instancias de Evento.")
        self.items.append(evento)

    def buscar_por_nombre(self, texto: str) -> list["Evento"]:
        """Búsqueda parcial, case-insensitive, por nombre del evento."""
        t = texto.lower()
        return [e for e in self.items if t in e.nombre.lower()]

    def filtrar_por_categoria(self, categoria: str) -> list["Evento"]:
        """Filtra por categoría exacta (case-insensitive)."""
        c = categoria.lower()
        return [e for e in self.items if e.categoria.lower() == c]

    def estadisticas(self) -> dict:
        """Devuelve un dict con métricas. No imprime: la presentación es del menú."""
        total = len(self.items)
        confirmados = sum(1 for e in self.items if e.confirmado)
        entradas_vendidas = sum(e.entradas_vendidas for e in self.items)
        cupo_total = sum(e.cupo_maximo for e in self.items)
        categorias = {e.categoria for e in self.items}
        return {
            "nombre": self.nombre,
            "total": total,
            "confirmados": confirmados,
            "pendientes": total - confirmados,
            "entradas_vendidas": entradas_vendidas,
            "cupo_total": cupo_total,
            "ocupacion": (entradas_vendidas / cupo_total) if cupo_total else 0.0,
            "categorias": categorias,
        }

    def __len__(self) -> int:
        return len(self.items)


class EventoDeportivo(AgendaEventos):
    """Agenda especializada en un deporte. Hereda toda la gestión de AgendaEventos
    y añade el reglamento del deporte y estadísticas propias."""

    # Reglamentos mínimos por deporte (constante de clase, extensible sin tocar la lógica).
    REGLAMENTOS = {
        "futbol": "11 jugadores por equipo, dos tiempos de 45 minutos.",
        "futsal": "5 jugadores por equipo, dos tiempos de 20 minutos a reloj parado.",
        "basquet": "5 jugadores por equipo, cuatro cuartos de 10 minutos.",
        "voley": "6 jugadores por equipo, sets a 25 puntos con diferencia de 2.",
        "tenis": "1 vs 1, sets a 6 games con diferencia de 2.",
    }

    def __init__(self, nombre: str, deporte: str) -> None:
        super().__init__(nombre) # inicializa nombre e items en el padre
        self.deporte = deporte

    def reglamento(self) -> str:
        """Devuelve el reglamento del deporte de la agenda (método propio del dominio)."""
        return self.REGLAMENTOS.get(
            self.deporte.lower(),
            f"No hay reglamento cargado para '{self.deporte}'."
        )

    def estadisticas(self) -> dict:
        """Override: extiende las estadísticas del padre con datos del deporte."""
        datos = super().estadisticas() # reutiliza el cálculo base
        datos["deporte"] = self.deporte
        datos["reglamento"] = self.reglamento()
        # 'deporte' determina el reglamento; este conteo es independiente, por categoría.
        datos["eventos_categoria_deportivo"] = len(self.filtrar_por_categoria("deportivo"))
        return datos
