# Guion individual — Enzo Domínguez

**En la presentación:** apertura (slides 1-5) — presento el grupo, el problema, la
solución y el valor. Mi guion hablado está en `guion_presentacion_grupal.md`.
**En el código (mi parte):** clase `AgendaEventos` (Coleccion) + módulo funcional
(`modelo.py`, `modulo_funcional.py`).

---

## A. Preguntas frecuentes de producto (mi bloque de la presentación)

**¿Cuál es el objetivo principal del sistema?** Centralizar la gestión de eventos en
una consola: carga, consulta, venta de entradas con control de cupo, validaciones y
estadísticas.

**¿Por qué consola y no interfaz gráfica?** El objetivo del proyecto era demostrar la
lógica y el flujo funcional; la consola permite validar el producto de forma directa.
Además la lógica está desacoplada, así que mañana se le podría poner una GUI.

**¿Qué problema real resuelve?** Evita errores típicos de la gestión manual: fechas
inválidas, cupos incorrectos, sobreventa y falta de visibilidad.

**¿Qué significa que sea una demo de producto / UAT?** Que mostramos el comportamiento
del sistema desde el punto de vista del usuario, verificando que cumple lo esperado.

**¿Qué valor aporta?** Control de cupos, trazabilidad de eventos y estadísticas rápidas
para tomar decisiones.

**¿Por qué está especializado por deporte?** Para sumar información propia del deporte
(el reglamento) sin perder la gestión general de eventos.

**¿Qué diferencia este sistema de una simple lista de eventos?** Además de guardar,
aplica reglas, controla ventas y genera indicadores.

---

## B. Preguntas técnicas sobre mi código (defensa individual)

> Saber señalar la línea en pantalla.

---

### Sobre la colección

**¿Qué responsabilidad tiene `AgendaEventos`?**
Es el contenedor: guarda los eventos en `items` y centraliza las operaciones sobre el
conjunto —agregar, buscar, filtrar, estadísticas—. El evento individual se ocupa de sus
datos; la colección, de las operaciones sobre el grupo. Es separación de responsabilidades.

**¿Qué hace `agregar` y por qué validás el tipo?**
Antes de meter el evento a la lista, valido con `isinstance(evento, Evento)`; si no lo es,
lanzo `TypeError`. Protege la integridad: garantiza que `items` solo tenga Eventos.

**¿Por qué el parámetro de `agregar` está tipado como `object` y no `Evento`?**
A propósito: el contrato es "aceptá cualquier cosa y validá en runtime que sea un Evento".
Si lo anotara como `Evento`, el `isinstance` sería redundante para el verificador estático,
pero la validación en ejecución igual hace falta porque los type hints no se imponen en
runtime.

**¿Cómo funcionan `buscar_por_nombre` y `filtrar_por_categoria`?**
Con list comprehensions. `buscar_por_nombre` hace `[e for e in items if texto in
e.nombre.lower()]`: búsqueda parcial, insensible a mayúsculas por el `.lower()`.
`filtrar_por_categoria` filtra por coincidencia exacta de categoría.

**¿Por qué list comprehensions y no un bucle con append?**
Más conciso y legible: una línea reemplaza cuatro de bucle. Es el estilo idiomático de
Python.

### Sobre estadísticas (decisión de diseño clave)

**¿Por qué `estadisticas()` devuelve un dict en vez de imprimir?**
Para desacoplar la lógica de la presentación. La agenda calcula y devuelve un diccionario
con las métricas; quien la use —la consola u otra interfaz— decide cómo mostrarlo. Si
imprimiera acá adentro, no podría reutilizar el cálculo en otra interfaz.

**¿Qué métricas calcula?**
Total de eventos, confirmados, pendientes, entradas vendidas, cupo total, ocupación
(vendidas/cupo) y el conjunto de categorías presentes.

**¿Qué es `__len__`?**
Un método especial que permite hacer `len(agenda)` y que devuelva la cantidad de eventos,
como si fuera una lista nativa.

### Sobre el módulo funcional

**¿Qué son las tres funciones y qué herramienta usa cada una?**
`items_activos` (filter + map): nombres de los confirmados. `resumen_coleccion` (map): una
línea por evento. `items_ordenados` (sorted + key=lambda): lista ordenada por un atributo.

**¿Cómo opera `filter` sobre los objetos? ¿Qué condición evalúa?**
`filter(lambda e: e.confirmado, items)` recorre los eventos y se queda con los que tienen
`confirmado == True`. Evalúa el atributo booleano del objeto, no una clave de diccionario.

**¿Por qué envolvés `filter` y `map` en `list()`?**
Porque en Python 3 devuelven iteradores perezosos; sin `list()` no se materializan los
resultados (no se ven los datos).

**¿Qué hace `key=lambda` en `sorted`?**
Define por qué valor ordenar. Uso `getattr(e, criterio)`, donde `criterio` es un string
('fecha', 'nombre'…), lo que permite ordenar por cualquier atributo sin un if por cada uno.

**Al ordenar por nombre, ¿por qué "Zumba" aparece antes que "aerobic"?**
Por el orden de code point: las mayúsculas van antes que las minúsculas. Es el orden
lexicográfico por defecto de Python; con `.lower()` en la key sería alfabético real.

**¿Por qué el módulo funcional opera sobre objetos y no diccionarios?**
Porque trabajar `e.confirmado` en vez de `dato['confirmado']` evita los `KeyError` y es más
expresivo. Es justo la mejora respecto al TPI 1.

### Comparación con TPI 1/2 (reflexión)

**¿Qué cambió respecto a los TPI anteriores?**
En el TPI 1, filter/map operaban sobre diccionarios (`libro['genero']`). En el final operan
sobre objetos `Evento`. Y `estadisticas` pasó de imprimir a devolver datos, lo que permite
reutilizar el modelo en cualquier interfaz.
