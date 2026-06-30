"""Interfaz de consola. Única capa con print/input.

Opera sobre una EventoDeportivo (colección especializada) y delega toda la
lógica en el modelo y el módulo funcional.
"""

from datetime import date
from typing import Callable

from modelo import Evento, EventoDeportivo, PATRON_FECHA
from modulo_funcional import items_activos, resumen_coleccion, items_ordenados


# ---------- helpers de entrada (revalidan hasta recibir un dato correcto) ----------

def _leer_texto(prompt: str) -> str:
    valor = input(prompt).strip()
    while not valor:
        print("No puede quedar vacío.")
        valor = input(prompt).strip()
    return valor


def _leer_entero(prompt: str, minimo: int | None = None) -> int:
    while True:
        try:
            valor = int(input(prompt).strip())
            if minimo is not None and valor < minimo:
                print(f"Debe ser >= {minimo}.")
                continue
            return valor
        except ValueError:
            print("Ingresá un número entero válido.")


def _leer_opcion_categoria(prompt: str) -> str:
    print("Categorías:", ", ".join(Evento.CATEGORIAS_VALIDAS))
    while True:
        cat = input(prompt).strip().lower()
        if cat in Evento.CATEGORIAS_VALIDAS:
            return cat
        print("Categoría inválida.")


def _leer_fecha(prompt: str) -> str:
    while True:
        valor = input(prompt).strip()
        try:
            if not PATRON_FECHA.fullmatch(valor):
                raise ValueError
            date.fromisoformat(valor)
            return valor
        except ValueError:
            print("Fecha inválida. Usá el formato AAAA-MM-DD (ej: 2026-08-15).")


# ---------- acciones del menú ----------

def _accion_agregar(agenda: EventoDeportivo) -> None:
    print("\n--- AGREGAR EVENTO ---")
    nombre = _leer_texto("Nombre: ")
    fecha = _leer_fecha("Fecha (AAAA-MM-DD): ")
    lugar = _leer_texto("Lugar: ")
    categoria = _leer_opcion_categoria("Categoría: ")
    cupo = _leer_entero("Cupo máximo: ", minimo=1)
    evento = Evento(nombre, fecha, lugar, categoria, cupo)
    agenda.agregar(evento)
    print(f"Evento '{nombre}' agregado correctamente.")


def _mostrar_lista(eventos: list[Evento]) -> None:
    if not eventos:
        print("(sin resultados)")
        return
    for i, e in enumerate(eventos, start=1):
        print(f"  {i}. {e}")


def _accion_mostrar(agenda: EventoDeportivo) -> None:
    print("\n--- TODOS LOS EVENTOS ---")
    _mostrar_lista(agenda.items)


def _accion_buscar(agenda: EventoDeportivo) -> None:
    print("\n--- BUSCAR POR NOMBRE ---")
    texto = _leer_texto("Texto a buscar: ")
    _mostrar_lista(agenda.buscar_por_nombre(texto))


def _accion_filtrar(agenda: EventoDeportivo) -> None:
    print("\n--- FILTRAR POR CATEGORÍA ---")
    categoria = _leer_opcion_categoria("Categoría: ")
    _mostrar_lista(agenda.filtrar_por_categoria(categoria))


def _accion_marcar(agenda: EventoDeportivo) -> None:
    print("\n--- MARCAR EVENTO COMO CONFIRMADO ---")
    if not agenda.items:
        print("(no hay eventos cargados)")
        return
    _mostrar_lista(agenda.items)
    idx = _leer_entero("Número de evento a confirmar: ", minimo=1)
    if 1 <= idx <= len(agenda.items):
        agenda.items[idx - 1].confirmar()
        print("Evento confirmado.")
    else:
        print("Número fuera de rango.")


def _accion_vender(agenda: EventoDeportivo) -> None:
    print("\n--- VENDER ENTRADAS ---")
    if not agenda.items:
        print("(no hay eventos cargados)")
        return
    _mostrar_lista(agenda.items)
    idx = _leer_entero("Número de evento: ", minimo=1)
    if not 1 <= idx <= len(agenda.items):
        print("Número fuera de rango.")
        return
    evento = agenda.items[idx - 1]
    cantidad = _leer_entero("Cantidad a vender: ", minimo=1)
    if evento.vender_entrada(cantidad):
        print(f"Vendidas {cantidad}. Disponibles: {evento.lugares_disponibles}")
    else:
        print(f"No hay cupo suficiente. Disponibles: {evento.lugares_disponibles}")


def _accion_estadisticas(agenda: EventoDeportivo) -> None:
    print("\n--- ESTADÍSTICAS ---")
    d = agenda.estadisticas()
    print(f"Colección: {d['nombre']}")
    print(f"Deporte (especialización): {d['deporte']}")
    print(f"Total de eventos: {d['total']}")
    print(f"Confirmados: {d['confirmados']} | Pendientes: {d['pendientes']}")
    print(f"Entradas vendidas: {d['entradas_vendidas']} / {d['cupo_total']} "
          f"({d['ocupacion']:.0%} de ocupación)")
    print(f"Categorías presentes: {', '.join(sorted(d['categorias'])) or '—'}")
    print(f"Eventos de categoría deportivo: {d['eventos_categoria_deportivo']}")
    print(f"Reglamento {d['deporte']}: {d['reglamento']}")


# Etiquetas amigables -> atributo real de Evento (para el ordenamiento del menú).
CRITERIOS_ORDEN = {
    "1": ("Nombre", "nombre"),
    "2": ("Fecha", "fecha"),
    "3": ("Categoría", "categoria"),
    "4": ("Cupo", "cupo_maximo"),
}


def _accion_funcional(agenda: EventoDeportivo) -> None:
    print("\n--- MÓDULO FUNCIONAL ---")
    print("a. Nombres de eventos confirmados (filter + map)")
    print("b. Resumen de la colección (map)")
    print("c. Ordenar por criterio (sorted)")
    opcion = input("Seleccione: ").strip().lower()
    if opcion == "a":
        print("Confirmados:", items_activos(agenda) or "(ninguno)")
    elif opcion == "b":
        resumen = resumen_coleccion(agenda)
        if not resumen:
            print("(sin resultados)")
        for linea in resumen:
            print("->", linea)
    elif opcion == "c":
        for clave, (etiqueta, _) in CRITERIOS_ORDEN.items():
            print(f"  {clave}. {etiqueta}")
        sel = input("Ordenar por: ").strip()
        if sel not in CRITERIOS_ORDEN:
            print("Criterio inválido.")
            return
        atributo = CRITERIOS_ORDEN[sel][1]
        _mostrar_lista(items_ordenados(agenda, atributo))
    else:
        print("Opción inválida.")


# ---------- bucle principal ----------

OPCIONES: dict[str, tuple[str, Callable[[EventoDeportivo], None]]] = {
    "1": ("Agregar evento", _accion_agregar),
    "2": ("Mostrar todos los eventos", _accion_mostrar),
    "3": ("Buscar por nombre", _accion_buscar),
    "4": ("Filtrar por categoría", _accion_filtrar),
    "5": ("Marcar evento como confirmado", _accion_marcar),
    "6": ("Vender entradas", _accion_vender),
    "7": ("Ver estadísticas", _accion_estadisticas),
    "8": ("Módulo funcional", _accion_funcional),
}

SALIR = "9"


def _imprimir_menu() -> None:
    print("\n--- MENÚ PRINCIPAL ---")
    for clave, (etiqueta, _) in OPCIONES.items():
        print(f"{clave}. {etiqueta}")
    print(f"{SALIR}. Salir")


def iniciar() -> None:
    print("=" * 46)
    print("SISTEMA DE GESTIÓN DE EVENTOS — PROYECTO FINAL")
    print("Paradigmas de la Programación · FP-UNA · Grupo 15")
    print("=" * 46)
    nombre = _leer_texto("Nombre de la colección: ")
    deporte = _leer_texto("Especialización (deporte): ")
    agenda = EventoDeportivo(nombre, deporte)
    print(f"\nColección '{nombre}' iniciada. Deporte: {deporte}")

    while True:
        _imprimir_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == SALIR:
            print("¡Hasta luego!")
            break
        accion = OPCIONES.get(opcion)
        if accion:
            accion[1](agenda)
        else:
            print("Opción inválida.")
