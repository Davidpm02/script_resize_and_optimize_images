# Procesamiento de imágenes para webs

Este proyecto está diseñado para procesar imágenes de un directorio objetivo dado, generando un nuevo directorio donde residan las imágenes procesadas y minificadas.

## Estructura del proyecto

El proyecto contiene los siguientes archivos y directorios:

- `script.py`: Archivo principal del proyecto.
- `scripts/`: Directorio que contiene los scripts de procesamiento.
  - `resolution.py`: Script que contiene funciones para ajustar la resolución de las imágenes.

## Uso

Para poder utilizar este script de la forma esperada, es necesario obtener una clave (key) para la API de Tinify. Puedes obtener más información al respecto
accediendo al siguiente [enlace](https://tinypng.com/developers).

Una vez hayas obtenido tu API-KEY, define un fichero .env dentro del entorno virtual, y crea una clave cuyo valor almacene tu API-KEY. De forma gratuita, tendrás acceso a 500 compresiones mensuales.

Para utilizar este proyecto, sigue los siguientes pasos:

1. Clona el repositorio en tu equipo local.
2. Instala las dependencias necesarias, definidas en el fichero 'requirements.txt', en tu entorno virtual.
3. Ejecuta el script principal `script.py` proporcionando el directorio de imágenes objetivo y el directorio de salida para las imágenes procesadas.
4. Revisa la ruta de destino y echa un vistazo a las imágenes procesadas y listas para utilizar.

## Ejemplo de ejecución

Una vez hayas clonado el contenido del repositorio, accede al directorio en cuestión y ejecuta el fichero `script.py`. En este caso, puedes ejecutar el fichero desde la propia terminal, enviando las rutas absolutas del directorio de imágenes que quieres procesar, y el directorio donde quieras almacenar las imágenes resultantes (envía estas rutas en los parámetros `--input_dir` y `--output_dir`, respectivamente).

```sh
python script.py --input_dir /ruta/al/directorio/de/imagenes --output_dir /ruta/al/directorio/de/salida
```

## Contacto

Si tienes preguntas, comentarios, o deseas discutir sobre posibles colaboraciones, no dudes en contactarme.

* **Email**: padish_dev@proton.me
* **LinkedIn**: [David Padilla Muñoz](https://www.linkedin.com/in/david-padilla-mu%C3%B1oz-52126725a/)
