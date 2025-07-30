from lexer import lexer, test_lexer
from parser import parser
from semantic import validate_instruction
from symbol_table import add_symbol, print_symbol_table
from code_generator import generate_svg

# Leer el archivo de entrada
with open("ejemplos/ejemplo1.txt", "r") as file:
    data = file.read()

print("📥 Entrada:")
print(data)

# 1. Análisis Léxico
print("\n🔍 Tokens reconocidos:")
test_lexer(data)

# 2. Análisis Sintáctico
print("\n✅ Instrucciones válidas:")
result = parser.parse(data, lexer=lexer)

# 3. Validación Semántica y Construcción de Tabla de Símbolos
if result:
    errors = []
    for instr in result:
        err = validate_instruction(instr)
        if err:
            errors.append(err)
        else:
            add_symbol(instr)

    if errors:
        print("\n❌ Errores semánticos encontrados:")
        for e in errors:
            print(" -", e)
    else:
        print_symbol_table()
        generate_svg()  # Solo si no hay errores semánticos
else:
    print("❌ No se reconocieron instrucciones válidas.")
