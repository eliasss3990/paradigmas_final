# Guion de defensa — Enzo Dominguez

## Parte: clase `AgendaEventos` (Coleccion) + módulo funcional

### Qué defiendo (archivos)

- `modelo.py` → clase `AgendaEventos` (líneas ~71 a ~113)
- `modulo_funcional.py` → las tres funciones

### Guion hablado (intro)

> "Yo implementé la colección, `AgendaEventos`, que centraliza la gestión: agregar con
> validación de tipo, búsqueda parcial, filtrado por categoría y estadísticas. Decidí
> que `estadisticas()` devuelva un diccionario en vez de imprimir, para desacoplar la
> lógica de la interfaz. También hice el módulo funcional con filter, map y sorted."

### Puntos fuertes

1. **`agregar` valida con `isinstance`** → la colección nunca se contamina con
   objetos que no son `Evento`.
2. **List comprehensions** para búsqueda/filtrado: `[e for e in items if ...]`,
   más conciso que un bucle con `append`.
3. **`estadisticas()` devuelve `dict`** (no imprime) → desacople; la consola formatea.
4. **Módulo funcional sobre objetos**, no diccionarios: `e.confirmado` en vez de
   `dato["confirmado"]`.

### Preguntas probables y respuestas

**P: ¿Cómo opera `filter()` sobre tus objetos? ¿Qué condición evalúa?**
R: En `items_activos`, `filter(lambda e: e.confirmado, coleccion.items)` recorre los
eventos y se queda con los que tienen `confirmado == True`. Después `map` extrae el
nombre de cada uno. La condición es el atributo booleano `confirmado` del objeto.

**P: ¿Por qué envolvés `filter`/`map` en `list()`?**
R: En Python 3 devuelven iteradores perezosos; sin `list()` no se materializan los
resultados.

**P: ¿Qué es la `key=lambda` de `sorted`?**
R: Es la función que decide por qué valor ordenar. Uso `key=lambda e: getattr(e,
criterio)`, así ordeno por cualquier atributo cuyo nombre venga como string.

**P: ¿Por qué `estadisticas` no imprime?**
R: Para desacoplar el dominio de la interfaz. Devolviendo un dict, la consola lo
muestra a su manera, y mañana una GUI lo usa igual sin tocar el modelo.

**P: ¿Qué ganás con `isinstance` en `agregar`?**
R: Integridad: garantizo que `items` solo contenga Eventos. Si llega otra cosa, lanzo
`TypeError` en el punto de entrada en vez de fallar después en otro lado.
