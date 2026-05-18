import sys
import math

def parsear_linea(linea):
    partes = linea.split(',')
    
    # Regla estricta: Exactamente 4 columnas. Ni una más, ni una menos.
    if len(partes) != 4:
        return None
        
    producto = partes[1].strip() # Conservar mayúsculas/minúsculas originales
    
    try:
        cantidad = int(partes[2].strip())
        precio = float(partes[3].strip())
        
        # Evitar que los errores intencionales "1e999" (infinito) o "NaN" pasen como números
        if math.isinf(precio) or math.isnan(precio):
            return None
            
        return producto, cantidad, precio
    except ValueError:
        # Si tiene TEXTOS_BASURA como "abc", "$100" o "12..5", fallará y se ignora
        return None

def procesar_ventas(lineas):
    productos = {}
    es_encabezado = True

    for linea in lineas:
        linea = linea.strip()
        if es_encabezado:
            es_encabezado = False
            continue
        if not linea:
            continue

        datos = parsear_linea(linea)
        if not datos:
            continue # Se ignora la línea inválida

        producto, cantidad, precio = datos

        if producto not in productos:
            productos[producto] = {
                "unidades": 0,
                "ingreso": 0.0
            }

        productos[producto]["unidades"] += cantidad
        productos[producto]["ingreso"] += cantidad * precio

    lista_resultados = []
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

    # Ordenar por ingreso (descendente) y luego alfabético para desempatar
    lista_ordenada = sorted(lista_resultados, key=lambda x: (-x["ingreso"], x["producto"]))
    
    return lista_ordenada

def imprimir_reporte(resultados):
    print("producto,unidades_vendidas,ingreso_total,precio_promedio")
    for res in resultados:
        print(f"{res['producto']},{res['unidades']},{res['ingreso']:.2f},{res['promedio']:.2f}")

def main():
    resultados_agrupados = procesar_ventas(sys.stdin)
    imprimir_reporte(resultados_agrupados)

if __name__ == "__main__":
    main()