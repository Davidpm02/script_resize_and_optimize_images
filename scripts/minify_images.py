"""
Contiene funciones auxiliares para llevar a cabo la minificación de 
imágenes utilizando la API de Minify.
"""

# IMPORTS -----
import os
import tinify
from dotenv import load_dotenv

# VARIABLES DE ENTORNO -----
# Cargo las variables de entorno definidas en el proyecto
load_dotenv()
api_key = os.getenv('API_KEY')

# FUNCTIONS -----

def check_connection():

    """
    Comprueba si la conexión a la API de Minify es correcta.

    returns:
        bool
    """

    try:
        tinify.key = api_key
        tinify.validate()
        print("DEBUG: Conexión a la API de Tinify exitosa.")
        return True
    except tinify.AccountError as e:
        print(f'DEBUG: Error de cuenta de Tinify: {e}')
        return False
    except tinify.ClientError as e:
        print(f'DEBUG: Error del cliente de Tinify: {e}')
        return False
    except tinify.ServerError as e:
        print(f'DEBUG: Error del servidor de Tinify: {e}')
        return False
    except Exception as e:
        print(f'DEBUG: Error general al conectar con la API de Tinify: {e}')
        return False
    return False


def minify(image_path, output_path):

    """
    Minifica una imagen utilizando la API de Minify.

    params:
        image_path: str
            Ruta de la imagen a minificar.
        output_path: str
            Ruta donde se almacenará la imagen minificada.

    returns:
        None
    """

    print(f"DEBUG: Intentando minificar la imagen: {image_path}")
    print(f"DEBUG: Guardando la imagen minificada en: {os.path.join(output_path, os.path.basename(image_path))}")

    try:
        # Compruebo la conexión
        if not check_connection():
            print("DEBUG: No se pudo minificar debido a un problema de conexión.")
            return

        # Minifico la imagen
        source = tinify.from_file(image_path)
        print("DEBUG: Imagen cargada correctamente en Tinify.")

        # Imprimir información ANTES de la compresión
        original_size = os.path.getsize(image_path)
        print(f"DEBUG: Tamaño original de la imagen: {original_size} bytes.")

        # Guardar en la ruta correcta
        source.to_file(os.path.join(output_path, os.path.basename(image_path)))
        print("DEBUG: Imagen guardada por Tinify.")

        # Imprimir información DESPUÉS de la compresión
        optimized_size = os.path.getsize(os.path.join(output_path, os.path.basename(image_path)))
        print(f"DEBUG: Tamaño optimizado de la imagen: {optimized_size} bytes.")
        reduction = 1 - (optimized_size / original_size)
        print(f"DEBUG: Reducción de tamaño: {reduction:.2%}")

        compression_count = tinify.compression_count
        print(f"DEBUG: Compresiones realizadas este mes: {compression_count}")

    except tinify.AccountError as e:
        print(f'DEBUG: Error de cuenta de Tinify al minificar {os.path.basename(image_path)}: {e}')
    except tinify.ClientError as e:
        print(f'DEBUG: Error del cliente de Tinify al minificar {os.path.basename(image_path)}: {e}')
    except tinify.ServerError as e:
        print(f'DEBUG: Error del servidor de Tinify al minificar {os.path.basename(image_path)}: {e}')
    except Exception as e:
        print(f'DEBUG: Error general al minificar la imagen {os.path.basename(image_path)}: {e}')