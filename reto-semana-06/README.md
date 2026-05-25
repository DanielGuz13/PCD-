° Reto Semana 6: Validador de Códigos con Expresiones Regulares 

    - Descripción del Programa.
    Herramienta automática para inspeccionar y validar la integridad de diferentes tipos de códigos de logística mediante expresiones regulares. Recibe un lote de códigos vía entrada estándar (stdin) y genera un reporte en formato CSV a la salida estándar (stdout) indicando el tipo de código y si es válido o inválido.

    - Instrucciones de uso.
    detectar_tipo(codigo): 
    Detecta el tipo de código por su estructura básica usando regex generales y retorna "producto", "envio", "empleado", "factura" o "desconocido".

    validar_producto(codigo): 
    Valida mediante coincidencia exacta que los bloques de categoría y país estén formados estrictamente por letras mayúsculas.

    validar_envio(codigo): 
    Extrae las variables de fecha y valida que los enteros correspondan a los rangos permitidos (año 2020-2030, mes 01-12, día 01-31).

    validar_empleado(codigo): 
    Verifica que el departamento esté en la lista válida (VEN, ADM, TEC, LOG, RHH) y que el identificador numérico no empiece con cero.

    validar_factura(codigo): 
    Inspecciona que el carácter de la serie corresponda a una letra mayúscula de la A a la E.

    validar_codigo(codigo): 
    Enlaza la detección de tipo con la validación estricta y retorna una tupla con el tipo detectado y un booleano de validez.

    Procesamiento de datos (Bloque main): 
    Imprime los encabezados CSV, lee un flujo de datos línea por línea desde `sys.stdin`, ignora líneas vacías e imprime el resultado de la validación directamente a `sys.stdout`.

  -Ejemplo de entrada:
    TEC-0001-MX
    ALI-9999-US
    tec-0001-MX
    ENV-2024-03-15-001234
    ENV-2019-03-15-001234
    EMP-VEN-1234
    EMP-VEN-0123

    -Salida esperada:
    codigo,tipo,valido
    TEC-0001-MX,producto,VALIDO
    ALI-9999-US,producto,VALIDO
    tec-0001-MX,producto,INVALIDO
    ENV-2024-03-15-001234,envio,VALIDO
    ENV-2019-03-15-001234,envio,INVALIDO
    EMP-VEN-1234,empleado,VALIDO
    EMP-VEN-0123,empleado,INVALIDO