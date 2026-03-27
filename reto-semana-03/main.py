import sys

def parsear_linea(linea):
    """
    Intenta extraer y validar los datos de una línea del CSV.
    Retorna una tupla (producto, cantidad, precio) o None si es inválida.
    """
    partes = linea.split(',')
    
    #Regla 5: Menos de 4 columnas
    if len(partes) != 4:
        return None
        
    producto = partes[1]
    
    #Regla 5: Cantidad o precio no numéricos
    try:
        cantidad = int(partes[2])
        precio = float(partes[3])
        return producto, cantidad, precio
    except ValueError:
        return None

def procesar_ventas(lineas):
    """
    Recibe un iterable de líneas, agrupa por producto y calcula las métricas.
    Retorna una lista de diccionarios ordenada por ingreso total descendente.
    """
    productos = {}
    es_encabezado = True

    for linea in lineas:
        linea = linea.strip()
        
        #Ignorar la primera línea (encabezados) y líneas vacías
        if es_encabezado:
            es_encabezado = False
            continue
        if not linea:
            continue

        datos = parsear_linea(linea)
        if not datos:
            continue  #Ignorar línea si parsear_linea devolvió None

        producto, cantidad, precio = datos

        #Regla 1: Agrupar por producto
        if producto not in productos:
            productos[producto] = {
                "unidades": 0,
                "ingreso": 0.0
            }

        #Regla 2: Calcular métricas base
        productos[producto]["unidades"] += cantidad
        productos[producto]["ingreso"] += cantidad * precio

    lista_resultados = []
    
    #Regla 2: Calcular precio promedio
    for prod, totales in productos.items():
        unidades = totales["unidades"]
        ingreso = totales["ingreso"]
        promedio = ingreso / unidades if unidades > 0 else 0
        
        lista_resultados.append({
            "producto": prod,
            "unidades": unidades,
            "ingreso": ingreso,
            "promedio": promedio
        })

    #Regla 3: Ordenar por ingreso total (Descendente)
    lista_ordenada = sorted(lista_resultados, key=lambda x: x["ingreso"], reverse=True)
    
    return lista_ordenada

def imprimir_reporte(resultados):
    """
    Imprime el reporte en formato CSV a stdout aplicando las reglas de formato.
    """
    print("producto,unidades_vendidas,ingreso_total,precio_promedio")
    
    #Regla 4: Formato de números (enteros para unidades, 2 decimales para dinero)
    for res in resultados:
        print(f"{res['producto']},{res['unidades']},{res['ingreso']:.2f},{res['promedio']:.2f}")

def main():
    #sys.stdin actúa como un iterable de las líneas de entrada
    resultados_agrupados = procesar_ventas(sys.stdin)
    imprimir_reporte(resultados_agrupados)

if __name__ == "__main__":
    main()