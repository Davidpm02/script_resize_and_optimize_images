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
    except Exception as e:
        print(f'Error al conectar con la API de Minify: {e}')
        return False


def minify_image(image_path, output_path):
    
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
    
    try:
        # Compruebo la conexión
        if not check_connection():
            return
        
        # Minifico la imagen
        source = tinify.from_file(image_path)
        source.to_file(os.path.join(output_path, image_path.split('/')[-1]))
    except Exception as e:
        print(f'Error al minificar la imagen {image_path.split('/')[-1]}: {e}')