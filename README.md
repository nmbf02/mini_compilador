# 🧠 Mini Compilador - Lenguaje SBN (SVG by Numbers)

Este es un mini compilador desarrollado como parte de la Tarea Semana 7. Traduce instrucciones en un lenguaje personalizado tipo "SBN" a un archivo SVG visual, implementando un flujo completo de análisis léxico, sintáctico, semántico, tabla de símbolos y generación de código intermedio.

---

## 📌 Funcionalidades

- ✅ Analizador Léxico (Lexer)
- ✅ Analizador Sintáctico (Parser)
- ✅ Analizador Semántico
- ✅ Tabla de Símbolos
- ✅ Generador de Código Intermedio (SVG)
- ✅ Documentación clara y ejecutable generado

---

## 📥 Ejemplo de Entrada (`ejemplo1.txt`)

```txt
Paper 100
Pen 0
Line 10 10 90 90
Line 90 90 10 90
Line 10 90 10 10
````

---

## 📤 Resultado (`output/output.svg`)

Este archivo SVG es generado como salida visual del código. Puedes abrirlo en cualquier navegador.

---

## 🚀 Cómo ejecutar el compilador

1. **Clona este repositorio o descarga el ZIP**
2. **Instala dependencias (solo una):**

```bash
pip install ply
```

3. **Ejecuta el compilador:**

```bash
python main.py
```

4. **Visualiza la salida:**

Abre `output/output.svg` en tu navegador para ver el dibujo generado.

---

## 📂 Estructura del Proyecto

```
mini_compilador/
├── lexer.py
├── parser.py
├── semantic.py
├── symbol_table.py
├── code_generator.py
├── main.py
├── ejemplos/
│   └── ejemplo1.txt
├── output/
│   └── output.svg
└── README.md
```

---

## 🧪 Validaciones Semánticas

* `Paper` y `Pen` deben tener valores entre `0` y `100`
* `Line` debe tener exactamente 4 parámetros
* No se permiten coordenadas negativas

---

## 🛠 Herramientas utilizadas

* **Python 3.10+**
* **PLY (Python Lex-Yacc)** para análisis léxico y sintáctico
* SVG como salida visual

---

## 👨‍💻 Autor

Nathaly Michel Berroa Fermin
Tarea Semana 7 - Compiladores
Universidad Tecnológica de Santiago (UTESA)

---

## 📎 Licencia

Este proyecto es académico y libre de usar con fines educativos.
