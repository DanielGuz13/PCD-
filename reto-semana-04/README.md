
° Reto Semana 4: Sistema de Inventario Modular 📦

    - Descripción del Programa.
    Este programa es una herramienta de procesamiento modular diseñada para gestionar el inventario de una cadena de tiendas de tecnología. 
    Recibe un archivo en formato CSV que contiene el estado actual de los productos, valida la información, y genera un reporte limpio y unificado exclusivamente con aquellos artículos que necesitan reorden (stock bajo).

    - Instrucciones de uso.
    Clase Producto (models/producto.py): 
    Es la plantilla que representa cada artículo. Recibe los datos validados y utiliza métodos internos para determinar matemáticamente si el artículo necesita reorden (`stock < stock_minimo`), calcular exactamente cuántas unidades faltan y obtener el valor monetario del inventario actual.

    Validadores (utils/validators.py): 
    Actúan como el control de calidad de los datos. Son funciones lógicas que evalúan que el SKU no esté vacío y que tanto los precios como las cantidades de stock sean valores numéricos reales mayores o iguales a cero (`float` o `int`).

    Entrada y Salida (utils/io.py): 
    Funciones dedicadas exclusivamente a la interacción con archivos. `leer_inventario` lee el archivo CSV separando las columnas correctamente y devolviendo listas de diccionarios. `escribir_reporte` toma los productos procesados y los guarda estructurados en un nuevo CSV.

    Procesamiento de datos (Bloque `main`): 
    Es el orquestador del programa. Lee los datos crudos e implementa la validación para capturar errores de tipo (como letras en vez de números en los precios o columnas faltantes/sobrantes). Si una fila tiene datos corruptos, la ignora silenciosamente. Luego instancia los objetos, filtra únicamente los que necesitan reorden, los ordena de forma descendente por la urgencia de unidades faltantes y manda a escribir el archivo final en la carpeta de salidas.

    -Ejemplo de entrada:
    sku,nombre,categoria,precio,stock,stock_minimo
    SKU001,Laptop HP,Electronica,15000.00,5,10
    SKU002,Mouse Logitech,Accesorios,350.00,3,15
    SKU003,Teclado Mecanico,Accesorios,N/A,20,10
    SKU004,Monitor LG,Electronica,6000.00,abc,5
    SKU005,Audifonos Sony,Accesorios,1200.00,2,???
    SKU006,Webcam HD,Accesorios
    SKU007,SSD 1TB,Almacenamiento,1800.00,0,5,dato_extra,otro

    -Salida esperada:
    sku,nombre,categoria,stock_actual,stock_minimo,unidades_faltantes,valor_inventario
    SKU002,Mouse Logitech,Accesorios,3,15,12,1050.00
    SKU001,Laptop HP,Electronica,5,10,5,75000.00

Guzman Meza Jose Daniel, 3AM1