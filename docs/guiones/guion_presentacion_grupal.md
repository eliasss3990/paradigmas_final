# Guion de presentación grupal — Grupo 15

Libreto que acompaña a la presentación (`presentacion_G15.pptx`, 11 slides). El enfoque
es una **demo de producto (estilo UAT)**: explicamos *qué hace el sistema y qué valor
da*, **sin mostrar código**. El detalle slide por slide está en `contenido_ppt.md`.

**Duración:** ~10 min + preguntas.
**Reparto** (interno — NO está en el PPT proyectado): **Enzo abre y presenta al grupo**
(slides 1-4) · **Elias** hace la demostración en vivo (slides 5-6) · **Nicolas** cierra
(slides 7-11). Cada uno debe poder responder preguntas de TODA la app.

**Antes de empezar:** abrir el PPT en pantalla completa y tener la consola lista en otra
ventana (`python3 proyecto_G15.py`).

---

## Parte 1 — Apertura, problema y solución · Enzo [slides 1-4, ~3 min]

- **Slide 1 (portada):** "Buenas, somos el Grupo 15: Elias, Nicolas y yo, Enzo. Les
  presentamos nuestro sistema de gestión de eventos."
- **Slide 2 (el problema):** "Gestionar eventos a mano lleva a errores: datos
  incompletos, sobreventa de entradas, perder el control de qué está confirmado."
- **Slide 3 (la solución):** "Nuestra app de consola centraliza todo: cargar eventos,
  controlar cupos, confirmar, vender entradas y consultar estadísticas."
- **Slide 4 (funcionalidades):** "Estas son las ocho capacidades del sistema." → dar
  paso a Elias para la demo.

## Parte 2 — DEMO EN VIVO · Elias [slides 5-6 como apoyo, ~3-4 min]

> Cambiar a la consola. Las slides 5-6 (recorrido y capturas) quedan de apoyo; el foco
> es la app en vivo.

1. **Crear la agenda:** nombre 'Liga Verano', deporte 'Futsal'.
2. **Agregar 'Final del Torneo'** (opción 1): fecha 2026-07-20, lugar, categoría
   'deportivo', cupo 200.
   - **Mostrar validación:** escribir una fecha inválida a propósito → "la rechaza y me
     la vuelve a pedir" → luego la correcta.
3. **Agregar un segundo evento** (charla/taller) para tener variedad.
4. **Listar** (2), **buscar** 'final' (3), **filtrar** por 'deportivo' (4).
5. **Vender entradas** (6): vender 150; luego **intentar 100 más** → "no me deja, no hay
   cupo. Esta es la regla central."
6. **Confirmar** (5) la final.
7. **Estadísticas** (7): "la foto completa —total, confirmados, ocupación de la
   colección, categorías y reglamento." (señalar el % que aparezca; no decirlo de memoria).
8. **Módulo funcional** (8): confirmados, resumen, ordenar por fecha.
9. Salir (9). Volver al PPT y pasar a Nicolas.

## Parte 3 — Beneficios y cierre · Nicolas [slides 7-11, ~2.5 min]

- **Slide 7 (beneficios):** "Control de cupo, trazabilidad de cada evento, visibilidad
  con estadísticas, validación de datos, simplicidad de uso y un diseño extensible."
- **Slide 8 (resultados):** "Acá está la evidencia concreta de lo que mostró Elias:
  rechazo de fecha inválida, venta controlada, indicadores en vivo."
- **Slide 9 (cómo está construido):** "Tres piezas —evento, agenda y agenda deportiva—,
  con la lógica separada de la interfaz; por eso puede crecer sin reescribir el motor."
- **Slide 10 (cierre):** "El sistema está listo y demuestra el flujo completo."
- **Slide 11 (gracias):** "Gracias, quedamos atentos a las preguntas."

---

## Recordatorios

- **No leer las slides**: son apoyo; hablar mirando al profe.
- En la demo, **provocar a propósito** los rechazos (fecha inválida, sobreventa):
  demuestran robustez y suman muchísimo.
- Las preguntas serán técnicas y de arquitectura ("¿qué pasaría si esa validación
  estuviera en otro módulo?"). Ver `preguntas_comunes.md` y los guiones individuales.
- Si no sabés algo con certeza, razoná en voz alta desde el diseño; no inventes.
