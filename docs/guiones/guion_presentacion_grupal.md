# Guion de presentación grupal — Grupo 15

Flujo de la exposición oral. El foco es **mostrar la app funcionando** y explicar
**qué hace y por qué**, no recorrer el código línea por línea. Después vienen las
preguntas individuales (ver los otros guiones).

**Duración estimada:** 8–10 min de presentación + preguntas.
**Reparto sugerido** (ajustable): Elias abre y hace la demo · Enzo explica modelado
y UML · Nicolas cierra con documentación técnica. Igual cada uno debe poder
responder preguntas de TODA la app.

---

## Bloque 1 — Apertura y contexto [~1 min] · (Elias)

"Buenas. Somos el Grupo 15. Nuestro dominio asignado es **gestión de eventos**.
El sistema permite administrar una agenda de eventos —por ejemplo una liga
deportiva— desde una aplicación de consola: cargar eventos, vender entradas
controlando el cupo, confirmarlos, filtrarlos y sacar estadísticas.

El problema que resuelve: organizar eventos sin herramientas suele llevar a
sobrevender entradas o perder el control de qué está confirmado. Nuestro sistema
centraliza eso y valida las reglas automáticamente."

---

## Bloque 2 — Demo en vivo [~3 min] · (Elias)

> Ejecutar `python3 proyecto_G15.py` y mostrar, explicando el "por qué" de cada paso.

**Guion de la demo (qué hacer y qué decir):**

1. **Inicio:** "Al arrancar pide el nombre de la colección y el deporte de
   especialización. Pongo 'Liga Verano' y 'Futsal'." → escribir.

2. **Agregar evento (opción 1):** "Cargo la final del torneo." → nombre, fecha,
   lugar, categoría 'deportivo', cupo 200.
   *Por qué:* "Fíjense que si pongo una fecha mal escrita, el sistema la rechaza y
   me la vuelve a pedir —validamos el formato—." (mostrarlo a propósito).

3. **Agregar otro** (una charla o taller) para tener variedad de categorías.

4. **Vender entradas (opción 6):** vender 150 de la final.
   *Por qué:* "Acá está la regla central: si intento vender más que el cupo, no me
   deja." → intentar vender 100 más y mostrar que lo rechaza.

5. **Confirmar (opción 5):** confirmar la final.

6. **Estadísticas (opción 7):** "Muestra total, confirmados, ocupación (75%),
   categorías y el reglamento del deporte." → señalar la ocupación y el reglamento.

7. **Módulo funcional (opción 8):** mostrar las tres: confirmados, resumen y
   ordenar por fecha. *Por qué:* "Esto es la parte funcional, con filter, map y
   sorted."

8. Salir (opción 9).

---

## Bloque 3 — Cómo lo modelamos [~2 min] · (Enzo)

"Brevemente cómo está diseñado. Usamos **tres clases** con dos niveles de
abstracción:

- **`Evento`**: la entidad individual. Encapsula sus datos y sus reglas (el cupo,
  las entradas vendidas).
- **`AgendaEventos`**: la colección. Centraliza agregar, buscar, filtrar y las
  estadísticas.
- **`EventoDeportivo`**: hereda de `AgendaEventos`, es una agenda especializada en
  un deporte; agrega el reglamento y amplía las estadísticas.

Una decisión clave: **separamos la lógica de la interfaz**. El modelo no usa
`print` ni `input`; la consola es la única capa que interactúa con el usuario. Eso
nos permitiría cambiar a una interfaz gráfica reutilizando el mismo modelo.

Y aparte está el **módulo funcional**: tres funciones con filter, map y sorted que
operan sobre los objetos."

---

## Bloque 4 — Diagrama UML [~1.5 min] · (Enzo)

> Mostrar `diagramas/diagrama_G15.png` en pantalla.

"Este es el diagrama de clases. Se ven las tres clases con sus atributos y métodos.
Hay dos relaciones:

- La **herencia**: `EventoDeportivo` apunta a `AgendaEventos` con el triángulo
  hueco —es una agenda especializada—.
- La **composición**: `AgendaEventos` contiene de 0 a muchos `Evento` (el rombo
  relleno). Cada evento pertenece a una sola agenda.

Las properties están marcadas: `cupo_maximo` y `fecha` con validación,
`entradas_vendidas` de solo lectura, y las calculadas."

---

## Bloque 5 — Documentación técnica [~1.5 min] · (Nicolas)

> Mostrar `docs/documentacion_G15.md`.

"La documentación técnica tiene las siete secciones que pide la consigna: carátula,
descripción del sistema, decisiones de diseño, el diagrama UML, la descripción de
cada clase y función, las instrucciones de ejecución y la reflexión comparativa.

En decisiones de diseño explicamos por qué elegimos herencia para la colección
especializada, y por qué separamos el modelo de la interfaz. La reflexión compara
nuestro código con el TPI 1 y el TPI 2 —cómo pasamos de diccionarios y estado
global a objetos encapsulados—, y está también al final del archivo de código en
comentarios, con referencias a las funciones concretas."

---

## Bloque 6 — Cierre [~30 seg] · (cualquiera)

"En resumen: cumplimos los requisitos —las tres clases con herencia real y
`super()`, el módulo funcional con filter/map/sorted, el menú completo— y cuidamos
que el código sea mantenible y la lógica esté desacoplada de la interfaz. Quedamos
atentos a las preguntas."

---

## Recordatorios para todos

- **No leer de memoria**: practicar hasta que salga natural.
- **Cada uno responde por SU parte** en las preguntas (ver guiones individuales),
  pero todos deben entender la app completa.
- Si el profe pregunta algo que no sabés con certeza, mejor razonar en voz alta que
  inventar. "Lo modelé así porque…" suma más que una respuesta memorizada y dudosa.
- Tener el código y el UML abiertos y listos para señalar.
