from utilidades import *

def menu_principal():
    limpiar()
    print()
    print("=========================================================")
    print("                     Garage Manager                      ")
    print("=========================================================")
    print()
    print("1 - Gestión de veículos")
    print("2 - Gestión de mantenimientos")
    print("3 - Estadísticas")
    print("4 - Configuración")
    print()
    print("0 - Salir")
    print()
    smenu_principal = input("seleccione una opccion (1, 2, 3, 4, 0): ")
    return smenu_principal


def menu_veiculos():
    limpiar()
    print()
    print("=========================================================")
    print("                   Gestión de veículos                   ")
    print("=========================================================")
    print()
    print("1 - Añadir veículo")
    print("2 - Ver veículos")
    print("3 - Buscar veículo")
    print("4 - Eliminar veículo")
    print()
    print("0 - volver")
    print()
    smenu_veiculos = input("seleccione una opccion (1, 2, 3, 4, 0): ")
    return smenu_veiculos

def menu_mostrar_veiculos():
    print()
    