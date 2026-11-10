# Funciones del Inventario


from paquete_funciones.auxiliares import validar_nombre, buscar_herramienta



def cargar_herramientas(inventario):
    cantidad_a_cargar = 0
    while cantidad_a_cargar <= 0:
        try:
            cantidad_a_cargar = int(input('¿Cuántas herramientas desea cargar?: '))
            if cantidad_a_cargar <= 0:
                raise ValueError('La cantidad debe ser mayor que 0.')
        except ValueError as e:
            print(f'Error: {e}')

    for i in range(cantidad_a_cargar):
        print(f'\nHerramienta {i + 1} de {cantidad_a_cargar}')
        nombre = ''
        while nombre == '':
            try:
                nombre = validar_nombre(input('Nombre: '))
                if buscar_herramienta(inventario, nombre) != None:
                    nombre = ''
                    raise ValueError('Esa herramienta ya existe en el inventario.')
            except ValueError as e:
                print(f'Error: {e}')

        stock = -1
        while stock < 0:
            try:
                stock = int(input('Stock inicial: '))
                if stock < 0:
                    raise ValueError('El stock no puede ser negativo.')
            except ValueError as e:
                print(f'Error: {e}')
        inventario.append({'herramienta': nombre, 'cantidad': stock})
        print(f'"{nombre}" cargada con {stock} unidades.')
                

def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print('Todavía no hay herramientas cargadas.')
    else:
        print('\n--- INVENTARIO ---')
        for herramienta in inventario:
            print(f"{herramienta['herramienta']}: {herramienta['cantidad']} unidades")

def consultar_stock(inventario):
    if len(inventario) == 0:
        print('Todavía no hay herramientas cargadas.')
    else:
        nombre = validar_nombre(input('Nombre de la herramienta a consultar: '))
        herramienta = buscar_herramienta(inventario, nombre)
        if herramienta == None:
            print(f'"{nombre}" no está en el inventario.')
        else:
            print(f"Stock de {herramienta['herramienta']}: {herramienta['cantidad']} unidades")

def reporte_agotados(inventario):
    if len(inventario) == 0:
        print('Todavía no hay herramientas cargadas.')
    else:
        agotados = 0
        print('\n--- HERRAMIENTAS AGOTADAS ---')
        for herramienta in inventario:
            if herramienta['cantidad'] == 0:
                print(f"- {herramienta['herramienta']}")
                agotados += 1
        if agotados == 0:
            print('No hay herramientas agotadas.')

def alta_producto(inventario):
    nombre = validar_nombre(input('Nombre del nuevo producto: '))
    if buscar_herramienta(inventario, nombre) != None:
        raise ValueError('Esa herramienta ya existe en el inventario.')
    stock = int(input('Stock inicial: '))
    if stock < 0:
        raise ValueError('El stock no puede ser negativo.')
    inventario.append({'herramienta': nombre, 'cantidad': stock})
    print(f'"{nombre}" agregada con {stock} unidades.')


def actualizar_stock(inventario):
    if len(inventario) == 0:
        print('Todavía no hay herramientas cargadas.')
        return
    nombre = validar_nombre(input('Nombre de la herramienta: '))
    herramienta = buscar_herramienta(inventario, nombre)
    if herramienta == None:
        print(f'"{nombre}" no está en el inventario.')
        return
    tipo = input('Tipo de movimiento (1 = venta, 2 = ingreso): ').strip()
    if tipo != '1' and tipo != '2':
        print('Tipo de movimiento inválido. Debe ser 1 o 2.')
        return

    unidades = int(input('Unidades: '))
    if unidades <= 0:
        raise ValueError('Las unidades deben ser mayores que 0.')
    if tipo == '1':
        if unidades > herramienta['cantidad']:
            raise ValueError(f"Stock insuficiente: hay {herramienta['cantidad']} unidades.")
        herramienta['cantidad'] -= unidades
        print(f"Venta registrada. Nuevo stock de {herramienta['herramienta']}: {herramienta['cantidad']}")
    else:
        herramienta['cantidad'] += unidades
        print(f"Ingreso registrado. Nuevo stock de {herramienta['herramienta']}: {herramienta['cantidad']}")