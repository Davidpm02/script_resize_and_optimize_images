"""
Fichero principal del script. Ejecuta el script para el procesamiento
de imágenes que se encuentren en el directorio indicado.
"""

# IMPORTS -----
import os
import sys
import shutil

from scripts.resolution import process_image

# SCRIPT -----

if __name__ == "__main__":
    
    # Recibimos las rutas de los directorios enviados al script
    try:
        assert (len(sys.argv) == 3)
        input_dir = sys.argv[1]
        output_dir = sys.argv[2]
        
        # Comprobamos que los directorios existen
        assert (os.path.exists(input_dir))
        assert (os.path.exists(output_dir))
        
        # Consultamos al usuario las dimensiones deseadas de las imágenes
        desired_width = int(input("Introduce el ancho deseado de las imágenes: "))
        desired_height = int(input("Introduce el alto deseado de las imágenes: "))
        
        # Verificamos que las dimensiones introducidas son válidas
        assert (desired_width > 0)
        assert (desired_height > 0)
        
        # Lista con las extensiones de imágenes permitidas
        image_extensions = ["webp", "png", "jpg", "jpeg", "heif"]
        
        # Recorremos el listado de imágenes de entrada, y conservamos
        # los nombres de los ficheros con extensión permitida
        images_on_directory = []
        for file in os.listdir(input_dir):
            file_extension = file.split(".")[-1].lower()
            if (file_extension in image_extensions):
                images_on_directory.append(file)
        
        # Definimos un directorio temporal, donde copiamos las imágenes
        # cuyos nombres se encuentren dentro de 'images_on_directory'
        temp_directory = 'temporal_directory/'
        if (not os.path.exists(temp_directory)):	
            os.mkdir(f"{temp_directory}")
        
        # Copiamos las imagenes seleccionadas a este directorio
        for file in os.listdir(input_dir):
            if file in images_on_directory:
                shutil.copyfile(os.path.join(input_dir, file),
                                os.path.join(temp_directory, file))
       
        for image in os.listdir(temp_directory):
            # Procesamos la imagen (cambio de resolución y optimización).
            process_image(os.path.join(temp_directory, image),
                          output_dir,
                          desired_width,
                          desired_height) 
            
        else:
            # Elimino el directorio temporal
            shutil.rmtree(temp_directory)
            print(f'Las imágenes procesadas se han almacenado correctamente en: {output_dir}.')
    except AssertionError:
        print("Asegúrate de que has introducido correctamente las rutas de los directorios y que las dimensiones de salida con válidas.")
        