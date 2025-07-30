# lexer.py
import ply.lex as lex

# Lista de tokens
tokens = (
    'PAPER',
    'PEN',
    'LINE',
    'NUMBER',
)

# Palabras clave
def t_PAPER(t):
    r'Paper'
    return t

def t_PEN(t):
    r'Pen'
    return t

def t_LINE(t):
    r'Line'
    return t

# Números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios y tabs
t_ignore = ' \t'

# Ignorar saltos de línea pero contar líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Errores
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Función de prueba
def test_lexer(data):
    lexer.input(data)
    for token in lexer:
        print(token)
