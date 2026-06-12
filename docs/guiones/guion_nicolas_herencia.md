# Guion de defensa — Nicolas Bareiro

## Parte: clase `EventoDeportivo` (herencia + super() + override)

### Qué defiendo (archivos)

- `modelo.py` → clase `EventoDeportivo` (líneas ~116 a ~146)

### Guion hablado (intro)

> "Yo implementé la colección especializada, `EventoDeportivo`, que hereda de
> `AgendaEventos`. Es una agenda enfocada en un deporte: reutiliza toda la gestión
> del padre (agregar, buscar, filtrar) y agrega lo propio: el atributo `deporte`, el
> método `reglamento()` y un override de `estadisticas()` que usa `super()` para
> reutilizar el cálculo base y sumarle datos del deporte."

### Puntos fuertes

1. **Herencia real:** `class EventoDeportivo(AgendaEventos)` → hereda todos los métodos.
2. **`super().__init__(nombre)`** inicializa nombre e items en el padre sin repetir código.
3. **Override con `super()`:** `estadisticas()` llama a `super().estadisticas()` y
   extiende el dict, en vez de copiar la lógica del padre.
4. **`REGLAMENTOS` como dict de clase** + `reglamento()` con `.get()` y default:
   extensible sin tocar la lógica.

### Preguntas probables y respuestas

**P: Mostrá dónde usás `super()` y explicá qué hace.**
R: En `__init__`, `super().__init__(nombre)` llama al constructor del padre
`AgendaEventos`, que crea `self.nombre` y `self.items`. Y en `estadisticas()`,
`super().estadisticas()` ejecuta la versión del padre y me devuelve su dict, al que
le agrego `deporte`, `reglamento` y `eventos_del_deporte`. Así no duplico el cálculo.

**P: ¿Qué tiene `EventoDeportivo` que no tiene `AgendaEventos`? ¿Por qué en la subclase?**
R: El atributo `deporte`, el método `reglamento()` y un `estadisticas()` ampliado.
Va en la subclase porque son conceptos de la versión especializada; si los pusiera en
la base, la base conocería algo que no le corresponde y perdería generalidad.

**P: Si tuvieras que agregar una tercera subclase, ¿cómo la diseñarías?**
R: Heredaría también de `AgendaEventos` (p. ej. `EventoCultural` con atributo `genero`),
sobrescribiendo `estadisticas()` con `super()` y agregando su método propio. La base
no cambia: solo extiendo.

**P: ¿Qué pasa si llamás `estadisticas()` sobre `EventoDeportivo`?**
R: Python usa el método de la subclase (el override). Eso es polimorfismo: el mismo
nombre, comportamiento extendido. La parte común la sigue dando el padre vía `super()`.

**P: ¿Por qué herencia y no composición acá?**
R: Porque `EventoDeportivo` *es una* `AgendaEventos` (relación "es-un"), no *tiene una*.
Reutiliza toda su interfaz y solo especializa. Composición sería para "tiene-un".
