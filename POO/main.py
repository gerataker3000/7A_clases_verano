from archivo import Archivo
from analizador_lexico import AnalizadorLexico

#snake_case
# en Python, self sirve para referirse al objeto actual dentro de una clase y python obliga a ponerlo como primer parámetro en los métodos de instancia

class Main:

    def __init__(self):
        self.analizador = AnalizadorLexico()

    def ejecutar(self):
        ruta = input("Escribe la ruta del archivo: ")
        archivo = Archivo(ruta)

        if not archivo.existe():
            print("El archivo no existe")
            return

        if not archivo.es_el_tipo_correcto():
            print("El archivo debe ser .txt")
            return

        codigo = archivo.leer()

        archivo.imprimir_info()

        print("\nCODIGO ORIGINAL")
        print("-" * 40)
        print(codigo)

        self.analizador.analizar(codigo)

        self.analizador.imprimir_tokens()
        self.analizador.imprimir_errores()

# permite controlar el punto de inicio del programa y evita que el código principal se ejecute automáticamente al importar el archivo
if __name__ == "__main__":
    app = Main()
    app.ejecutar()