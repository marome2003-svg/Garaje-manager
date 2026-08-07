from utilidades import *
import veiculos
import os 

def menu_principal():

    while True:
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
        opcion = input("seleccione una opccion (1, 2, 3, 4, 0): ")

        if opcion == "1":
            menu_veiculos()                     

        
        elif opcion == "2":
            funcion_nodisponible()
            #menu_mantenimientos()

        elif opcion == "3":
            funcion_nodisponible()
            #menu_estadisticas()

        elif opcion == "4":
            #funcion_nodisponible()
            menu_config()

        elif opcion == "0":
            print()
            print("Hasta luego!")
            pause()
            limpiar()
            break

        else:
            print()
            print("Selecciona una opcion valida")
            pause()


def menu_veiculos():
    while True:
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
        opcion = input("seleccione una opccion (1, 2, 3, 4, 0): ")

        if opcion == "1":
            veiculos.añadir_veiculo()

        elif opcion == "2":
            menu_mostrar_veiculos()
                

        elif opcion == "3":
            funcion_nodisponible()

        elif opcion == "4":
            funcion_nodisponible()

        elif opcion == "0":
            break

        else:
            print()
            print("Selecciona una opcion valida")
            pause()

    

def menu_mostrar_veiculos():

    while True:
        contador_veiculos = 1
        limpiar()
        print()
        for imprimir_veiculo in veiculos.veiculos:
            print(str(contador_veiculos) + "-" + imprimir_veiculo)
            contador_veiculos = contador_veiculos + 1
        print()
        print("1. eliminar veiculo")
        print("0. volver")
        print()
        opcion = input("seleccione una opcion (1, 2): ")

        if opcion == "1":
            veiculos.borrar_veiculo()

        elif opcion == "0":
            break

        else:
            print()
            print("seleccione una opcion correcta.")
            pause()

def menu_config():
    while True:
        limpiar()
        print()
        print("=========================================================")
        print("                      Configuracion                      ")
        print("=========================================================")
        print()
        print()
        print("1 - Resetear memoria")
        print("0 - volver")
        print()
        opcion = input("Seleccione una opcion (1, 0): ")

        if opcion == "1":
            from rutas import ruta_veiculos
            try:
                os.remove(ruta_veiculos)

            except FileNotFoundError:
                pass

            veiculos.veiculos.clear()
            break

        elif opcion == "0":
            break

        else:
            print()
            print("seleccione una opcion correcta.")
            pause()
            