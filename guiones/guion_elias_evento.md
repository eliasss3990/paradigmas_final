# Guion de defensa — Elias Gonzalez

## Parte: clase `Evento` (EntidadBase) + menú de consola

### Qué defiendo (archivos)

- `modelo.py` → clase `Evento` (líneas ~8 a ~68)
- `menu_consola.py` y `proyecto_G15.py` → la interfaz

### Guion hablado (30–40 seg de intro)

> "Yo implementé la EntidadBase del dominio, la clase `Evento`. Representa un evento
> individual con sus datos (nombre, fecha, lugar, categoría, cupo) y su
> comportamiento: vender entradas y confirmarse. Usé `@property` para encapsular el
> cupo con validación y para que `entradas_vendidas` sea de solo lectura, de modo
> que las ventas solo cambien a través de `vender_entrada()`, que respeta el cupo.
> También implementé el menú de consola, que es la única capa que usa print/input."

### Puntos fuertes a mencionar

1. **`@property` = getter/setter pythónico.** `cupo_maximo` valida (>0) en el setter;
   `entradas_vendidas` tiene getter sin setter → solo lectura (encapsulación real).
2. **Propiedades calculadas** (`lugares_disponibles`, `esta_agotado`): no se guardan,
   se computan al pedirlas.
3. **Validación desde la construcción:** en `__init__` asigno `self.cupo_maximo = ...`
   (a la property, no a `_cupo_maximo`), así el setter valida incluso al crear el objeto.
4. **Desacople UI:** el menú usa un `dict` de despacho (OPCIONES) en vez de un
   if/elif largo, y delega toda la lógica al modelo.

### Preguntas probables y respuestas

**P: ¿Qué hace `@property` exactamente?**
R: Convierte un método en algo que se usa como atributo. `cupo_maximo` es el getter
(se lee sin paréntesis) y `cupo_maximo.setter` el setter con validación. Mantengo
encapsulación sin escribir getters/setters explícitos como en Java.

**P: Si te pido cambiar `entradas_vendidas` a 500 desde afuera, ¿qué pasa?**
R: Da `AttributeError`, porque tiene getter pero no setter: es de solo lectura. La
única forma de modificarlo es `vender_entrada()`, que valida contra el cupo.

**P: ¿Por qué `_entradas_vendidas` con guion bajo?**
R: Es la variable interna (convención de "no tocar de afuera"). La property pública se
llama `entradas_vendidas`; necesitan nombres distintos para no caer en recursión.

**P: Diferencia entre `__str__` y `__repr__`.**
R: `__str__` es el texto amigable para el usuario; `__repr__` es el técnico para
depuración (idealmente permite recrear el objeto). `print()` usa `__str__`; al imprimir
una lista, se usa `__repr__` de cada elemento.

**P: ¿Por qué el menú usa un diccionario en vez de if/elif?**
R: Es table dispatch: cada opción mapea a su función. Es más limpio y extensible;
agregar una opción es agregar una entrada al dict, no otro `elif`.
