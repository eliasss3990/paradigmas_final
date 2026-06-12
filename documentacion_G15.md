# Documentación Técnica — Proyecto Final

## Paradigmas de la Programación · FP-UNA · 2026

---

## Carátula

| Campo | Valor |
|-------|-------|
| **Dominio** | Gestión de eventos |
| **Grupo** | G15 |
| **Integrantes** | Elias Gonzalez · Enzo Dominguez · Nicolas Bareiro |
| **Fecha** | Junio 2026 |
| **Docente** | Prof. Lic. Gustavo Galeano |
| **Materia** | Paradigmas de la Programación (Código 4.2) |

---

## 1. Descripción del sistema

### ¿Qué hace el sistema?

El sistema permite administrar una colección de eventos desde la consola. El usuario puede:

- Registrar nuevos eventos con sus datos (nombre, fecha, lugar, categoría, cupo).
- Listar todos los eventos cargados.
- Buscar eventos por nombre (búsqueda parcial).
- Filtrar eventos por categoría.
- Confirmar eventos.
- Vender entradas validando que no se supere el cupo.
- Ver estadísticas de la colección, adaptadas al deporte de especialización.
- Ejecutar el módulo funcional (eventos confirmados, resumen y ordenamiento).

### ¿Qué problema resuelve?

Organizar una agenda de eventos sin herramientas suele derivar en sobreventa de
entradas y pérdida de control sobre qué está confirmado. El sistema centraliza el
registro, valida el cupo al vender entradas y ofrece estadísticas inmediatas
(ocupación, confirmados, categorías) para una agenda especializada en un deporte.

---

## 2. Decisiones de diseño

### ¿Por qué esta jerarquía de clases?

Se eligió una jerarquía de tres clases con dos niveles de abstracción:

1. **Evento** encapsula los datos y el comportamiento de un evento individual.
   Conoce su propio estado (cupo, entradas vendidas, confirmación) y aplica sus
   reglas: no se vende más entradas que el cupo, el cupo debe ser positivo.

2. **AgendaEventos** centraliza la gestión de la colección. Las operaciones de
   búsqueda, filtrado y estadística son responsabilidad del contenedor, no del
   elemento individual.

3. **EventoDeportivo** extiende `AgendaEventos` con el concepto de *deporte*. Se
   eligió herencia porque *es una* `AgendaEventos` más específica: reutiliza todas
   sus operaciones y solo amplía `estadisticas()` y agrega `reglamento()`.

### Separación de capas (desacoplamiento)

La lógica de dominio (`modelo.py`) **no contiene `print` ni `input`**: las
estadísticas se devuelven como `dict` y la presentación corre por cuenta de la
interfaz (`menu_consola.py`). Así la misma lógica puede reutilizarse en una
interfaz gráfica (Tkinter) o web sin modificar las clases.

### Alternativas consideradas

Modelar el deporte como un atributo más de `AgendaEventos`, sin herencia, hubiera
funcionado, pero mezclaría responsabilidades: la clase base conocería un concepto
propio de una versión especializada. Con herencia, la base permanece genérica.

---

## 3. Diagrama UML de clases

Ver `diagrama_G15.png` (generado desde `diagrama_G15.puml`).

- `EventoDeportivo ▷── AgendaEventos`: herencia (triángulo hueco hacia el padre).
- `AgendaEventos 1 ◆── 0..* Evento`: composición; la agenda contiene 0..* eventos.
  Cada `Evento` pertenece a una sola agenda y vive dentro de su colección.

---

## 4. Descripción de clases y funciones públicas

### Clase `Evento` (EntidadBase)

| Elemento | Tipo / Retorno | Descripción |
|----------|----------------|-------------|
| `nombre`, `fecha`, `lugar`, `categoria` | `str` | Datos básicos del evento |
| `cupo_maximo` | `int` (property) | Capacidad; valida que sea > 0 |
| `entradas_vendidas` | `int` (property solo lectura) | Solo cambia vía `vender_entrada` |
| `lugares_disponibles` | `int` (calculada) | `cupo_maximo - entradas_vendidas` |
| `esta_agotado` | `bool` (calculada) | True si no quedan lugares |
| `vender_entrada(cantidad=1)` | `bool` | Vende respetando el cupo |
| `confirmar()` / `cancelar()` | `None` | Cambian el estado `confirmado` |
| `__str__` / `__repr__` | `str` | Representaciones de texto |

### Clase `AgendaEventos` (Coleccion)

| Elemento | Tipo / Retorno | Descripción |
|----------|----------------|-------------|
| `nombre` | `str` | Nombre de la colección |
| `items` | `list[Evento]` | Eventos registrados |
| `agregar(evento)` | `None` | Agrega validando el tipo |
| `buscar_por_nombre(texto)` | `list[Evento]` | Búsqueda parcial case-insensitive |
| `filtrar_por_categoria(categoria)` | `list[Evento]` | Filtra por categoría exacta |
| `estadisticas()` | `dict` | Métricas de la colección |

### Clase `EventoDeportivo` (ColeccionEspecializada, hereda de `AgendaEventos`)

| Elemento | Tipo / Retorno | Descripción |
|----------|----------------|-------------|
| `deporte` | `str` | Deporte de especialización |
| `REGLAMENTOS` | `dict` (clase) | Reglamentos por deporte |
| `reglamento()` | `str` | Reglamento del deporte configurado |
| `estadisticas()` | `dict` | Override: `super()` + datos del deporte |

### Módulo funcional

| Función | Retorno | Herramienta | Descripción |
|---------|---------|-------------|-------------|
| `items_activos(coleccion)` | `list[str]` | filter + map | Nombres de eventos confirmados |
| `resumen_coleccion(coleccion)` | `list[str]` | map + lambda | Una línea de resumen por evento |
| `items_ordenados(coleccion, criterio)` | `list[Evento]` | sorted + lambda | Lista ordenada por el atributo dado |

---

## 5. Instrucciones de ejecución

### Requisitos

- Python 3.8 o superior. No requiere librerías externas.

### Ejecución

```bash
python3 proyecto_G15.py
```

### Estructura de archivos

- `modelo.py` — clases de dominio (Evento, AgendaEventos, EventoDeportivo)
- `modulo_funcional.py` — funciones filter/map/sorted
- `menu_consola.py` — interfaz de consola
- `proyecto_G15.py` — punto de entrada

---

## 6. Reflexión comparativa

La reflexión completa está en comentarios al final de `proyecto_G15.py`. Resumen:

- **`agregar` (POO) vs `agregar_libro` (TPI 1):** en TPI 1 el estado vivía en una
  lista global; ahora `self.items` pertenece al objeto y la validación de tipo está
  encapsulada en el método, eliminando una clase entera de errores.
- **Decisión más difícil:** modelar el reglamento por deporte sin crear una subclase
  por cada deporte. Se resolvió con un `dict` de reglamentos, más extensible.
- **Módulo funcional sobre objetos:** operar `e.confirmado` en vez de
  `dato["confirmado"]` elimina los `KeyError` y hace el código más expresivo.

---

*Fin del documento — Proyecto Final · Paradigmas de la Programación · FP-UNA 2026*
