import sys

def limpiar_valor(valor):
    """
    Limpia un valor individual:
    - Quita espacios
    - Elimina caracteres no validos
    - Retorna el numero limpio como string
    """
    #Este es para los espacios
    valores_limpios = valor.strip()

    #Solo dara los valores validos y luego reotrna en string
    caracteres_validos = '0123456789.-'
    resultado = ''
    for char in valores_limpios:
        if char in caracteres_validos:
            resultado += char
    return resultado


def procesar_linea(linea):
    """
    Procesa una linea completa:
    - Separa por comas
    - Limpia cada valor
    - Trunca a entero
    - Suma todos
    - Retorna el resultado
    """
    
    #Separa los valores por comas y suma total de los valores
    valores = linea.split(',')
    valores_limpios = [limpiar_valor(v) for v in valores]
    return sum(convertir_a_entero(v) for v in valores_limpios)

    #Truncado de los mismos valores
def convertir_a_entero(texto):
    """Convierte texto a entero, truncando decimales."""
    if not texto:  # Si esta vacio
        return 0
    try:
        numero = float(texto)  # Primero a float
        return int(numero)     # Luego truncar a int
    except ValueError:
        return 0  # Si no se puede convertir, es 0

def main():
    """
    Lee de stdin linea por linea
    Procesa cada linea
    Imprime el resultado
    """
    for linea in sys.stdin:
        resultado = procesar_linea(linea)
        print(resultado)

if __name__ == "__main__":
    main()