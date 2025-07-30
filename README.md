# 🧠 Mini Compilador - Lenguaje SBN (SVG by Numbers)

Este es un mini compilador desarrollado como parte de la **Tarea Semana 7**. Traduce instrucciones en un lenguaje personalizado tipo **SBN (SVG by Numbers)** a un archivo visual SVG. Implementa el flujo completo de análisis léxico, sintáctico, semántico, generación de tabla de símbolos y código intermedio.

Cuenta con una **interfaz gráfica en Tkinter** que permite cargar un archivo, analizarlo y ver directamente la imagen generada desde el SVG convertido a PNG.

---

## 📌 Funcionalidades

- ✅ Analizador Léxico (Lexer)
- ✅ Analizador Sintáctico (Parser)
- ✅ Analizador Semántico
- ✅ Tabla de Símbolos
- ✅ Generador de Código Intermedio (SVG)
- ✅ Interfaz Gráfica con Tkinter
- ✅ Conversión automática de SVG a PNG y visualización integrada
- ✅ Ejecutable `.exe` generado con PyInstaller
- ✅ Documentación clara y código organizado

---

## 📥 Ejemplo de Entrada (`ejemplos/ejemplo1.txt`)

```txt
Paper 100
Pen 0
Line 10 10 90 90
Line 90 90 10 90
Line 10 90 10 10
````

---

## 📤 Resultado (`output/output.svg` → PNG en GUI)

El compilador genera un archivo `output.svg` y lo convierte automáticamente a `.png` para mostrarlo en la interfaz.

---

## 🚀 Cómo ejecutar el compilador

### Opción 1: Código fuente (`.py`)

1. **Instalar dependencias:**

```bash
pip install ply pillow cairosvg
```

2. **Ejecutar la interfaz gráfica:**

```bash
python gui.py
```

3. **Cargar un archivo `.txt`, compilar y ver el resultado visual en la misma ventana**

---

### Opción 2: Ejecutable `.exe` (sin necesidad de Python)

1. Ir a la carpeta `dist/`
2. Ejecutar el archivo `gui.exe`
3. Usar la interfaz normalmente (ya empaquetada)

---

## 📂 Estructura del Proyecto

```
mini_compilador/
├── lexer.py
├── parser.py
├── semantic.py
├── symbol_table.py
├── code_generator.py
├── gui.py                ← Interfaz principal
├── ejemplos/
│   └── ejemplo1.txt
│   └── ejemplo2.txt
├── output/
│   └── output.svg        ← Archivo generado
│   └── temp.png          ← Imagen mostrada en GUI
├── dist/
│   └── gui.exe           ← Ejecutable (.exe) generado
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
* **PLY (Python Lex-Yacc)** – Lexer y Parser
* **Tkinter** – Interfaz gráfica
* **CairoSVG + Pillow** – Conversión de SVG a PNG
* **PyInstaller** – Generación del `.exe`

---

## 👩‍💻 Autora

**Nathaly Michel Berroa Fermin**
Tarea Semana 7 - Compiladores
Universidad Tecnológica de Santiago (UTESA)

---

## 📎 Licencia

Este proyecto es académico y libre de usar con fines educativos.
