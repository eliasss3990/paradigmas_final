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
mostrar. Así la misma lógica sirve para otra interfaz (gráfica o web) sin cambios.

**¿Qué es `@property`?**
Getter/setter pythónico: expone un método como atributo. Lo usamos para validar
`cupo_maximo` y para hacer `entradas_vendidas` de solo lectura.

**¿Diferencia entre `__str__` y `__repr__`?**
`__str__` = texto para el usuario; `__repr__` = texto técnico para depurar. `print`
usa `__str__`; al imprimir una lista se usa el `__repr__` de cada elemento.

**¿Qué garantiza `isinstance` en `agregar`?**
Que la colección solo contenga Eventos; si llega otra cosa, lanza `TypeError`. El
parámetro está anotado como `object` a propósito: el contrato es aceptar cualquier
cosa y validar en runtime. Si lo anotáramos como `Evento`, el `isinstance` sería
redundante para el verificador estático, pero la validación en ejecución igual hace
falta porque los type hints no se imponen en runtime.

**¿Por qué list comprehensions y no bucles con append?**
Más conciso y legible: `[e for e in items if cond]` reemplaza 4 líneas de bucle.

**¿La relación Agenda–Evento es composición o agregación?**
La modelamos como composición: cada `Evento` pertenece a una sola agenda y vive dentro
de su colección (no se comparte entre agendas). Que el objeto se construya en el menú y
se pase a `agregar()` es solo la forma de implementarlo en Python; la pertenencia sigue
siendo exclusiva. (Es el mismo criterio que el ejemplo Biblioteca–Libro del enunciado.)

**¿Por qué al ordenar por nombre "Zumba" aparece antes que "aerobic"?**
`sorted` con `key=lambda e: getattr(e, criterio)` ordena por orden de code point, donde
las mayúsculas van antes que las minúsculas. Es el orden lexicográfico por defecto de
Python; si quisiéramos orden alfabético real usaríamos `key=...lower()`.

**¿Cómo validan la fecha?**
Con `date.fromisoformat()` en el setter de `fecha`: valida que sea AAAA-MM-DD real
(rechaza mes 13, texto, etc.). Es property igual que `cupo_maximo`.

**¿Qué son los type hints? ¿Obligan algo?**
Anotan tipos de parámetros y retorno. Son opcionales y NO se imponen en runtime (a
diferencia de Java); sirven de documentación y para que Pylance detecte errores.

**¿Qué evolucionó respecto al TPI 1 y TPI 2?**
TPI 1: estado global + diccionarios (`libro["titulo"]`). TPI 2: ya objetos `Libro` con
una `Biblioteca`. Proyecto Final: encapsulación con `@property`, herencia con
comportamiento real (no solo un atributo), desacople de la interfaz y type hints.

---

## Preguntas de arquitectura ("¿qué pasaría si…?")

El profe, al no ver código, suele preguntar por diseño y modularidad: dónde vive cada
responsabilidad y qué pasaría si estuviera en otro lado. La clave de casi todas las
respuestas es el **desacople** (el modelo no sabe de la interfaz) y la **encapsulación**.

**¿Qué pasaría si la validación del cupo estuviera en el menú en vez de en el `Evento`?**
Se rompería la encapsulación: la regla quedaría atada a la consola. Si mañana
agregáramos otra interfaz (gráfica/web), habría que reescribir la validación allí, y se
podría crear un evento inválido por otro camino. Al estar en el setter del `Evento`, la
regla se cumple **siempre**, sin importar quién cree el objeto.

**¿Qué pasaría si `estadisticas()` imprimiera en vez de devolver un dict?**
Quedaría acoplada a la consola. Hoy devuelve datos y cada interfaz decide cómo
mostrarlos; si imprimiera, no podríamos reutilizar ese cálculo en una GUI o web sin
modificar el modelo. Por eso el modelo no usa `print`.

**¿Qué pasaría si el módulo funcional estuviera dentro de las clases?**
Mezclaría dos paradigmas en el mismo lugar. Lo separamos a propósito: el módulo OO
gestiona estado y comportamiento; el funcional son transformaciones puras (filter/map/
sorted) sobre los objetos. Separado, se ve y se prueba más fácil.

**¿Qué pasaría si `EventoDeportivo` NO heredara de `AgendaEventos`?**
Tendríamos que copiar toda la gestión (agregar, buscar, filtrar) o duplicar lógica. La
herencia nos deja reutilizar todo eso y solo agregar lo propio del deporte. Sin
herencia, perderíamos el `super()` y el override, que son el corazón de la consigna.

**¿Qué pasaría si quitáramos el `isinstance` de `agregar`?**
La colección podría llenarse de objetos que no son `Evento`; al iterar para
estadísticas o búsqueda, fallaría más adelante con un error confuso. El `isinstance`
falla temprano y con un mensaje claro, en el punto de entrada.

**¿Qué pasaría si `entradas_vendidas` tuviera setter público?**
Se podría falsear la cantidad vendida sin pasar por la regla del cupo (sobrevender por
la ventana de atrás). Por eso es de solo lectura: la única vía es `vender_entrada()`.

**¿Dónde habría que tocar para agregar una nueva funcionalidad al menú?**
Solo en `menu_consola.py`: una función nueva y una entrada en el diccionario `OPCIONES`.
El modelo no se toca. Eso muestra que las responsabilidades están bien separadas.

**¿Y para soportar una interfaz gráfica?**
Se agregaría un nuevo archivo de interfaz que use el mismo `modelo.py` y
`modulo_funcional.py`. El modelo no cambiaría en nada, porque no depende de la consola.
