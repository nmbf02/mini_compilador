import tkinter as tk
from tkinter import filedialog
from lexer import get_tokens, lexer
from parser import parser
from semantic import validate_instruction
from symbol_table import symbol_table, add_symbol
from code_generator import generate_svg

import cairosvg
from PIL import Image, ImageTk
import os

class CompilerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Compilador - Nathaly Michel Berroa Fermin")

        # Área de entrada del código
        self.text = tk.Text(root, height=15, width=60)
        self.text.pack()

        # Botones
        tk.Button(root, text="Cargar archivo", command=self.load_file).pack(pady=2)
        tk.Button(root, text="Compilar", command=self.compile_code).pack(pady=2)

        # Área de salida
        self.output = tk.Text(root, height=15, width=60, bg="#f0f0f0")
        self.output.pack()

        # Área para mostrar imagen SVG como PNG
        self.canvas = tk.Label(root)
        self.canvas.pack(pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as f:
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, f.read())

    def compile_code(self):
        self.output.delete("1.0", tk.END)
        source = self.text.get("1.0", tk.END).strip()

        self.output.insert(tk.END, "📥 Código cargado:\n" + source + "\n")

        # 1. Tokens
        tokens = get_tokens(source)
        self.output.insert(tk.END, "\n🔍 Tokens:\n")
        for tok in tokens:
            self.output.insert(tk.END, tok + "\n")

        # 2. Sintaxis
        result = parser.parse(source, lexer=lexer)
        if not result:
            self.output.insert(tk.END, "\n❌ Error de sintaxis\n")
            return

        # 3. Semántica + tabla
        symbol_table.clear()
        errors = []
        for instr in result:
            err = validate_instruction(instr)
            if err:
                errors.append(err)
            else:
                add_symbol(instr)

        if errors:
            self.output.insert(tk.END, "\n❌ Errores semánticos:\n")
            for e in errors:
                self.output.insert(tk.END, f" - {e}\n")
            return

        # 4. Tabla de símbolos
        self.output.insert(tk.END, "\n📋 Tabla de símbolos:\n")
        for s in symbol_table:
            self.output.insert(tk.END, f"{s['type']} -> {s['params']}\n")

        # 5. Generar SVG
        generate_svg()
        self.output.insert(tk.END, "\n✅ SVG generado: output/output.svg\n")

        # 6. Mostrar imagen convertida
        try:
            cairosvg.svg2png(url="output/output.svg", write_to="output/temp.png")
            img = Image.open("output/temp.png")
            img = img.resize((300, 300))
            self.imgtk = ImageTk.PhotoImage(img)
            self.canvas.configure(image=self.imgtk)
        except Exception as e:
            self.output.insert(tk.END, f"\n⚠️ No se pudo cargar la imagen: {e}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = CompilerApp(root)
    root.mainloop()
