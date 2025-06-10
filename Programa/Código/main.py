import os
import funciones
import pandas as pd
from sqlalchemy import create_engine

os.environ["OLLAMA_USE_GPU"] = "1"

df = pd.DataFrame(columns = ["empresa", "fecha", "conceptos", "importe", "moneda", "pais", "servicio", "valor USD"])
pdf_errores = []
# Diccionario de conversión de moneda a dólares del año 2018
tasa_cambio = {"dolar estadounidense": 1, "dolar canadiense": 0.7717, "euro": 1.1793, "yuan chino": 0.1514}

# Recorrer los recibos por país
for pais in sorted(os.listdir(".\Imágenes")):
    ruta = os.path.join(".\Imágenes", pais)

    # De cada país recorrer por servicio
    for servicio in sorted(os.listdir(ruta)):
        ruta = os.path.join(".\Imágenes", pais, servicio)

        # Obtener la ruta de la imagen deL recibo
        for pdf in os.listdir(ruta):
            ruta_pdf = os.path.join(ruta, pdf)

            # Extraer información de la imagen
            texto = funciones.extrear_texto_pdf(ruta_pdf)

            errores = 0

            while True:

                # Extraer datos importantes del PDF
                respuesta = funciones.obtener_informacion(pais, servicio, texto)
                
                # Determinar si están bien o no los datos
                evaluacion = funciones.evaluar_respuesta(texto, pais, servicio, respuesta)

                if evaluacion == "Yes":
                    break

                # Tolerancia de errores
                elif errores < 5:
                    errores += 1

                else:
                    respuesta = str(ruta_pdf)
                    break

            
            # Almacenar la ruta del PDF que no pudo extraer bien la información 
            if respuesta == str(ruta_pdf) or not respuesta.startswith("[["):
                pdf_errores.append(respuesta)
                print("PDF '{}' fallido.".format(str(pdf)))

            # Convertir a un data frame para poder trabajar con los datos 
            else:
                df = funciones.convertir_df(df, respuesta, pais, servicio)
                print("PDF '{}' analizado.".format(str(pdf)))
            
print("Todos los PDF's examinados")

# Convertir el tipo de datos de la columna "importe" a numérico
df["importe"] = pd.to_numeric(df["importe"], errors = "coerce")

# Obtener valor en USD del año correspondiente
df["valor USD"] = df.apply(lambda x: x["importe"] * tasa_cambio.get(x["moneda"], 1), axis = 1)

print("Data Frame completo")

# Crear db en SQLite
engine = create_engine("sqlite:///Código/recibos.db")

# Agregar nuevos datos al archivo existente
# Cambiar 'replace' por 'append' para agregar a la db
df.to_sql("recibos", engine, if_exists = "replace", index = False)

engine.dispose()