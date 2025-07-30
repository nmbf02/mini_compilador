# code_generator.py

import os
from symbol_table import get_symbol_table

def generate_svg(output_path=None, canvas_size=100):
    table = get_symbol_table()

    # Establecer ruta por defecto si no se proporciona
    if not output_path:
        output_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "output.svg")

    paper_color = "#ffffff"
    pen_color = "#000000"

    svg_lines = []

    # Ajustar colores según "Paper" y "Pen"
    for instr in table:
        if instr["type"] == "PAPER":
            level = 255 - int(instr["params"][0] * 255 / 100)
            paper_color = f"rgb({level},{level},{level})"
        elif instr["type"] == "PEN":
            level = 255 - int(instr["params"][0] * 255 / 100)
            pen_color = f"rgb({level},{level},{level})"

    # Generar líneas
    for instr in table:
        if instr["type"] == "LINE":
            x1, y1, x2, y2 = instr["params"]
            svg_lines.append(
                f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{pen_color}" stroke-width="2" />'
            )

    # Esqueleto del SVG
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{canvas_size}" height="{canvas_size}">
  <rect width="100%" height="100%" fill="{paper_color}" />
  {chr(10).join(svg_lines)}
</svg>'''

    # Guardar archivo SVG
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"\n🖼 SVG generado: {output_path}")
