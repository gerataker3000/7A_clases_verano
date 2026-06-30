# Importar la clase antlr4
from antlr4 import *

# Analizador lexico
from ExprLexer import ExprLexer

# Convierte ese texto en una entrada que ANTLR pueda leer
# El lexer analiza el texto y lo separa en tokens
lexer = ExprLexer(InputStream(input("? ")))

# Toma los tokens que produjo el lexer y los guarda en un flujo/lista
# para que después los pueda usar el parser
# Sirve para que ANTLR tenga los tokens ordenados y preparados
# Toma lo que encontró el analizador léxico y conviértelo en una secuencia de tokens lista para usarse
tokens = CommonTokenStream(lexer)

# Hace que ANTLR lea todos los tokens de una vez y los guarde dentro de tokens
tokens.fill()

print(tokens.tokens)

print(f"{'LEXEMA':<15} {'TOKEN':<15} {'TIPO':<6} {'LINEA':<6} {'COLUMNA':<8}")
print("-" * 60)

for token in tokens.tokens:
    if token.type == Token.EOF:
        continue

    nombre_token = lexer.symbolicNames[token.type]

    print(f"{token.text:<15} {nombre_token:<15} {token.type:<6} {token.line:<6} {token.column:<8}")