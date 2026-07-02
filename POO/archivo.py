# Importamos os para trabajar con rutas y archivos
import os

# la clase Archivo es una clase utilitaria o helper, porque agrupa funciones reutilizables para trabajar con archivos

# Creamos la clase Archivo
class Archivo:

    # Constructor de la clase
    def __init__(self, ruta):

        # Guardamos la ruta del archivo
        self.ruta = ruta

    # Metodo para saber si el archivo existe
    def existe(self):

        # Retorna True si el archivo existe, False si no existe
        return os.path.exists(self.ruta)

    # Metodo para obtener la extension del archivo
    def extension(self):

        # Separamos la ruta y obtenemos solo la extension
        return os.path.splitext(self.ruta)[1]

    # Metodo para validar si el archivo es .txt
    def es_el_tipo_correcto(self):

        # Comparamos si la extension es igual a .txt
        return self.extension() == ".txt"

    # Metodo para leer el contenido del archivo
    def leer(self):

        # Abrimos el archivo en modo lectura con codificacion utf-8
        with open(self.ruta, "r", encoding="utf-8") as archivo:

            # Retornamos todo el texto del archivo
            return archivo.read()

    # Metodo para imprimir informacion basica del archivo
    def imprimir_info(self):

        # Imprimimos titulo
        print("\nINFORMACION DEL ARCHIVO")

        # Imprimimos separador
        print("-" * 40)

        # Imprimimos la ruta del archivo
        print("Ruta:", self.ruta)

        # Imprimimos la extension del archivo
        print("Extension:", self.extension())