° Reto Semana 2: Clasificador de Temperaturas 🌡️

    - Descripción del Programa.
    Este programa es una herramienta de procesamiento de datos diseñada para estandarizar reportes de clima de agencias de viajes.
    Recibe un flujo de datos en formato CSV que contiene temperaturas de distintas ciudades (mezclando grados Celsius y Fahrenheit) y genera un reporte limpio y unificado.

    - Instrucciones de uso.
    fahrenheit_a_celsius(f): 
    Es una función matemática simple que recibe un valor numérico en grados Fahrenheit. Aplica la fórmula estándar `(F - 32) * 5 / 9` y retorna su equivalente exacto en grados Celsius.

    clasificar_temperatura(celsius): 
    Esta función actúa como el "cerebro" lógico del clima. Recibe una temperatura ya convertida a Celsius y la evalúa a través de una estructura de condiciones (`if/elif`). Dependiendo del rango exacto en el que caiga el número, retorna una etiqueta de texto descriptiva (ej. "Congelante" para `< 0`, "Templado" para `<= 25`, etc.).

    Procesamiento de datos (Bloque `main`): 
    Es el motor del programa. En lugar de cargar todo el archivo en la memoria de golpe, lee los datos línea por línea a través de la entrada estándar (`sys.stdin`). 
    Utiliza los métodos `.strip()` y `.split(',')` para limpiar espacios en blanco y separar la ciudad, la temperatura y la unidad.
    Implementa un bloque `try/except` para intentar convertir el texto de la temperatura a un número decimal (`float`). Si la línea contiene letras o datos corruptos en esa columna, captura el error de valor (`ValueError`) e ignora esa fila silenciosamente usando `continue`, evitando que el programa colapse.

  -Ejemplo de entrada:
    ciudad,temperatura,unidad
    CDMX,22,C
    Nueva York,50,F
    Moscu,-10,C
    Miami,95,F
    Cancun,30,C
    Chicago,14,F
    Phoenix,104,F
    Error,abc,C
    Lima,25,C
    Bangkok,36,C

    -Salida esperada:
    ciudad,temperatura_celsius,clasificacion
    CDMX,22.0,Templado
    Nueva York,10.0,Frio
    Moscu,-10.0,Congelante
    Miami,35.0,Calido
    Cancun,30.0,Calido
    Chicago,-10.0,Congelante
    Phoenix,40.0,Extremo
    Lima,25.0,Templado
    Bangkok,36.0,Extremo
