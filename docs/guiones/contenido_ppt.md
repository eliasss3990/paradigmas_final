# Contenido de la presentación — Grupo 15

Presentación estilo **demo de producto (UAT)**: alto nivel, enfocada en *qué hace el
sistema y qué valor entrega*, no en el código. Acompaña a la demo en vivo de la app.

**Formato:** 12 slides · ~10 min · 16:9
**Archivo generado:** `presentacion_G15.pptx`
**Reparto sugerido** (ajustable): Elias (slides 1-4) · Enzo (5-8) · Nicolas (9-12).

---

## Slide 1 — Portada
**Título:** Sistema de Gestión de Eventos
**Tagline:** Organizá, controlá y analizá tus eventos en un solo lugar
**Pie:** Grupo 15 · Paradigmas de la Programación · FP-UNA · 2026
**Integrantes:** Elias Gonzalez · Enzo Dominguez · Nicolas Bareiro

> Notas del orador: "Buenas. Somos el Grupo 15 y les vamos a presentar nuestro
> sistema de gestión de eventos. La idea es mostrarles qué hace, cómo se usa y qué
> problema resuelve, y después una demostración en vivo."

---

## Slide 2 — Agenda
**Título:** Qué vamos a ver
**Bullets:**
- El problema que resolvemos
- La solución y su propuesta de valor
- Recorrido por las funcionalidades (demo en vivo)
- Control de cupo y validaciones
- Información y estadísticas
- Cómo está construido y por qué

> Notas: "Este es el recorrido. Arrancamos por el problema, vemos el sistema
> funcionando, y cerramos con cómo lo diseñamos."

---

## Slide 3 — El problema
**Título:** El problema
**Bullets:**
- Organizar muchos eventos sin una herramienta se vuelve caótico
- Riesgo de **sobrevender** entradas más allá de la capacidad
- Se pierde el control de **qué está confirmado** y qué no
- No hay una **visión rápida** del estado general (ocupación, totales)

> Notas: "Cualquiera que organice eventos —una liga, un ciclo de charlas— sin una
> herramienta termina con planillas sueltas. Dos dolores típicos: vender más
> entradas que el cupo, y no saber de un vistazo qué está confirmado."

---

## Slide 4 — La solución
**Título:** Nuestra solución
**Subtítulo:** Una aplicación que centraliza la gestión de una agenda de eventos
**Bullets (propuesta de valor):**
- Registro centralizado de todos los eventos
- Venta de entradas con **control automático de cupo**
- Seguimiento de confirmaciones
- Estadísticas inmediatas de la colección
- Búsqueda y filtrado al instante

> Notas: "Nuestra solución centraliza todo en un solo lugar. Lo importante: las
> reglas se aplican solas —el sistema no te deja sobrevender— y siempre tenés la
> foto del estado actual."

---

## Slide 5 — Funcionalidades principales
**Título:** Todo lo que podés hacer
**Grid de funcionalidades (tarjetas):**
1. Registrar eventos
2. Listar y consultar
3. Buscar por nombre
4. Filtrar por categoría
5. Vender entradas
6. Confirmar eventos
7. Ver estadísticas
8. Análisis avanzado

> Notas: "Estas son las ocho capacidades del sistema. Ahora las mostramos
> funcionando."

---

## Slide 6 — Recorrido por el sistema (demo en vivo)
**Título:** El sistema en acción
**Flujo de la demo:**
- Creamos la agenda (nombre + deporte de especialización)
- Cargamos un par de eventos
- Los listamos, buscamos y filtramos por categoría

> Notas: "Pasamos a la demo. Creo la agenda 'Liga Verano', deporte futsal. Cargo la
> final del torneo y una charla. Los listo, busco 'final', filtro por categoría
> deportivo." (HACER EN VIVO en la consola.)

---

## Slide 7 — Control de cupo y validaciones
**Título:** Un sistema que cuida tus datos
**Bullets:**
- **No permite sobrevender:** si no hay cupo, rechaza la venta
- **Valida la fecha:** solo acepta formato AAAA-MM-DD real
- **Valida el cupo:** debe ser un número positivo
- **No se rompe** ante datos mal ingresados: vuelve a pedirlos
- Las entradas vendidas **no se pueden alterar** a mano

> Notas: "Acá está la confianza del sistema. Voy a intentar vender más que el cupo
> —no me deja—. Voy a meter una fecha inválida —la rechaza y me la pide de nuevo—.
> Esto es lo que evita los errores típicos." (DEMOSTRAR los rechazos en vivo.)

---

## Slide 8 — Información y estadísticas
**Título:** La foto completa, al instante
**Bullets:**
- Total de eventos, confirmados y pendientes
- **Ocupación** de la colección (entradas vendidas / cupo total)
- Categorías presentes
- Reglamento del deporte de la agenda
- Análisis avanzado: listar confirmados, resúmenes y ordenamientos

> Notas: "Con una opción tengo el panorama: cuántos eventos, cuántos confirmados, la
> ocupación general, las categorías. Y un módulo de análisis para listar los
> confirmados, ver resúmenes y ordenar por distintos criterios." (MOSTRAR
> estadísticas y módulo funcional en vivo.)

---

## Slide 9 — Cómo está construido
**Título:** Cómo está construido (en simple)
**Bullets:**
- **Evento:** cada evento individual, con sus datos y reglas
- **Agenda de eventos:** el contenedor que gestiona la colección
- **Agenda deportiva:** una agenda especializada en un deporte
- La **lógica** está separada de la **pantalla**: el corazón del sistema no depende
  de cómo se muestre

> Notas: "Sin entrar en código: modelamos el sistema en tres piezas. El evento
> individual, la agenda que los agrupa, y una agenda especializada por deporte. Y
> algo clave: separamos la lógica de la interfaz."

---

## Slide 10 — El modelo en un vistazo
**Título:** El modelo en un vistazo
**Contenido:** Diagrama UML (`diagramas/diagrama_G15.png`)

> Notas: "Este es el diagrama de clases. La agenda deportiva hereda de la agenda
> general —reutiliza todo y agrega lo suyo—, y la agenda contiene los eventos. Cada
> dato sensible está protegido con validación."

---

## Slide 11 — Pensado para crecer
**Título:** Diseñado para crecer
**Bullets:**
- La lógica está **desacoplada** de la interfaz de consola
- Se podría agregar una **interfaz gráfica o web** reutilizando el mismo motor
- Nuevos deportes o tipos de agenda se suman **sin reescribir** lo existente
- Código validado, documentado y con diagrama técnico

> Notas: "El sistema está pensado para crecer. Hoy es de consola, pero como la
> lógica está separada, mañana le podríamos poner una interfaz gráfica sin tocar el
> motor. Y sumar un deporte nuevo es trivial."

---

## Slide 12 — Cierre
**Título:** Gracias
**Bullets:**
- Sistema de gestión de eventos: centraliza, valida y analiza
- Cumple los requisitos del proyecto: POO, módulo funcional, documentación
- ¿Preguntas?
**Pie:** Grupo 15 · FP-UNA · 2026

> Notas: "En resumen: un sistema que centraliza la gestión, aplica las reglas solo y
> da la información al instante. Gracias, quedamos atentos a las preguntas."
