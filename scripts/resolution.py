"""
Fichero donde se encuentran las funciones relevantes para el 
procesamiento de la resolución en las imágenes que se desean procesar.
"""

# IMPORTS -----
import os
from PIL import Image
from .minify_images import minify

# FUNCTIONS -----

def process_image(image_path, output_path, desired_width, desired_height):
    
    """
    Se encarga de aplicar el procesamiento necesario a una imagen de
    entrada, para cambiar su resolución y optimizarla en formato PNG.
    
    La imagen resultante se almacena en el directorio de salida.
    
    params:
        image_path: str
            Ruta de la imagen a procesar.
        output_path: str
            Ruta donde se almacenará la imagen procesada.
        desired_width: int
            Ancho deseado de la imagen.
        desired_height: int
            Alto deseado de la imagen.
    returns:
        None
    """
    
    # Nombre de la imagen
    image_name = os.path.basename(image_path)
    new_image_name = os.path.splitext(image_name)[0] + '.png'
    
    try:
        with Image.open(image_path) as img:
            
            # Redimensiono la imagen
            new_img = img.resize((desired_width, desired_height),
                                 Image.LANCZOS)
            
            # Creo una nueva imagen con el tamaño exacto y pego
            # la imagen redimensionada en el centro.
            final_img = Image.new("RGB",
                                  (desired_width, desired_height))
            final_img.paste(new_img,
                            ((desired_width - new_img.width) // 2,
                             (desired_height - new_img.height) // 2))
            
            # Guardo la imagen en formato PNG
            final_img.save(os.path.join(output_path, new_image_name),
                           format="PNG",
                           optimize=True)
            
            # Minifico la imagen resultante
            minify(os.path.join(output_path, new_image_name),
                   os.path.join(output_path, new_image_name))
            
    except Exception as e:
        print(f'No ha sido posible procesar la imagen {image_name}: {e}')