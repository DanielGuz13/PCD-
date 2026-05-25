import sys
import re

DEPARTAMENTOS_VALIDOS = ['VEN', 'ADM', 'TEC', 'LOG', 'RHH']
SERIES_VALIDAS = ['A', 'B', 'C', 'D', 'E']


def detectar_tipo(codigo: str) -> str:
    """Detecta el tipo de codigo por su estructura usando regex basicos."""
    if re.match(r'^[A-Za-z]{3}-\d{4}-[A-Za-z]{2}$', codigo):
        return "producto"
    elif re.match(r'^ENV-\d{4}-\d{2}-\d{2}-\d{6}$', codigo):
        return "envio"
    elif re.match(r'^EMP-[A-Za-z]{3}-\d{4}$', codigo):
        return "empleado"
    elif re.match(r'^FAC-[A-Za-z]-\d{6}$', codigo):
        return "factura"
    else:
        return "desconocido"


def validar_producto(codigo: str) -> bool:
    """Valida que categoria y pais sean estrictamente mayusculas."""
    return bool(re.match(r'^[A-Z]{3}-\d{4}-[A-Z]{2}$', codigo))


def validar_envio(codigo: str) -> bool:
    """Valida rangos de fecha (año 2020-2030, mes 01-12, dia 01-31)."""
    m = re.match(r'^ENV-(\d{4})-(\d{2})-(\d{2})-(\d{6})$', codigo)
    if m:
        anio = int(m.group(1))
        mes = int(m.group(2))
        dia = int(m.group(3))
        
        # Validacion estricta de rangos segun las especificaciones
        if (2020 <= anio <= 2030) and (1 <= mes <= 12) and (1 <= dia <= 31):
            return True
    return False


def validar_empleado(codigo: str) -> bool:
    """Valida departamento valido y que el numero no empiece con 0."""
    # Usamos un regex estricto que exige [1-9] en el primer digito
    m = re.match(r'^EMP-([A-Z]{3})-([1-9]\d{3})$', codigo)
    if m and m.group(1) in DEPARTAMENTOS_VALIDOS:
        return True
    return False


def validar_factura(codigo: str) -> bool:
    """Valida serie A-E en mayuscula."""
    return bool(re.match(r'^FAC-([A-E])-\d{6}$', codigo))


def validar_codigo(codigo: str):
    """Detecta tipo y valida. Retorna la tupla (tipo, es_valido)."""
    tipo = detectar_tipo(codigo)
    
    if tipo == "producto":
        es_valido = validar_producto(codigo)
    elif tipo == "envio":
        es_valido = validar_envio(codigo)
    elif tipo == "empleado":
        es_valido = validar_empleado(codigo)
    elif tipo == "factura":
        es_valido = validar_factura(codigo)
    else:
        # Los desconocidos siempre son invalidos
        es_valido = False
        
    return tipo, es_valido


def main():
    # 1. Imprime los encabezados requeridos para la salida CSV
    print("codigo,tipo,valido")
    
    # 2. Itera sobre cada linea inyectada desde stdin
    for linea in sys.stdin:
        codigo = linea.strip()
        
        # Las lineas vacias o con solo espacios deben ignorarse
        if not codigo:
            continue
            
        # 3. Validamos e imprimimos el resultado en formato CSV estricto
        tipo, es_valido = validar_codigo(codigo)
        estado = "VALIDO" if es_valido else "INVALIDO"
        print(f"{codigo},{tipo},{estado}")


if __name__ == "__main__":
    main()