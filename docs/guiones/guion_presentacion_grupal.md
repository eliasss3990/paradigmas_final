# Guion de presentación grupal — Grupo 15

Libreto que acompaña a la presentación (`presentacion_G15.pptx`). El enfoque es una
**demo de producto (estilo UAT)**: explicamos *qué hace el sistema y qué valor da* a
alguien no técnico, **sin mostrar código**. El detalle slide por slide está en
`contenido_ppt.md`.

**Duración:** ~10 min de presentación + preguntas.
**Reparto sugerido** (ajustable): Elias (slides 1-4) · Enzo (5-8) · Nicolas (9-12).
Cada uno debe poder responder preguntas de TODA la app.

**Antes de empezar:** abrir el PPT en pantalla completa y tener la consola lista en
otra ventana (`python3 proyecto_G15.py`) para la demo en vivo.

---

## Parte 1 — Apertura y problema · Elias [slides 1-3, ~2 min]

- **Slide 1 (portada):** "Buenas, somos el Grupo 15. Les presentamos nuestro sistema
  de gestión de eventos."
- **Slide 2 (agenda):** "Vamos a ver el problema, la solución, una demo en vivo, y
  cómo lo construimos."
- **Slide 3 (el problema):** "Organizar eventos sin una herramienta lleva al caos:
  sobreventa de entradas, no saber qué está confirmado, no tener una visión global."

## Parte 2 — La solución y funcionalidades · Elias→Enzo [slides 4-5, ~1.5 min]

- **Slide 4 (la solución):** "Nuestra app centraliza todo. Lo importante: aplica las
  reglas sola (no te deja sobrevender) y siempre tenés la foto del estado."
- **Slide 5 (funcionalidades):** "Estas son las ocho capacidades. Las mostramos
  funcionando."

## Parte 3 — DEMO EN VIVO · Enzo [slides 6-8 como apoyo, ~3-4 min]

> Cambiar a la consola. El PPT (slides 6, 7, 8) queda de apoyo visual; el foco es la app.

**Guion de la demo (qué hacer y qué decir):**

1. **Crear la agenda:** "Pongo nombre 'Liga Verano' y deporte 'Futsal'." → escribir.
2. **Agregar la final** (opción 1): nombre 'Final del Torneo', fecha 2026-07-20,
   lugar, categoría 'deportivo', cupo 200.
   - **Mostrar validación:** "Si escribo una fecha mal, miren —la rechaza y me la
     vuelve a pedir." → escribir una fecha inválida a propósito, luego la correcta.
3. **Agregar un segundo evento** (una charla o taller) para tener variedad.
4. **Listar** (opción 2) y **buscar** 'final' (opción 3); **filtrar** por 'deportivo'
   (opción 4).
5. **Vender entradas** (opción 6): vender 150 de la final. Luego **intentar vender
   100 más** → "No me deja, no hay cupo. Esta es la regla central del sistema."
6. **Confirmar** la final (opción 5).
7. **Estadísticas** (opción 7): "Acá está la foto completa —total, confirmados, la
   ocupación de la colección, las categorías y el reglamento del deporte." (señalar
   el porcentaje que aparezca; NO decir un número de memoria).
8. **Módulo funcional** (opción 8): mostrar las tres (confirmados, resumen, ordenar
   por fecha). "Esta es la parte de análisis."
9. Salir (opción 9). Volver al PPT.

## Parte 4 — Cómo está construido · Nicolas [slides 9-12, ~2.5 min]

- **Slide 9 (cómo está construido):** "Sin entrar en código: tres piezas —el evento
  individual, la agenda que los agrupa, y la agenda deportiva especializada. Y algo
  clave: separamos la lógica de la pantalla."
- **Slide 10 (UML):** "Este es el modelo. La agenda deportiva hereda de la agenda
  general; la agenda contiene los eventos; cada dato sensible está validado."
- **Slide 11 (pensado para crecer):** "Como la lógica está separada de la interfaz,
  mañana podríamos ponerle una interfaz gráfica reutilizando el mismo motor. Y sumar
  un deporte nuevo es trivial."
- **Slide 12 (cierre):** "En resumen: centraliza, valida y analiza. Gracias, quedamos
  atentos a las preguntas."

---

## Recordatorios

- **No leer las slides**: son apoyo; hablar mirando al profe.
- En la demo, **provocar a propósito** los rechazos (fecha inválida, sobreventa):
  demuestran robustez y suman muchísimo.
- Las preguntas serán técnicas y a alto nivel ("¿qué pasaría si esa validación
  estuviera en otro módulo?"). Ver `preguntas_comunes.md` y los guiones individuales.
- Si no sabés algo con certeza, razoná en voz alta desde el diseño; no inventes.
