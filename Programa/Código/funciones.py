import ast
import fitz
import prompts
import ollama
import pandas as pd


def extrear_texto_pdf(ruta_pdf):
    """
    Extrae texto de un PDF.
    """
    img = fitz.open(ruta_pdf)
    texto = "\n".join([pagina.get_text("text") for pagina in img])
    return texto


def obtener_informacion(pais, servicio, texto):
    """
    Devuelve [['nombre_empresa', 'fecha', 'conceptos', 'importe', 'moneda']] del texto.
    """
    respuesta = ollama.chat(model = "deepseek-r1:14b", messages = [{"role": "system", "content": prompts.regla}, 
                                                                  {"role": "user", "content": prompts.prompt_empleado.format(pais, servicio, texto)}])
    return str(respuesta["message"].content).split("Respuesta : ", 1)[-1]


def evaluar_respuesta(pais, servicio, texto, respuesta):
    """
    Determina si el resultado coincide con valores del texto.
    """
    evaluacion = ollama.chat(model = "deepseek-r1:14b", messages = [{"role": "system", "content": prompts.regla},
                                                                  {"role": "user", "content": prompts.prompt_evaluador.format(pais, servicio, texto, respuesta)}])
    return str(evaluacion["message"].content).split("Respuesta : ", 1)[-1]


def convertir_df(df, respuesta, pais, servicio):
    """
    Convierte la lista de listas '[[ ]]' a un df.
    """
    try:
        data_list = ast.literal_eval(respuesta)
        for lista in data_list:
            lista.append(pais)
            lista.append(servicio)
            lista.append(0)
        df_nuevo = pd.DataFrame(data_list, columns = ["empresa", "fecha", "conceptos", "importe", "moneda", "pais", "servicio", "valor USD"])
        return pd.concat([df, df_nuevo], ignore_index = True)
    
    except:
        return df