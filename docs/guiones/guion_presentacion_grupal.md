# Guion de presentación grupal — Grupo 15

Libreto que acompaña a la presentación (`presentacion_G15.pptx`, 13 slides). Enfoque
**demo de producto (UAT)**: explicamos *qué hace el sistema y qué valor da*, **sin
mostrar código**. El detalle slide por slide está en `contenido_ppt.md`.

**Duración:** ~4-5 min por integrante (más la demo en vivo y las preguntas).
**Reparto** (interno — NO está en el PPT proyectado):
- **Enzo** abre, **presenta al grupo** y da el contexto → slides 1-4.
- **Elias** hace la **demostración en vivo** y recorre las capacidades → slides 5-9.
- **Nicolás** cierra con calidad, diseño y el UML → slides 10-13.

Cada uno debe poder responder preguntas técnicas de TODA la app (ver guiones
individuales y `preguntas_comunes.md`).

**Antes de empezar:** PPT en pantalla completa y la consola lista en otra ventana
(`python3 proyecto_G15.py`).

---

## Parte 1 — Apertura y contexto · ENZO [slides 1-4, ~4-5 min]

> Enzo es quien saluda y presenta al grupo.

- **Slide 1 (portada):** "Buenas. Somos el Grupo 15: Elías, Nicolás y yo, Enzo. Les
  presentamos nuestro Sistema de Gestión de Eventos, una aplicación de consola para
  administrar una agenda de eventos."
- **Slide 2 (qué entregamos):** "En resumen: un producto que centraliza eventos,
  controla cupos y muestra información de seguimiento. Hoy lo defendemos con una demo
  en vivo."
- **Slide 3 (el problema):** "Gestionar eventos a mano lleva a errores: datos
  incompletos, sobreventa de entradas y poca visibilidad del estado. Eso es lo que
  resolvemos."
- **Slide 4 (propuesta de valor):** "Tres pilares: control, trazabilidad y
  visibilidad. Estos números resumen la demo —cero sobreventas, 54% de ocupación—."
  → "Para verlo en acción, le paso la palabra a Elías."

## Parte 2 — Demostración en vivo · ELÍAS [slides 5-9, ~5 min]

> Las slides 5-9 son apoyo; el foco es la consola. Cambiar a la app.

- **Slide 5 (capacidades):** "Estas son las capacidades del sistema. Las muestro
  funcionando." → pasar a la consola.
- **Demo (apoyo: slides 6-9):**
  1. **Crear agenda**: nombre 'Liga Verano', deporte 'Futsal'.
  2. **Agregar 'Final del Torneo'**: fecha 2026-07-20, lugar, categoría 'deportivo',
     cupo 200. → **meter una fecha mal a propósito** y mostrar que la rechaza.
  3. **Agregar** un segundo evento (otra categoría) para tener variedad.
  4. **Listar / buscar 'final' / filtrar 'deportivo'**.
  5. **Vender 150 entradas**; luego **intentar 100 más** → "no me deja, no hay cupo".
  6. **Confirmar** un evento.
  7. **Estadísticas**: señalar ocupación, categorías y reglamento (no decir el número
     de memoria; leer el que aparezca).
  8. **Módulo funcional**: ordenar por fecha.
- "Volviendo a las slides: esto es lo que acaban de ver —el sistema en acción, el
  control de cupos y los indicadores." → paso la palabra a Nicolás.

## Parte 3 — Calidad, diseño y cierre · NICOLÁS [slides 10-13, ~4-5 min]

- **Slide 10 (calidad de datos):** "El sistema protege la calidad de datos: valida el
  formato de fecha, exige cupo positivo y bloquea la sobreventa. Ante un dato inválido,
  no se rompe: lo vuelve a pedir."
- **Slide 11 (cómo está construido):** "A alto nivel, tres capas: la interfaz de
  consola, el motor de gestión y la especialización deportiva. La lógica está separada
  de la pantalla, por eso puede crecer."
- **Slide 12 (UML):** "Este es el modelo de clases. La agenda deportiva hereda de la
  agenda general —reutiliza todo y agrega su reglamento—; la agenda contiene los
  eventos; y los datos sensibles están validados."
- **Slide 13 (gracias):** "En síntesis, el sistema demuestra un flujo completo:
  registrar, validar, vender, consultar y analizar. Gracias, quedamos atentos a las
  preguntas."

---

## Recordatorios

- **No leer las slides**: son apoyo; hablar mirando al profe.
- En la demo, **provocar a propósito** los rechazos (fecha inválida, sobreventa):
  demuestran robustez y suman muchísimo.
- Las preguntas serán técnicas y de arquitectura ("¿qué pasaría si esa validación
  estuviera en otro módulo?"). Ver `preguntas_comunes.md` y los guiones individuales.
- Si no sabés algo con certeza, razoná en voz alta desde el diseño; no inventes.
