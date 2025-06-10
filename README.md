# Extracción de Información de Recibos

## Descripción:
Este proyecto analiza la información de recibos en formato PDF, para luego usar la información valiosa en generar un reporte en Power BI. 


## Tabla de Contenidos 
- [Datos](#datos)
- [Procedimiento](#metodología)
- [Resultados](#resultados)
- [Conclusión](#Conclusión)

## Datos 
- El dataset utilizado proviene de la página Kaggle, el dataser se llama [my receipts (pdf scans)]([https://archive.ics.uci.edu/dataset/502/online+retail+ii](https://www.kaggle.com/datasets/jenswalter/receipts)).
- El datase tiene desde el año 2017 hasta el 2024, pero para este caso solo trabajé con los correspondientes al 2018.

## Procedimiento

### 1. Recorrer todo los Archivos. 
- La primera parte se realizó un recorrido por cada una de las imágenes del dataset.
- Se guarda la ruta, país y tipo de transacción en variables.

### 2. Funciones para el Procesamiento de Información.
- Cada una de las imágenes se envió a una función para extraer el texto de la imagen, se usó la librería PyMuPDF, en concreto el módulo "fitz".
- Después se envía el texto extraido a una función para analizar el texto, se usó el LLM DeepSeek para el procesamiento de la información y que extraiga datos especificados en un determinado formato.
- Con esa respuesta se envió a otro LLM para que evalue si la respuesta enviada es correcta o no.

### 3. Guardado de Información
- Una vez que se determine que el resultado coincide con la información del PDF se envia a otra función para convertirlo en un dataframe.
- Si no coincide la información y ya hizo una cantidad de intentos, se almacena la ruta del PDF a una lista para informar que esos PDF's no se puideron evaluar de manera satisfactoria.

### 4. Almacenarlo en un DB 
- Una vez se recorrió todos los PDF's, el dataframe resultante con toda la información se convierte y almacena en una base de datos, en este caso usé SQLite.

### 5. Informe Power BI 
- Con los datos almacenados en la Base de Datos, cargué la información en un Power BI.
- Se editaron algunos datos para hacer los gráficos de manera más fácil.

![Power BI](Img_ReadMe/PBI.png)

## Resultados
- Se logró obtener la información de la mayoría de los PDF's sin problemas.
- También se pudo realizar una Dashboard decente que muestre los gastos de la persona/empresa que se realizaron en el año 2018.

## Conclusión 
- Los tiempos que se tomaron para procesar 1 sola imagen me tomaron en promedio entre 3 a 10 min aprox., si se tieme una GPU mejor los tiempos se pueden reducir, este también fue la razon por la que decidí trabajar solo con los PDF's del 2018 y no con todos los del dataset.
- Puede que con un mejor prompt y más corto de mejores resultados, sería cuestión de probar.
