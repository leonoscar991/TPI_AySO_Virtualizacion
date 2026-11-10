# Funciones auxiliares 

def validar_nombre(nombre):
    nombre = nombre.strip()
    if nombre == '':
        raise ValueError('El nombre no puede estar vacío.')
    return nombre


def buscar_herramienta(inventario, nombre):
    for herramienta in inventario:
        if herramienta['herramienta'].lower() == nombre.lower():
            return herramienta
    return None