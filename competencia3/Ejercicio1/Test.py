from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser

entrada = input("Código: ")
lexer = ExprLexer(InputStream(entrada))
tokens = CommonTokenStream(lexer)
parser = ExprParser(tokens)
arbol = parser.root()

print("Hola mundo")

if parser.getNumberOfSyntaxErrors() == 0:
    print("El código es correcto")
    print("Árbol sintáctico:")
    print(arbol.toStringTree(parser))
else:
    print("El código tiene errores de sintaxis")

