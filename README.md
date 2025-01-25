# Script destinado al procesamiento de imágenes para webs

Este proyecto está diseñado para procesar imágenes de un directorio objetivo dado, generando un nuevo directorio donde residan las imágenes procesadas y minificadas.

## Estructura del Proyecto

El proyecto contiene los siguientes archivos y directorios:

- `script.py`: Archivo principal del proyecto.
- `scripts/`: Directorio que contiene los scripts de procesamiento.
  - `resolution.py`: Script que contiene funciones para ajustar la resolución de las imágenes.

## Uso

Para utilizar este proyecto, sigue los siguientes pasos:

1. Clona el repositorio en tu equipo local.
2. Instala las dependencias necesarias, definidas en el fichero 'requirements.txt', en tu entorno virtual.
3. Ejecuta el script principal `script.py` proporcionando el directorio de imágenes objetivo y el directorio de salida para las imágenes procesadas.

## Ejemplo de Ejecución

```sh
python script.py --input_dir /ruta/al/directorio/de/imagenes --output_dir /ruta/al/directorio/de/salida
```
