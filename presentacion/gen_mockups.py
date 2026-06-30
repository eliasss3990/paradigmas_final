"""Genera las capturas (mockups) de la terminal de la app, con tildes correctas.

Las imágenes se usan como "capturas de pantalla" dentro de la presentación.
Salida: ./mockups/*.png

Uso:
    python gen_mockups.py
(requiere Pillow; ver README.md)
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "mockups")
os.makedirs(OUT, exist_ok=True)

# Colores estilo terminal
BG = (13, 17, 23); BAR = (28, 33, 40)
GREEN = (134, 239, 172); WHITE = (230, 237, 243); GRAY = (139, 148, 158)
CYAN = (86, 209, 222); AMBER = (245, 158, 11); RED = (248, 113, 113)

# Fuentes monoespaciadas (DejaVu suele venir en Linux; cambiar si hace falta)
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONOB = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"


def fnt(sz, bold=False):
    return ImageFont.truetype(MONOB if bold else MONO, sz)


def terminal(w, h, lines, fs=20, title="Sistema de Gestión de Eventos"):
    """Dibuja una ventana de terminal. lines: lista de (texto, color, bold)."""
    img = Image.new("RGB", (w, h), BG); d = ImageDraw.Draw(img)
    barh = 44
    d.rectangle([0, 0, w, barh], fill=BAR)
    for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        cx = 16 + i * 22
        d.ellipse([cx, barh // 2 - 6, cx + 12, barh // 2 + 6], fill=c)
    d.text((w // 2, barh // 2), title, fill=GRAY, font=fnt(fs - 4), anchor="mm")
    y = barh + 16; x = 20
    for txt, col, bold in lines:
        d.text((x, y), txt, fill=col, font=fnt(fs, bold)); y += int(fs * 1.5)
    d.rectangle([0, 0, w - 1, h - 1], outline=(40, 48, 58))
    return img


# 1) Menú principal
terminal(880, 760, [
    ("==============================================", GRAY, False),
    (" SISTEMA DE GESTIÓN DE EVENTOS", WHITE, True),
    (" Paradigmas de la Programación · FP-UNA", GRAY, False),
    ("==============================================", GRAY, False),
    ("", WHITE, False),
    ("Colección 'Liga Verano' iniciada.", GREEN, False),
    ("Deporte: Futsal", GREEN, False),
    ("", WHITE, False),
    ("--- MENÚ PRINCIPAL ---", CYAN, True),
    ("1. Agregar evento", WHITE, False),
    ("2. Mostrar todos los eventos", WHITE, False),
    ("3. Buscar por nombre", WHITE, False),
    ("4. Filtrar por categoría", WHITE, False),
    ("5. Marcar evento como confirmado", WHITE, False),
    ("6. Vender entradas", WHITE, False),
    ("7. Ver estadísticas", WHITE, False),
    ("8. Módulo funcional", WHITE, False),
    ("9. Salir", WHITE, False),
    ("Seleccione una opción: _", GREEN, True),
], fs=22).save(os.path.join(OUT, "mockup_menu.png"))

# 2) Alta + validación de fecha
terminal(940, 420, [
    ("--- AGREGAR EVENTO ---", CYAN, True),
    ("Nombre: Final del Torneo", WHITE, False),
    ("Fecha (AAAA-MM-DD): 20/07/2026", WHITE, False),
    ("Fecha inválida. Usá el formato AAAA-MM-DD.", AMBER, True),
    ("Fecha (AAAA-MM-DD): 2026-07-20", WHITE, False),
    ("Categoría: deportivo", WHITE, False),
    ("Cupo máximo: 200", WHITE, False),
    ("Evento 'Final del Torneo' agregado correctamente.", GREEN, True),
], fs=21).save(os.path.join(OUT, "mockup_alta.png"))

# 3) Venta con control de cupo
terminal(940, 420, [
    ("--- VENDER ENTRADAS ---", CYAN, True),
    ("  1. Final del Torneo | 0/200 entradas | pendiente", WHITE, False),
    ("Número de evento: 1", WHITE, False),
    ("Cantidad a vender: 150", WHITE, False),
    ("Vendidas 150. Disponibles: 50", GREEN, True),
    ("", WHITE, False),
    ("Cantidad a vender: 100", WHITE, False),
    ("No hay cupo suficiente. Disponibles: 50", RED, True),
], fs=21).save(os.path.join(OUT, "mockup_venta.png"))

# 4) Estadísticas
terminal(940, 460, [
    ("--- ESTADÍSTICAS ---", CYAN, True),
    ("Colección: Liga Verano", WHITE, False),
    ("Deporte (especialización): Futsal", WHITE, False),
    ("Total de eventos: 2", WHITE, False),
    ("Confirmados: 1 | Pendientes: 1", WHITE, False),
    ("Entradas vendidas: 150 / 280 (54% de ocupación)", GREEN, True),
    ("Categorías presentes: conferencia, deportivo", WHITE, False),
    ("Reglamento Futsal: 5 jugadores por equipo...", GRAY, False),
], fs=21).save(os.path.join(OUT, "mockup_stats.png"))

# 5) Módulo funcional
terminal(940, 420, [
    ("--- MÓDULO FUNCIONAL ---", CYAN, True),
    ("a. Nombres de eventos confirmados (filter + map)", WHITE, False),
    ("b. Resumen de la colección (map)", WHITE, False),
    ("c. Ordenar por criterio (sorted)", WHITE, False),
    ("Seleccione: c", GREEN, False),
    ("Criterio: fecha", WHITE, False),
    ("  1. Semifinal — 2026-07-18 ...", WHITE, False),
    ("  2. Final del Torneo — 2026-07-20 ...", WHITE, False),
], fs=21).save(os.path.join(OUT, "mockup_funcional.png"))

# 6) Filtrar por categoría
terminal(940, 420, [
    ("--- FILTRAR POR CATEGORÍA ---", CYAN, True),
    ("Categorías: concierto, conferencia, deportivo...", GRAY, False),
    ("Categoría: deportivo", WHITE, False),
    ("  1. Final del Torneo (deportivo) — 2026-07-20", WHITE, False),
    ("     Polideportivo | 150/200 entradas | confirmado", GREEN, False),
    ("  2. Semifinal (deportivo) — 2026-07-18", WHITE, False),
    ("     Polideportivo | 0/150 entradas | pendiente", WHITE, False),
], fs=21).save(os.path.join(OUT, "mockup_filtrar.png"))

print("Mockups generados en:", OUT)
print(sorted(os.listdir(OUT)))
