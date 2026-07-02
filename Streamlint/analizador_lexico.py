# Importamos herramientas principales de ANTLR
from antlr4 import InputStream, CommonTokenStream, Token

# Importamos ErrorListener para capturar errores lexicos
from antlr4.error.ErrorListener import ErrorListener

# Importamos el lexer generado por ANTLR
from ExprLexer import ExprLexer


# Clase para guardar errores lexicos
class ErroresLexicos(ErrorListener):

    # Constructor
    def __init__(self):

        # Lista donde guardaremos los errores
        self.lista = []

    # Metodo que ANTLR ejecuta cuando encuentra error lexico
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):

        # Guardamos el error en la lista
        self.lista.append({
            "linea": line,
            "columna": column,
            "mensaje": msg
        })


# Clase para hacer el analisis lexico
class AnalizadorLexico:

    # Constructor
    def __init__(self):

        # Variable para guardar el lexer
        self.lexer = None

        # Variable para guardar los tokens
        self.tokens = None

        # Objeto para guardar errores lexicos
        self.errores = ErroresLexicos()

    # Metodo para analizar codigo
    def analizar(self, codigo):

        # Convertimos el texto en entrada para ANTLR
        entrada = InputStream(codigo)

        # Creamos el lexer
        self.lexer = ExprLexer(entrada)

        # Quitamos los errores normales de ANTLR
        self.lexer.removeErrorListeners()

        # Agregamos nuestro capturador de errores
        self.lexer.addErrorListener(self.errores)

        # Creamos el flujo de tokens
        self.tokens = CommonTokenStream(self.lexer)

        # Leemos todos los tokens
        self.tokens.fill()

    # Metodo para obtener tokens como lista
    def obtener_tokens(self):

        # Creamos una lista vacia
        resultado = []

        # Recorremos todos los tokens
        for token in self.tokens.tokens:

            # Saltamos EOF porque es el fin del archivo
            if token.type == Token.EOF:

                # Continuamos con el siguiente token
                continue

            # Obtenemos el nombre del token
            nombre_token = self.lexer.symbolicNames[token.type]

            # Agregamos el token a la lista
            resultado.append({
                "lexema": token.text,
                "token": nombre_token,
                "tipo": token.type,
                "linea": token.line,
                "columna": token.column
            })

        # Retornamos la lista de tokens
        return resultado

    # Metodo para obtener errores lexicos
    def obtener_errores(self):

        # Retornamos la lista de errores
        return self.errores.lista