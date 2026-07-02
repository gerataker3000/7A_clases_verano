# la clase AnalizadorLexico es una clase utilitaria o helper, porque agrupa funciones reutilizables para trabajar con la fase léxica

# Importamos las clases principales de ANTLR
from antlr4 import *

# Importamos ErrorListener para capturar errores lexicos
from antlr4.error.ErrorListener import ErrorListener

# Importamos el lexer generado por ANTLR
from ExprLexer import ExprLexer


# Clase para guardar errores lexicos
class ErroresLexicos(ErrorListener):

    # Constructor de la clase
    def __init__(self):

        # Creamos una lista vacia para guardar errores
        self.lista = []

    # Metodo que ANTLR ejecuta cuando encuentra un error
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):

        # Guardamos el error en la lista
        self.lista.append([line, column, msg])


# Clase principal del analizador lexico
class AnalizadorLexico:

    # Constructor de la clase
    def __init__(self):

        # Variable para guardar el lexer
        self.lexer = None

        # Variable para guardar los tokens
        self.tokens = None

        # Creamos el manejador de errores lexicos
        self.errores = ErroresLexicos()

    # Metodo para analizar el codigo
    def analizar(self, codigo):

        # Convertimos el texto en entrada para ANTLR
        entrada = InputStream(codigo)

        # Creamos el lexer usando la entrada
        self.lexer = ExprLexer(entrada)

        # Quitamos los errores normales de ANTLR
        self.lexer.removeErrorListeners()

        # Agregamos nuestro propio manejador de errores
        self.lexer.addErrorListener(self.errores)

        # Creamos el flujo de tokens
        self.tokens = CommonTokenStream(self.lexer)

        # Leemos todos los tokens
        self.tokens.fill()

    # Metodo para imprimir los tokens
    def imprimir_tokens(self):

        # Imprimimos titulo
        print("\nTOKENS")

        # Imprimimos separador
        print("-" * 70)

        # Imprimimos encabezados de la tabla
        print(f"{'LEXEMA':<15} {'TOKEN':<15} {'TIPO':<6} {'LINEA':<6} {'COLUMNA':<8}")

        # Imprimimos separador
        print("-" * 70)

        # Recorremos todos los tokens encontrados
        for token in self.tokens.tokens:

            # Saltamos el token final EOF
            if token.type == Token.EOF:

                # Continuamos con el siguiente token
                continue

            # Obtenemos el nombre del token
            nombre = self.lexer.symbolicNames[token.type]

            # Imprimimos los datos del token
            print(f"{token.text:<15} {nombre:<15} {token.type:<6} {token.line:<6} {token.column:<8}")

    # Metodo para imprimir errores lexicos
    def imprimir_errores(self):

        # Imprimimos titulo
        print("\nERRORES LEXICOS")

        # Imprimimos separador
        print("-" * 40)

        # Validamos si no hay errores
        if len(self.errores.lista) == 0:

            # Imprimimos mensaje si todo esta bien
            print("No hay errores lexicos")

        # Si existen errores
        else:

            # Recorremos la lista de errores
            for error in self.errores.lista:

                # Imprimimos linea columna y mensaje
                print(f"Linea {error[0]}, columna {error[1]}: {error[2]}")