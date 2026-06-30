# Preguntas individuales — Nicolas Bareiro

## Mi parte: clase `EventoDeportivo` (herencia + super() + override)
**Archivos:** `modelo.py` (clase `EventoDeportivo`)

> Banco de preguntas técnicas que el profe puede hacer sobre MI parte, con la
> respuesta y el "dónde mostrarlo". Saber señalar la línea en pantalla.

---

### Sobre herencia

**¿Qué representa `EventoDeportivo` y de qué hereda?**
Es la colección especializada: una agenda enfocada en un deporte concreto (ej. una liga de
futsal). Hereda de `AgendaEventos` —`class EventoDeportivo(AgendaEventos)`—, así que tiene
gratis todos sus métodos (agregar, buscar, filtrar) y solo agrega lo propio del deporte.

**¿Por qué herencia y no composición?**
Porque es una relación "es-un": un `EventoDeportivo` ES una `AgendaEventos` especializada.
Reutiliza toda su interfaz y solo se especializa. Composición sería para "tiene-un".

### Sobre `super()`

**Mostrá dónde usás `super()` y explicá qué hace.**
En dos lugares. En `__init__`, `super().__init__(nombre)` llama al constructor del padre,
que inicializa `nombre` e `items`; si no lo llamara, mi agenda no tendría lista de eventos.
En `estadisticas()`, `super().estadisticas()` ejecuta la versión del padre y me devuelve su
diccionario, que después amplío. Sirve para reutilizar el código del padre sin duplicarlo.

### Sobre override y polimorfismo

**¿Qué método sobreescribís y cómo?**
`estadisticas()`. Defino un método con el mismo nombre que el del padre (eso es el
override), pero en vez de copiar su lógica la reutilizo con `super().estadisticas()` y le
agrego las claves propias: `deporte`, `reglamento` y el conteo de eventos de categoría
deportivo.

**¿Qué pasa si llamás `estadisticas()` sobre un `EventoDeportivo`?**
Python usa automáticamente mi versión (la de la subclase), no la del padre. Eso es
polimorfismo: el mismo nombre de método, comportamiento extendido. La parte común la sigue
calculando el padre gracias a `super()`.

**¿Qué tiene `EventoDeportivo` que no tiene `AgendaEventos`? ¿Por qué ahí?**
El atributo `deporte`, el método `reglamento()` y el `estadisticas()` ampliado. Va en la
subclase porque son conceptos de la versión especializada; si estuvieran en la base, la
base conocería algo que no le corresponde y perdería generalidad.

### Sobre el método propio del dominio

**¿Qué hace `reglamento()` y cómo lo implementaste?**
Devuelve las reglas del deporte de la agenda. Uso un diccionario de clase `REGLAMENTOS` que
mapea cada deporte a su reglamento, con `dict.get()` y un valor por defecto. Si el deporte
no está cargado, devuelve un mensaje genérico en vez de fallar.

**¿Por qué un dict de reglamentos y no una subclase por deporte?**
Más extensible y menos verboso: agregar un deporte es una línea en el diccionario, no una
clase nueva. Una jerarquía de subclases por deporte sería sobreingeniería.

### Pregunta de diseño abierta

**Si tuvieras que agregar una tercera subclase, ¿cómo la diseñarías?**
Otra clase que herede de `AgendaEventos` —por ejemplo `EventoCultural` con un atributo
`genero`—, sobreescribiendo `estadisticas()` con `super()` y agregando su método propio. La
base no se toca: solo se extiende. Eso muestra que el diseño es abierto a extensión.

### Comparación con TPI 2 (reflexión)

**¿Qué cambió respecto al TPI 2?**
En el TPI 2 la `BibliotecaEspecializada` solo guardaba un atributo extra, sin comportamiento
propio. Acá la subclase agrega un método real (`reglamento`) y un override que reutiliza al
padre con `super()` —herencia con comportamiento de verdad, no solo un atributo de adorno—.

### Por si pregunta por la relación del UML

**En el diagrama, ¿qué relación hay entre Agenda y Evento?**
Composición (rombo relleno): la agenda contiene de 0 a muchos eventos, y cada evento
pertenece a una sola agenda. La herencia (triángulo hueco) es entre `EventoDeportivo` y
`AgendaEventos`.
