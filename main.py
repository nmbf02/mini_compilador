# main.py
from lexer import test_lexer

with open("ejemplos/ejemplo1.txt", "r") as file:
    data = file.read()

print("Tokens reconocidos:")
test_lexer(data)
