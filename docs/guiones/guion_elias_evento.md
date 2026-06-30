# Guion individual — Elías González

**En la presentación:** demostración en vivo (slides 6-8) — recorro el sistema en
consola: agenda, carga, validación, búsqueda, confirmación, venta y control de cupo.
Mi guion hablado y los datos fijos de la demo están en `guion_presentacion_grupal.md`.
**En el código (mi parte):** clase `Evento` (EntidadBase) + menú de consola
(`modelo.py`, `menu_consola.py`, `proyecto_G15.py`).

---

## A. Preguntas frecuentes de producto (mi bloque de la presentación)

**¿Qué opciones tiene el menú principal?** Agregar evento, mostrar, buscar, filtrar,
confirmar, vender entradas, ver estadísticas, módulo funcional y salir.

**¿Qué datos se cargan para registrar un evento?** Nombre, fecha, lugar, categoría y
cupo máximo.

**¿Cómo se valida la fecha?** Solo se acepta formato AAAA-MM-DD válido; si es inválida,
el sistema la vuelve a pedir.

**¿Qué pasa si el cupo no es positivo?** Se rechaza y se vuelve a pedir un cupo válido.

**¿Cómo se evita la sobreventa?** Antes de vender, el sistema verifica los lugares
disponibles; si no alcanzan, rechaza la operación.

**¿La búsqueda exige el nombre exacto?** No, es parcial: se encuentra con una parte del
nombre.

**¿Qué significa confirmar un evento?** Marcarlo como confirmado para diferenciarlo de
los pendientes y reflejarlo en las estadísticas.

**¿Qué evidencia demuestra que funciona?** La consola muestra altas, validaciones,
ventas aceptadas, ventas rechazadas y cambios de estado en vivo.

---

## B. Preguntas técnicas sobre mi código (defensa individual)

> No es para recitar: tener la respuesta clara y saber señalar la línea en pantalla.

---

### Sobre encapsulación y `@property`

**¿Qué es `@property` y por qué lo usaste?**
Es el getter/setter pythónico: expone un método como si fuera un atributo. Lo usé para
encapsular atributos con reglas, sin escribir getters/setters explícitos como en Java.
Quien usa la clase escribe `evento.cupo_maximo = 50` y no nota que por detrás corre una
validación.

**¿Qué atributos validás y cómo?**
Tres: `cupo_maximo` (el setter exige > 0), `fecha` (el setter valida formato AAAA-MM-DD
con `date.fromisoformat`), y `entradas_vendidas` (solo getter, sin setter → solo lectura).

**Si te pido `evento.entradas_vendidas = 500`, ¿qué pasa?**
Lanza `AttributeError`, porque no tiene setter. Es de solo lectura a propósito: las ventas
solo cambian con `vender_entrada()`, que valida contra el cupo. Así es imposible falsear
las ventas desde afuera.

**¿Por qué `_cupo_maximo` / `_fecha` con guion bajo?**
Es el campo interno donde se guarda el valor. La property pública necesita un nombre
distinto del campo, porque si fueran iguales el getter se llamaría a sí mismo →
recursión infinita. El guion bajo es la convención de "interno, no tocar de afuera".

**¿Por qué validás en `__init__` asignando a la property?**
Porque escribo `self.cupo_maximo = ...` (a la property) en lugar de `self._cupo_maximo`.
Así la validación corre incluso al construir el objeto: no se puede crear un Evento
inválido.

### Sobre las properties calculadas

**¿`lugares_disponibles` y `esta_agotado` son atributos?**
No se guardan: son properties calculadas. `lugares_disponibles` devuelve
`cupo - vendidas` en el momento; `esta_agotado` devuelve si llegó a cero. En Java serían
métodos `getX()`; acá se ven como atributo.

### Sobre `__str__` / `__repr__`

**¿Diferencia entre los dos?**
`__str__` es el texto amigable para el usuario (lo que muestra el menú). `__repr__` es el
técnico, para depurar. `print()` y `str()` usan `__str__`; al imprimir una lista, Python
usa el `__repr__` de cada elemento.

### Sobre el método de acción

**¿Cuál es el método de acción propio del dominio?**
`vender_entrada(cantidad=1)`. Encapsula la regla de negocio: solo vende si hay cupo, y
devuelve `True`/`False`. Si la cantidad supera lo disponible, no modifica nada y devuelve
`False`.

### Sobre el menú / interfaz

**¿Por qué el menú está separado del modelo?**
Por desacoplamiento: `menu_consola.py` es la única capa con `print`/`input`. El modelo no
sabe de interfaz. Eso permite cambiar de consola a otra interfaz reutilizando el modelo.

**¿Por qué un diccionario de opciones y no if/elif?**
Es table dispatch: cada opción del menú mapea a su función en el dict `OPCIONES`. Más
limpio y extensible que un if/elif largo; lo tipé como
`dict[str, tuple[str, Callable[[EventoDeportivo], None]]]`.

**¿Qué pasa si el usuario escribe mal un dato (letras donde va número, fecha inválida)?**
No se rompe. Los helpers `_leer_entero` y `_leer_fecha` revalidan en bucle: el primero
usa `try/except ValueError` alrededor de `int()`, el segundo valida con
`date.fromisoformat`. Vuelven a pedir el dato hasta que sea válido.

### Sobre type hints (si los ve)

**¿Qué son y obligan algo?**
Anotan el tipo de parámetros y retorno. Son opcionales y NO se imponen en runtime (a
diferencia de Java): si paso un tipo equivocado, Python lo ejecuta igual. Sirven de
documentación y para que herramientas como Pylance detecten errores en el editor.

### Comparación con TPI 1 (reflexión)

**¿Qué cambió respecto al TPI 1?**
En el TPI 1 los datos vivían en diccionarios y una lista global (`libro["titulo"]`), que
podían fallar con `KeyError`. Acá el estado pertenece al objeto `Evento`, encapsulado, y
las reglas viven junto a los datos. Pasamos de imperativo (datos sueltos) a POO (objeto
que se protege).
