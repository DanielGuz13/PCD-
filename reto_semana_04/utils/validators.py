def validar_sku(sku):
    """Valida que el SKU no este vacio."""
    if not sku or not str(sku).strip():
        return False
    return True

def validar_precio(precio):
    """Valida que el precio sea un numero >= 0."""
    try:
        precio_num = float(precio)
        return precio_num >= 0
    except (ValueError, TypeError):
        return False

def validar_stock(stock):
    """Valida que el stock sea un entero >= 0."""
    try:
        stock_num = int(stock)
        return stock_num >= 0
    except (ValueError, TypeError):
        return False

def validar_producto(sku, nombre, categoria, precio, stock, stock_minimo):
    """
    Valida todos los campos de un producto.
    
    Returns:
        tuple: (es_valido: bool, mensaje_error: str o None)
    """
    if not validar_sku(sku):
        return False, "SKU vacio o invalido"
    
    if not nombre or not str(nombre).strip():
        return False, "Nombre vacio"
    
    if not validar_precio(precio):
        return False, f"Precio invalido: {precio}"
    
    if not validar_stock(stock):
        return False, f"Stock invalido: {stock}"
    
    if not validar_stock(stock_minimo):
        return False, f"Stock minimo invalido: {stock_minimo}"
    
    return True, None