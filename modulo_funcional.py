"""Módulo funcional: operaciones sobre la colección con filter, map y sorted.

Separado de la capa OO a propósito (paradigma funcional). Opera sobre los
objetos Evento de una AgendaEventos, no sobre diccionarios.
"""

from modelo import AgendaEventos, Evento


def items_activos(coleccion: AgendaEventos) -> list[str]:
    """Nombres de los eventos confirmados (filter para seleccionar, map para transformar)."""
    confirmados = filter(lambda e: e.confirmado, coleccion.items)
    return list(map(lambda e: e.nombre, confirmados))


def resumen_coleccion(coleccion: AgendaEventos) -> list[str]:
    """Una línea de resumen por evento (map + lambda)."""
    return list(map(
        lambda e: f"{e.nombre} | {e.fecha} | {e.entradas_vendidas}/{e.cupo_maximo} entradas",
        coleccion.items
    ))


def items_ordenados(coleccion: AgendaEventos, criterio: str) -> list[Evento]:
    """Eventos ordenados por el atributo indicado (sorted + key=lambda).

    'criterio' es el nombre de un atributo de Evento, p. ej. 'fecha' o 'nombre'.
    """
    return sorted(coleccion.items, key=lambda e: getattr(e, criterio))
