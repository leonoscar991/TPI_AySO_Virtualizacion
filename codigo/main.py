
# Se importan funciones desde el paquete "paquete_funciones"y modulo "opciones".
from paquete_funciones.opciones import (cargar_herramientas,mostrar_inventario,
                                        consultar_stock,reporte_agotados,alta_producto,actualizar_stock)

# Se muestra el menu principal.
def mostrar_menu():
    print('\n===== CONTROL DE INVENTARIO - FERRETERÍA =====')
    print('1. Cargar herramientas')
    print('2. Mostrar inventario')
    print('3. Consultar stock')
    print('4. Reporte de agotados')
    print('5. Alta de nuevo producto')
    print('6. Actualizar stock (venta / ingreso)')
    print('7. Salir')

def main():
    inventario = []
    opcion = 0
    while opcion !=7:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                cargar_herramientas(inventario)
            elif opcion == 2:
                mostrar_inventario(inventario)
            elif opcion == 3:
                consultar_stock(inventario)
            elif opcion == 4:
                reporte_agotados(inventario)
            elif opcion == 5:
                alta_producto(inventario)
            elif opcion == 6:
                actualizar_stock(inventario)
            elif opcion == 7:
                print('Gracias por usar el sistema. ¡Hasta luego!')
            else:
                raise ValueError('Opción fuera de rango (1 a 7).')
        except ValueError as e:
            print(f'Error: {e}')


main()
