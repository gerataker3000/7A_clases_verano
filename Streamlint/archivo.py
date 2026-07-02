# Importamos os para trabajar con nombres y extensiones de archivos
import os


# Creamos la clase Archivo
class Archivo:

    # Constructor de la clase
    def __init__(self, archivo_subido):

        # Guardamos el archivo que viene desde Streamlit
        self.archivo_subido = archivo_subido

        # Guardamos el nombre del archivo
        self.nombre = archivo_subido.name

    # Metodo para obtener la extension del archivo
    def obtener_extension(self):

        # Separamos el nombre del archivo y obtenemos la extension
        return os.path.splitext(self.nombre)[1]

    # Metodo para validar si el archivo es .txt
    def es_txt(self):

        # Retornamos True si la extension es .txt
        return self.obtener_extension() == ".txt"

    # Metodo para leer el contenido del archivo
    def leer(self):

        # Leemos el archivo como bytes
        contenido_bytes = self.archivo_subido.read()

        # Convertimos los bytes a texto
        contenido_texto = contenido_bytes.decode("utf-8")

        # Retornamos el texto del archivo
        return contenido_texto

    # Metodo para regresar informacion del archivo
    def obtener_info(self):

        # Retornamos un diccionario con informacion simple
        return {
            "nombre": self.nombre,
            "extension": self.obtener_extension()
        }