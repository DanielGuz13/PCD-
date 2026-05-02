° Reto Semana 5: Perfilador de Datasets 📊

    - Descripción del Programa.
    Herramienta automática para inspeccionar la calidad de cualquier archivo CSV[cite: 1]. Recibe un dataset vía línea de comandos y genera un reporte detallando tipos de datos, valores faltantes y proporción de datos únicos por columna[cite: 1].

    - Instrucciones de uso.
    `es_valor_nulo(valor)`: 
    Retorna `True` si la celda es `None`, un string vacío `""` o contiene solo espacios en blanco[cite: 1].

    `inferir_tipo(valores)`: 
    Analiza los datos válidos; si >80% coincide con un formato, retorna "numerico", "fecha" o "booleano" (por defecto retorna "texto")[cite: 1].

    `perfilar_columna(nombre, valores)`: 
    Calcula registros totales, nulos y únicos, generando porcentajes exactos a dos decimales y extrayendo un valor de ejemplo[cite: 1].

    Procesamiento de datos (Bloque `main`): 
    Usa `argparse` para solicitar los argumentos `--input` y `--output`[cite: 1]. Implementa `try/except` para manejar errores de lectura, procesa los datos iterando por columna y exporta el reporte final a un nuevo archivo CSV[cite: 1].

  -Ejemplo de entrada:
    fecha,producto,cantidad,precio,vendedor
    2026-01-01,Laptop,2,15000.00,Ana
    2026-01-02,Mouse,10,250.00,Bob

    -Salida esperada:
    nombre_columna,tipo_inferido,total_registros,valores_nulos,porcentaje_nulos,valores_unicos,porcentaje_unicos,ejemplo_valor
    fecha,fecha,5,0,0.00,5,100.00,2026-01-01
    producto,texto,5,0,0.00,4,80.00,Laptop