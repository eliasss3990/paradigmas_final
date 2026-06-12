# Banco de preguntas de defensa — Grupo 15

Preguntas típicas del PDF (sección 8) + extras, con respuestas para todo el grupo.
Cada integrante debe poder responder al menos las de su parte; estas son comunes.

---

### 1. ¿Por qué eligieron esa jerarquía de clases? ¿Consideraron otras opciones?
Tres clases con dos niveles: `Evento` (el elemento), `AgendaEventos` (el contenedor)
y `EventoDeportivo` (el contenedor especializado en un deporte). La alternativa era
poner `deporte` como atributo de `AgendaEventos` sin herencia, pero eso mezclaría
responsabilidades: la base conocería un concepto especializado. Con herencia la base
queda genérica y reutilizable.

### 2. Mostrá dónde usan `super()` y qué hace.
`modelo.py`: en `EventoDeportivo.__init__`, `super().__init__(nombre)` llama al
constructor del padre (crea `nombre` e `items`). En `EventoDeportivo.estadisticas()`,
`super().estadisticas()` reutiliza el cálculo del padre y le agregamos datos del
deporte. Sirve para no duplicar código y extender el comportamiento del padre.

### 3. ¿Cómo opera `filter()` sobre los objetos? ¿Qué condición evalúa?
En `items_activos` (modulo_funcional.py), `filter(lambda e: e.confirmado, items)`
recorre los Eventos y se queda con los que tienen `confirmado == True`. Evalúa el
atributo booleano del objeto, no una clave de diccionario.

### 4. ¿Qué tiene `EventoDeportivo` que no tiene `AgendaEventos`? ¿Por qué ahí?
El atributo `deporte`, el método `reglamento()` y un `estadisticas()` ampliado. Va en
la subclase porque son conceptos de la versión especializada; en la base romperían su
generalidad.

### 5. Si tuvieran que agregar una tercera subclase, ¿cómo la diseñarían?
Otra clase que herede de `AgendaEventos` (ej. `EventoCultural` con `genero`),
sobrescribiendo `estadisticas()` con `super()` y agregando su método propio. La base
no se toca: solo se extiende.

---

### Extras frecuentes

**¿Por qué `estadisticas()` devuelve un dict en vez de imprimir?**
Para desacoplar dominio de interfaz. El modelo no usa `print`; la consola decide cómo
mostrar. Así la misma lógica sirve para Tkinter o web sin cambios.

**¿Qué es `@property`?**
Getter/setter pythónico: expone un método como atributo. Lo usamos para validar
`cupo_maximo` y para hacer `entradas_vendidas` de solo lectura.

**¿Diferencia entre `__str__` y `__repr__`?**
`__str__` = texto para el usuario; `__repr__` = texto técnico para depurar. `print`
usa `__str__`; al imprimir una lista se usa el `__repr__` de cada elemento.

**¿Qué garantiza `isinstance` en `agregar`?**
Que la colección solo contenga Eventos; si llega otra cosa, lanza `TypeError`.

**¿Por qué list comprehensions y no bucles con append?**
Más conciso y legible: `[e for e in items if cond]` reemplaza 4 líneas de bucle.

**¿Qué evolucionó respecto al TPI 1 y TPI 2?**
TPI 1: estado global + diccionarios (`libro["titulo"]`). TPI 2: ya objetos `Libro` con
una `Biblioteca`. Proyecto Final: encapsulación con `@property`, herencia con
comportamiento real (no solo un atributo), y desacople de la interfaz.
