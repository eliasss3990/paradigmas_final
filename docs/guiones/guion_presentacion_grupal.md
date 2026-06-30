# Guiones de defensa oral — Grupo 15
## Sistema de Gestión de Eventos · Proyecto Final · Paradigmas · FP-UNA 2026
**Integrantes:** Elías González · Enzo Domínguez · Nicolás Bareiro

**Objetivo:** organizar la exposición en tres intervenciones de ~3-4 min, con enfoque
de **demo de producto / UAT**: explicar *qué hace* el sistema, *qué valor* aporta y
*cómo se valida* su funcionamiento en consola. **Sin explicar código línea por línea.**

Acompaña al PPT (`presentacion_G15.pptx`, 13 slides — ver `contenido_ppt.md`).

---

## Orden de exposición

| | Integrante | Rol |
|---|---|---|
| 1 | **Enzo Domínguez** | Presenta el grupo, el problema, la solución y el valor. |
| 2 | **Elías González** | Hace la demo principal: agenda, carga, validación, ventas y cupos. |
| 3 | **Nicolás Bareiro** | Estadísticas, calidad de datos, diseño a alto nivel, UML y cierre. |

---

## 1) Guion de Enzo — Apertura [slides 1-5, ~3-4 min]

> Rol: apertura, presentación del grupo, problema, propuesta de valor y capacidades.

"Buenas tardes, profesor y compañeros. Somos el Grupo 15, integrado por Elías González,
Enzo Domínguez y Nicolás Bareiro, y hoy presentamos nuestro Proyecto Final de Paradigmas
de la Programación: un **Sistema de Gestión de Eventos**, una aplicación de consola en
Python.

La idea no es explicar el código línea por línea, sino **demostrar el producto
funcionando**, como si presentáramos una solución terminada a un cliente: qué problema
resuelve, qué funcionalidades ofrece y qué valor aporta.

El sistema administra una **agenda de eventos especializada por deporte**. Por ejemplo,
una agenda para una liga de futsal y, dentro de ella, eventos con nombre, fecha, lugar,
categoría y cupo de entradas.

El **problema** que resolvemos: gestionar eventos a mano lleva a errores —fechas mal
cargadas, cupos inválidos, sobreventa de entradas, falta de visibilidad del estado—.

Nuestra **solución** centraliza ese flujo en una consola, con un menú que permite crear
la agenda, registrar eventos, listar, buscar por nombre, filtrar por categoría, confirmar
eventos, vender entradas y ver estadísticas.

Lo importante es que el sistema no solo guarda información: **aplica reglas**. Valida que
la fecha tenga el formato correcto, que el cupo sea positivo y que no se vendan más
entradas de las disponibles. Si el dato es incorrecto, el programa no se rompe: lo vuelve
a pedir.

El **valor** se resume en tres ideas: **control** (evita la sobreventa), **trazabilidad**
(cada evento queda registrado con sus datos, estado y ventas) y **visibilidad** (las
estadísticas muestran al instante cuántos eventos hay, confirmados, pendientes, entradas
vendidas y ocupación).

En la slide de capacidades vemos todo lo que permite hacer la aplicación. Para comprobar
que el flujo realmente funciona, **le paso la palabra a Elías** para la demostración."

---

## 2) Guion de Elías — Demostración en vivo [slides 6-8, ~3-4 min]

> Rol: demo en consola — agenda, carga, validación, búsqueda, confirmación, venta y cupo.
> **Pasar a la consola.** Datos fijos para no improvisar (ver abajo).

"Gracias, Enzo. Pasamos a la parte más importante: la **demostración del sistema en
consola**.

Inicio el programa y el sistema pide crear una agenda: le pongo nombre **'Liga Verano'**
y deporte de especialización **'futsal'**. Aparece el menú principal con todas las
opciones.

Primero **cargo un evento**: 'Final del Torneo', con su fecha, lugar, categoría
'deportivo' y cupo 200. Acá muestro una validación: si ingreso una **fecha inválida** o
con formato incorrecto, el sistema **la rechaza y la vuelve a pedir** — control de calidad
desde la entrada. Cargo un segundo evento (una charla, cupo 80) para tener variedad.

**Listo los eventos**: la consola muestra nombre, categoría, fecha, lugar, entradas
vendidas, cupo y estado.

Ahora la **venta de entradas**: vendo 150 de un cupo de 200, el sistema las acepta y
muestra que quedan 50 disponibles. Y lo más importante: si **intento vender más de las
disponibles**, el sistema **rechaza la operación** — no permite sobreventa. Este es uno
de los mayores valores del sistema.

También **confirmo un evento** (se refleja en las estadísticas), **busco por nombre**
(búsqueda parcial, sin escribir el nombre completo) y **filtro por categoría**.

Lo clave es que la consola muestra el comportamiento **en vivo**: no solo decimos que
valida o controla cupos, se ve directamente cómo responde ante datos correctos e
incorrectos. **Le paso la palabra a Nicolás** para las estadísticas y el cierre."

**Datos fijos de la demo** (usar siempre los mismos):
- Agenda: *Liga Verano* · deporte *futsal*.
- Evento 1: *Final del Torneo*, 2026-07-20, Polideportivo, deportivo, **cupo 200**.
- Evento 2: *Charla Táctica*, 2026-09-01, Auditorio, conferencia, **cupo 80**.
- Vender **150** en la Final → quedan 50; intentar **100 más** → rechazado.
- Resultado: 150/280 = **54% de ocupación** (coincide con las slides).

---

## 3) Guion de Nicolás — Información, diseño y cierre [slides 9-13, ~3-4 min]

> Rol: estadísticas, calidad de datos, construcción a alto nivel, UML y cierre.

"Gracias, Elías. Después del flujo principal, me enfoco en la **información** que el
sistema entrega y en por qué está **preparado para crecer**.

La sección de **estadísticas** transforma la actividad de la agenda en información útil:
total de eventos, confirmados, pendientes, entradas vendidas, cupo total, **porcentaje de
ocupación** y categorías presentes. También muestra el **reglamento del deporte** —en el
ejemplo, futsal—, lo que refuerza que es una agenda **especializada**, no genérica. En la
demo vimos dos eventos, uno confirmado y otro pendiente, y un 54% de ocupación calculado
automáticamente.

Sobre **calidad de datos**: el sistema valida la fecha, exige cupo positivo y bloquea la
sobreventa. Y ante un dato incorrecto **no se rompe**: lo vuelve a pedir.

También hay un **módulo de análisis** que lista los confirmados, genera resúmenes y
ordena por criterios como fecha o nombre.

A nivel de **construcción**, sin entrar en código, el sistema está organizado en capas:
la **interfaz de consola** (muestra el menú y pide datos), el **motor de gestión**
(administra eventos, cupos, ventas y estadísticas) y la **especialización deportiva** (el
reglamento del deporte). En el **diagrama de clases (UML)** se ve esa estructura: la
agenda deportiva hereda de la agenda general y la agenda contiene los eventos.

Esa separación permite **crecer**: se podría reemplazar la consola por una interfaz
gráfica o web reutilizando la misma lógica, o sumar nuevos deportes sin rehacer el
sistema. Como mejoras futuras: persistencia de datos, reportes exportables o usuarios con
permisos.

En conclusión, el sistema cumple el objetivo: gestionar eventos desde consola, validar
datos, controlar ventas, consultar información y analizar la agenda. Una solución simple
pero completa. Con esto cerramos. **Muchas gracias, quedamos atentos a sus preguntas.**"

---

## Consejos para practicar

- **No memorizar palabra por palabra**: practicar el orden y las ideas; debe sonar natural.
- **Hablar como presentación de producto**: evitar "en esta clase hicimos…"; usar "el
  sistema permite…", "la solución valida…".
- **Coordinar la demo**: usar siempre los mismos datos de ejemplo (los de arriba).
- **Responder con evidencia**: conectar la respuesta con lo que se ve en consola o en las
  estadísticas.
- **Cuidar el tiempo**: cada uno prioriza sus ideas centrales, sin entrar en detalles de
  código.

> Las **preguntas técnicas sobre el código** (las que el profe hace en la defensa
> individual) están en los guiones individuales: `guion_elias_evento.md`,
> `guion_enzo_coleccion.md`, `guion_nicolas_herencia.md` y `preguntas_comunes.md`.
