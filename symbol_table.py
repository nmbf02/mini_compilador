# symbol_table.py

symbol_table = []

def add_symbol(instruction):
    entry = {
        "type": instruction[0],
        "params": instruction[1:]
    }
    symbol_table.append(entry)

def print_symbol_table():
    print("\n📌 Tabla de Símbolos:")
    for idx, symbol in enumerate(symbol_table):
        print(f"{idx+1}. {symbol['type']} -> {symbol['params']}")

def get_symbol_table():
    return symbol_table
