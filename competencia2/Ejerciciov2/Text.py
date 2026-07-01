# Importa ANTLR4 para funciones
from antlr4 import*
from ExprLexer import ExprLexer
import sys


# Lo que obtiene es la entrada , analiza el texto y lo separa en tokes
input_stream = FileStream(sys.argv[1])


lexer = ExprLexer(input_stream)
# Toma los tokens que produjo el lexer y los guarda en un flujo/lista
tokens = CommonTokenStream(lexer)
tokens.fill()
print(tokens)


print(f"{'LEXEMA':<15} {'TOKEN':<15} {'TIPO':<6} {'LINEA':<6} {'COLUMNA':<8}")
print("-" * 60)

for token in tokens.tokens:
    if token.type == Token.EOF:
        continue

    nombre_token = lexer.symbolicNames[token.type]

    print(f"{token.text:<15} {nombre_token:<15} {token.type:<6} {token.line:<6} {token.column:<8}")