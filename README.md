# Extracción de Información de Recibos

## Descripción:
Este proyecto analiza los datos de compras de clientes en una tienda minoristas con sede en UK, con el objetivo de identificar diferentes grupos de clientes y planificar distintas estrategias dependiendo del comportamiento del cliente. 


## Tabla de Contenidos 
- [Datos](#datos)
- [Metodología](#metodología)
- [Resultados](#resultados)
- [Conclusión](#conclusión)

## Datos 
- El dataset utilizado proviene de la página "UC Irvine Machine Learning Repository", el dataser se llama [Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii), que es del año 2019.
- Las fechas de los datos están comprendidas entre 01/12/2009 y 09/12/2011, las cuales están divididas en 2 hojas de excel.
- Para este problema solo se agarraron los datos de la primera hoja, que son hasta el año 2010.

![Dataset](Imágenes/Dataset.png)

## Metodología 

### 1. Exploración de Datos 
- Se realizó una exploración inicial del dataset a cada parámetro.
- Se identificó los valores nulos o que no podrían aportar nada de valor.

### 2. Limpieza de Datos 
- Se realizó la eliminación de registros previamente determinados como inútiles.
- Se eliminaron 118414 registros, lo que representa el 22.54% del total de registros.

### 3. Reducción de Dimensionalidad 
- De los datos limpios, se decidió crear un nuevo dataframe con nuevas columnas que aporten más información:
  - **Customer ID**: Identificación del cliente.
  - **Monetary Value**: Suma del total de compras pertenecientes al cliente. 
  - **Frequency**: Número de facturas únicas del cliente.
  - **Recency**: Días desde la última compra.

- Se graficaron algunos diagramas para visualizar de mejor manera los nuevos registros.
 
![Gráfico de Barras](Imágenes/Gráfico_Barras.png)

![Gráfico de Cajas](Imágenes/Gráfico_Cajas.png)

- Se visualizaba que habían muchos datos atípicos en los parámetros creados.
- Se eliminó los registros atípicos, en lo que dio como resultado:

![Gráfico de Cajas Limpios](Imágenes/Gráfico_Cajas_No_Atípicos.png)

![Gráfico 3D de Dispersión de los Datos](Imágenes/Gráfico_Dispersión.png)

### 4. Normalización de Datos 
- Se aplicó la "Normalización Z-Score" para estandarizar las variables y que no afencten mucho en el algoritmo KMeans.

### 5. Implementación de Algoritmo KMeans 
- Se utilizó el algoritmo KMeans para agrupar a los clientes en diferentes clusters.
- Primero se iteró con muchos valores de "k" para determinar cuál valor es la mejor opción a elegir.
- Se utilizó el "Coeficiente de Silueta" para determinar de mejor manera el valor de "k".
- Al final de visualizó los datos con sus respectivos clusters.

![Clusters Creados](Imágenes/Clusters.png)

### 6. Análisis de los Grupos 
- Para finalizar se interpretó o dio un significado a los clusters creados.
- Se utilizó el "Gráfico de Violín" para determinar de mejor manera el comportamiento de los clientes en cada cluster.

![Grupos](Imágenes/Grupos.png)

## Resultados 
- Se identificó los patrones de comportamiento de compra de los clientes.
- Se clasificó a los clientes en diferentes grupos según su valor monetario, frecuencia de compra y recencia.
- También se determinó qué acciones realizar para cada grupo de clientes.

## Conclusión 
El análisis de datos permitió clasificar a los clientes en grupos distintos, lo cual puede ayudar a diseñar diferentes estrategias para atraer o mantener a los clientes.  
