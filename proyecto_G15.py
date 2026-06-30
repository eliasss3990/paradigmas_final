"""Punto de entrada del sistema. Ejecutar con: python3 proyecto_G15.py"""

from menu_consola import iniciar


def main() -> None:
    iniciar()


if __name__ == "__main__":
    main()


# ============================================================================
# REFLEXIÓN COMPARATIVA (TPI 1 · TPI 2 · Proyecto Final)
# ============================================================================
#
# 1) agregar() de la colección vs agregar_libro() del TPI 1
#    En TPI 1, agregar_libro() (tpi1_GONZALEZ_BAREIRO_DOMINGUEZ.py, línea 27)
#    operaba sobre la lista global `libros` y guardaba diccionarios sueltos
#    (libro["titulo"], etc.), sin validar el tipo del elemento. En TPI 2,
#    Biblioteca.agregar() (tpi2_GRUPO_15.py, línea 46) ya pasó a objeto. En el
#    Proyecto Final, AgendaEventos.agregar() (modelo.py, línea ~78) valida con
#    isinstance(evento, Evento) y opera sobre self.items, atributo propio del
#    objeto. Lo que ganamos con la encapsulación: el estado dejó de ser global
#    (no se corrompe desde cualquier parte) y la regla de integridad —"solo
#    entran Eventos"— vive junto al dato, eliminando una clase entera de errores.
#
# 2) Decisión de diseño más difícil
#    Modelar el reglamento de cada deporte sin crear una subclase por deporte.
#    Se resolvió con el dict de clase REGLAMENTOS (modelo.py, línea ~121) y
#    reglamento() con dict.get() y valor por defecto. Es más extensible (se
#    agrega un deporte sin tocar la lógica) y menos verboso que una jerarquía.
#    Frente a TPI 2, donde BibliotecaEspecializada (tpi2_GRUPO_15.py, línea 78)
#    solo guardaba `especialidad`, acá la subclase agrega comportamiento real.
#
# 3) Qué parte del módulo funcional fue más natural sobre objetos que sobre dicts
#    items_activos() (modulo_funcional.py, línea ~9) usa filter(lambda e:
#    e.confirmado, ...). En TPI 1, filtrar_por_genero() (línea 78-82) y
#    marcar_leido() (línea 85-89) hacían filter sobre diccionarios con
#    libro["genero"] / item["titulo"]. En TPI 2, titulos_leidos() (línea 101-106)
#    ya usaba filter+map sobre objetos Libro (l.leido, l.titulo). Trabajar
#    e.confirmado (atributo de objeto) en vez de dato["confirmado"] elimina los
#    posibles KeyError y deja el código más expresivo y seguro.
# ============================================================================
