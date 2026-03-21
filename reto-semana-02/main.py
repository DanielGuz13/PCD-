import sys

def fahrenheit_a_celsius(f):
    """Convierte temperatura de Fahrenheit a Celsius."""
    return (f - 32) * 5 / 9

def clasificar_temperatura(celsius):
    """Clasifica la temperatura en Celsius según los rangos establecidos."""
    if celsius < 0:
        return "Congelante"
    elif celsius <= 15:
        return "Frio"
    elif celsius <= 25:
        return "Templado"
    elif celsius <= 35:
        return "Calido"
    else:
        return "Extremo"

def main():
    # 1. Imprimir estrictamente el encabezado de salida solicitado
    print("ciudad,temperatura_celsius,clasificacion")
    
    primera_linea = True
    
    # 2. Leer línea por línea desde la entrada estándar (stdin)
    for linea in sys.stdin:
        # Limpiar saltos de línea y espacios al inicio/final
        linea = linea.strip()
        
        # Saltar la primera línea (encabezado de entrada)
        if primera_linea:
            primera_linea = False
            continue
        
        # Ignorar líneas completamente vacías
        if not linea:
            continue
            
        # 3. Separar los datos por comas
        partes = linea.split(',')
        
        # Ignorar si no hay exactamente 3 columnas
        if len(partes) != 3:
            continue
            
        # Extraer y limpiar cada parte (strip ayuda con los casos de espacios extra)
        ciudad = partes[0].strip()
        temp_str = partes[1].strip()
        unidad = partes[2].strip().upper()  # Convertir a mayúsculas por si ingresan 'c' o 'f'
        
        # 4. Validar que la unidad sea correcta
        if unidad not in ['C', 'F']:
            continue
            
        # 5. Validar que la temperatura sea un número válido
        try:
            temperatura = float(temp_str)
        except ValueError:
            continue  # Ignorar silenciosamente si no es número
            
        # 6. Realizar la conversión a Celsius si es necesario
        if unidad == 'F':
            celsius = fahrenheit_a_celsius(temperatura)
        else:
            celsius = temperatura
            
        # 7. Obtener la clasificación
        clasificacion = clasificar_temperatura(celsius)
        
        # 8. Imprimir resultado con exactamente 1 decimal para la temperatura
        print(f"{ciudad},{celsius:.1f},{clasificacion}")

if __name__ == "__main__":
    main()