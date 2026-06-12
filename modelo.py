"""Capa de dominio: Evento, AgendaEventos y EventoDeportivo.

No depende de la interfaz (sin print/input), para poder reutilizarla desde
consola, Tkinter o web.
"""


class Evento:
    """Evento individual de la agenda (EntidadBase del dominio)."""

    CATEGORIAS_VALIDAS = ("concierto", "conferencia", "deportivo", "taller", "otro")

    def __init__(self, nombre, fecha, lugar, categoria, cupo_maximo,
                 entradas_vendidas=0, confirmado=False):
        self.nombre = nombre
        self.fecha = fecha # "AAAA-MM-DD"
        self.lugar = lugar
        self.categoria = categoria
        self.cupo_maximo = cupo_maximo # vía setter: valida desde la construcción
        self._entradas_vendidas = entradas_vendidas
        self.confirmado = confirmado

    @property
    def cupo_maximo(self):
        return self._cupo_maximo

    @cupo_maximo.setter
    def cupo_maximo(self, valor):
        if valor <= 0:
            raise ValueError("El cupo máximo debe ser un entero mayor a 0.")
        self._cupo_maximo = valor

    @property
    def entradas_vendidas(self):
        # Solo lectura: las ventas solo cambian vía vender_entrada(), nunca por asignación directa.
        return self._entradas_vendidas

    @property
    def lugares_disponibles(self):
        return self._cupo_maximo - self._entradas_vendidas

    @property
    def esta_agotado(self):
        return self.lugares_disponibles <= 0

    def vender_entrada(self, cantidad=1):
        """Vende entradas respetando el cupo. Devuelve True si concretó la venta."""
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor a 0.")
        if cantidad > self.lugares_disponibles:
            return False
        self._entradas_vendidas += cantidad
        return True

    def confirmar(self):
        self.confirmado = True

    def cancelar(self):
        self.confirmado = False

    def __str__(self):
        estado = "confirmado" if self.confirmado else "pendiente"
        return (f"{self.nombre} ({self.categoria}) — {self.fecha} en {self.lugar} "
                f"| {self._entradas_vendidas}/{self._cupo_maximo} entradas | {estado}")

    def __repr__(self):
        return (f"Evento(nombre={self.nombre!r}, fecha={self.fecha!r}, "
                f"categoria={self.categoria!r}, cupo_maximo={self._cupo_maximo})")
