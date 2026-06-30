# Importa ANTLR4 para funciones
from antlr4 import*
from ExprLexer import ExprLexer
# Lo que obtiene es la entrada , analiza el texto y lo separa en tokes
lexer = ExprLexer(InputStream(input("? ")))
# Toma los tokens que produjo el lexer y los guarda en un flujo/lista
tokens = CommonTokenStream(lexer)
tokens.fill()
print(tokens)


for token in tokens.tokens:
    print("Texto ", token.text)
    print("Linea ", token.line)
    print("Columna ", token.column)
    nombre_token = lexer.symbolicNames[token.type]
    print("Tipo ", nombre_token)
    
    print("-------------------")