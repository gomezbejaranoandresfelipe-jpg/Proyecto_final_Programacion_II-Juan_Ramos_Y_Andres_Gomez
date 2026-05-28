# Datos del Proyecto - Titanic Dataset

Este directorio está reservado exclusivamente para el almacenamiento local de los conjuntos de datos del proyecto. Por directrices de almacenamiento y buenas prácticas de control de versiones, los archivos con extensión `.csv` están excluidos del repositorio remoto mediante el archivo `.gitignore`.

## 1. Enlace de Descarga Oficial
Los datos deben ser obtenidos directamente desde la plataforma Kaggle a través de la competencia oficial:
* **URL de la Competencia:** [Kaggle - Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic/data)

## 2. Archivos Requeridos
Para garantizar la correcta ejecución del pipeline y de los cuadernos de análisis, se necesita el siguiente archivo:
* `train.csv`: Conjunto de datos de entrenamiento que contiene las variables demográficas, socioeconómicas y la etiqueta de supervivencia de los pasajeros.

## 3. Instrucciones de Ubicación
Para replicar el análisis en un entorno local de manera satisfactoria:
1. Ingrese al enlace de Kaggle provisto arriba y descargue el archivo `train.csv`.
2. Mueva o copie el archivo descargado de su carpeta personal de descargas a este directorio local denominado `data/`.
3. Asegúrese de mantener estrictamente el nombre en minúsculas (`train.csv`) para evitar errores de rutas de lectura (`FileNotFoundError`) en los scripts de Python y Jupyter Notebooks.
