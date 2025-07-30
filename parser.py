import ply.yacc as yacc
from lexer import tokens

# Lista para guardar las instrucciones válidas
instructions = []

# Reglas gramaticales

def p_program(p):
    'program : statement_list'
    p[0] = p[1]

def p_statement_list_multiple(p):
    'statement_list : statement statement_list'
    p[0] = [p[1]] + p[2]

def p_statement_list_single(p):
    'statement_list : statement'
    p[0] = [p[1]]

def p_statement_paper(p):
    'statement : PAPER NUMBER'
    p[0] = ('PAPER', p[2])

def p_statement_pen(p):
    'statement : PEN NUMBER'
    p[0] = ('PEN', p[2])

def p_statement_line(p):
    'statement : LINE NUMBER NUMBER NUMBER NUMBER'
    p[0] = ('LINE', p[2], p[3], p[4], p[5])

# Manejo de errores
def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}' (línea {p.lineno})")
    else:
        print("Error de sintaxis: fin de archivo inesperado")

# Construir el parser
# parser = yacc.yacc()
parser = yacc.yacc(debug=False, write_tables=False)
