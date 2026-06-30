# Generación de la presentación (PPT)

Scripts que generan `../docs/presentacion_G15.pptx` (11 slides, estilo demo de
producto). Sirven para **regenerar la presentación** si cambia algún dato, sin
rehacerla a mano en PowerPoint.

## Archivos

| Archivo | Qué hace |
|---|---|
| `gen_mockups.py` | Genera las "capturas de pantalla" de la consola en `./mockups/` (PNG). |
| `build_ppt.py` | Arma el `.pptx` usando esas capturas. Genera `../docs/presentacion_G15.pptx`. |
| `requirements.txt` | Dependencias de Python. |

## Requisitos

- Python 3.10+
- Las librerías de `requirements.txt`: `python-pptx` (arma el PPT) y `Pillow` (imágenes).
- Fuentes monoespaciadas DejaVu (en Linux suelen estar en
  `/usr/share/fonts/truetype/dejavu/`). En otro sistema, editar las rutas `MONO`/`MONOB`
  al principio de `gen_mockups.py`.

## Cómo usarlo

```bash
# 1) (recomendado) crear un entorno virtual
python -m venv .venv
source .venv/bin/activate        # Linux/Mac
# .venv\Scripts\activate         # Windows

# 2) instalar dependencias
pip install -r requirements.txt

# 3) generar las capturas y luego el PPT (en este orden)
python gen_mockups.py
python build_ppt.py
```

El resultado queda en `../docs/presentacion_G15.pptx`.

## Cómo cambiar contenido

- **Integrantes**: variable `INTEGRANTES` al inicio de `build_ppt.py`.
- **Textos de las slides**: están inline en `build_ppt.py`, cada slide está separada por
  un comentario `# ===== SLIDE N =====`.
- **Capturas de la consola** (texto que se ve en las pantallas): editar las llamadas a
  `terminal(...)` en `gen_mockups.py` y volver a ejecutar ambos scripts.
- **Colores / estilo**: bloque "Paleta" al inicio de `build_ppt.py`.

## Nota

`./mockups/` se regenera con `gen_mockups.py`, por eso no se versiona (ver `.gitignore`).
El `.pptx` final sí se versiona, en `../docs/`.
