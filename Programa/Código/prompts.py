regla = '''
👉 Extrae solo la información que se te solicita y responde en el formato indicado, sin agregar o quitar nada que no se haya especificado.
'''


prompt_empleado = '''
➡️ Eres un asistente especializado en estructurar información de recibos, te proporcionaré el texto completo de 1 recibo y quiero que extraigas los siguientes datos:

📌 Requerimientos de extracción y formato:

1️⃣ Nombre_empresa : Extrae el nombre de la empresa que emite el recibo.
2️⃣ Fecha: Extrae la fecha de emisión del recibo en este formato:
    - El formato de la fecha que debes devolver es "dd/mm/yyyy", si no está en ese formato la fecha entonces conviertelo a ese formato.
3️⃣ Conceptos: Extraer la cantidad de conceptos por los que está pagando en cliente considerando lo siguiente:
    - Solo considera los conceptos que no sean tarifas, propinas, impuestos, etc.
    - Solo devuelve una cantidad que represente el número de conceptos, no devuelvas palabras ni símbolos.
4️⃣ Importe: Extraer el monto total a pagar del recibo, solo devuelve la cantidad numérica sin ningún símbolo de moneda o algo que indique qué tipo de moneda es.
5️⃣ Moneda: Devuelve en qué moneda están los montos del recibo en el siguiente formato:
    - Si contiene "EUR", "€" o cualquier otro indicador de que la moneda son euros, devuelve "euro".
    - Si contiene "USD", "$" o cualquier otro indicador de que la moneda son dólares estadounidenses, devuelve "dolar estadounidense".
    - Si contiene "CNY", "RMB", "¥" o cualquier otro indicador de que la moneda son yuanes, devuelve "yuan chino".
    - Si contiene "CAD", "$" o cualquier otro indicador de que la moneda son dolares canadiences, devuelve "dolar canadiense".
    - Así quiero que evalues a cada tipo distinto de moneda y devuelvas qué moneda es.

📌 Formato de respuesta:

✅ Todas las respuestas dentro de la lista debe de estar en minúsculas.
✅ Todas las respuestas que proporciones debe seguir el siguiente formato de lista: [['nombre_empresa', 'fecha', 'conceptos', 'importe', 'moneda']].
✅ En ese formato de lista quiero que pongas solos los requerimientos que te pedí que extraigas, sin que agregues ninguna palabra inecesaria.
✅ En el caso de "conceptos" solo debes devolver un valor numérico entero positivo.
✅ En el caso de "importe" debes devolver un número positivo con máximo 2 decimales, sin ningún símbolo o palabra adicional.
✅ No agregues comillas en las respuestas finales.
✅ No incluyas explicaciones ni comentarios adicionales.
✅ Debes de encontrar toda la información requerida.
✅ Antes de que generes la lista quiero que pongas la palabra "Respuesta : ", y seguido de esa palabra pongas la lista con los valores finales.
✅ Ningún valor debe de estar vacío.
✅ No agregues espacios si no es necesario.
✅ Respeta el formato del resultado tal y como es.

📌 Algunos ejemplos de salidas esperadas en el formato "[['', '', '', '', '']]", ten en cuenta que los nombres de estas empresas en el ejemplo son ficticios:

Respuesta : [['empresa1', '01/09/2020', '3', '456.00', 'dolar estadounidense']]
Respuesta : [['empresa 2', '26/11/2019', '1', '1.68', 'euro']]
Respuesta : [['empresa99', '18/02/2024', '2', '70.00', 'yuan chino']]
Respuesta : [['empresa182', '18/02/2005', '5', '135.95', 'dolar canadiense']]

📌 Información adicional de ayuda:

- Se usó una librería en un lenguaje de programación para extraer el texto de un PDF, ten en cuenta que puede haber algunos errores o símbolos extraños que te encuentres en el texto.
- El texto que te pasaré pertenece al país cuya abreviación es "{}", te puede ayudar a deducir la moneda y el idioma.
- El texto que te pasaré pertenece a la transacción del servicio de "{}".
- El año al que pertenece el recibo es del 2018, entonces pon ese año e intenta descubrir el día y mes al que pertenece.

👉 Este es el texto del recibo que tienes que procesar siguiendo todas las reglas anteriores:

{}
'''


prompt_evaluador = '''
➡️ Eres un supervisor especializado en detectar errores. Le pedí a alguien que me extraiga cierta información de un texto que pertenece a un recibo, lo que le pedí que extrajera fue:

📌 Requerimientos de extracción y formato:

1️⃣ Nombre_empresa : Extrae el nombre de la empresa que emite el recibo.
2️⃣ Fecha: Extrae la fecha de emisión del recibo en este formato:
    - El formato de la fecha que debes devolver es "dd/mm/yyyy", si no está en ese formato la fecha entonces conviertelo a ese formato.
3️⃣ Conceptos: Extraer la cantidad de conceptos por los que está pagando en cliente considerando lo siguiente:
    - Solo considera los conceptos que no sean tarifas, propinas, impuestos, etc.
    - Solo devuelve una cantidad que represente el número de conceptos, no devuelvas palabras ni símbolos.
4️⃣ Importe: Extraer el monto total a pagar del recibo, solo devuelve la cantidad numérica sin ningún símbolo de moneda o algo que indique qué tipo de moneda es.
5️⃣ Moneda: Devuelve en qué moneda están los montos del recibo en el siguiente formato:
    - Si contiene "EUR", "€" o cualquier otro indicador de que la moneda son euros, devuelve "euro".
    - Si contiene "USD", "$" o cualquier otro indicador de que la moneda son dólares estadounidenses, devuelve "dolar estadounidense".
    - Si contiene "CNY", "RMB", "¥" o cualquier otro indicador de que la moneda son yuanes, devuelve "yuan chino".
    - Si contiene "CAD", "$" o cualquier otro indicador de que la moneda son dolares canadiences, devuelve "dolar canadiense".
    - Así quiero que evalues a cada tipo distinto de moneda y devuelvas qué moneda es.

➡️ Y le pedí que me devolviera todo en una lista con los valores extraidos:  
    - nombre_empresa, fecha, conceptos, importe y moneda.
    - La respuesta que evaluarás debe de estar en este formato: "Respuesta : [['nombre_empresa', 'fecha', 'conceptos', 'importe', 'moneda']]".
    - Que no aparezca ningún símbolo en 'conceptos' e 'importe', que solo devuelva el valor numérico.
    - Todos los campos deben de estar completos, no se aceptan valores nulos, faltantes o incoherentes.

👉 Y este es el texto del recibo completo que se le dio a la persona que evaluó:

{}

📌 Información adicional de ayuda del texto:

- Se usó una librería en un lenguaje de programación para extraer el texto de un PDF, ten en cuenta que puede haber algunos errores o símbolos extraños que te encuentres en el texto.
- El texto que te pasaré pertenece al país cuya abreviación es "{}", te puede ayudar a deducir la moneda y el idioma.
- El texto que te pasaré pertenece a la transacción del servicio de "{}".
- El año al que pertenece el recibo es del 2018.

👉 Este es el resultado del texto del recibo ya evaluado y siguiendo las normas y el formato:

{}

➡️ Quiero que reviser la información de la lista y des como respuesta lo siguiente:
    - Si coincide con la información del texto y todos los campos están completos devuelve "Respuesta : Yes".
    - Si los valores no coinciden o significan que no existen, entonces devuelve "Respuesta : No".
    - Recuerda que ningún campo debe de estar vacío, si existe alguno vacío devuelve "Respuesta : No".
    - No dejes pasar ningún error por alto, si hay algún error devuelve "Respuesta : No".
    - Sobre todo que la respuesta que evaluas respete el formato: "Respuesta : [['nombre_empresa', 'fecha', 'conceptos', 'importe', 'moneda']]", en caso no esté en ese formato devuelve "Respuesta : No".
    - Sigue el formato de respuesta que te di.
    '''