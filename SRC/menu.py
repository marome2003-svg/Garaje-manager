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

        if veiculos.veiculos:
            print(" - VEHICULOS REGISTRADOS - ")
            print("----------------------------")
            print()
            contador = 0
            for items in veiculos.veiculos:
                print(str(contador) + ". " + items["marca"] + " " + items["modelo"])
                contador = contador + 1
            print()

        print("1 - Añadir veículo")
        print("2 - Ver informacion de vehículos")
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
            veiculos.borrar_veiculo()

        elif opcion == "0":
            break

        else:
            print()
            print("Selecciona una opcion valida")
            pause()

    

def menu_mostrar_veiculos():
    print()
    while True:
        try:
            opcion = int(input("Elige un veiculo (0, 1, 2...) "))
            if opcion < len(veiculos.veiculos) and opcion >= 0:
                break

            else:
                print()
                print("No exixte ningun vehiculo con esa numeracion")

        except:
            print()
            print("Introduce una opccion correcta: ")
        

    while True:
        limpiar()
        print()
        print("=========================================================")
        print("             " + veiculos.veiculos[opcion]["marca"] + " " + veiculos.veiculos[opcion]["modelo"])
        print("=========================================================")
        print()
        for clave, valor in veiculos.veiculos[opcion].items():
            print(clave + ": ", valor)

        print()
        print("1 - Modificar datos")
        print("0 - volver")
        print()
        try:
            opcion2 = input("selecciona un opccion (1, 0): ")

            if opcion2 == "1":
                print()
                while True:
                    opcion3 = input("introduce el dato que deseas modificar (marcar, modelo...): ")
                    if opcion3 != "marca" and opcion3 != "modelo" and opcion3 != "km":
                        print()
                        print("Introduce un tipo de dato valido")

                    else:
                        break

                print()
                modificar = input("Introduce el nuevo valor: ")
                if opcion3 == "km":
                    modificar = int(modificar)

                veiculos.veiculos[opcion][opcion3] = modificar

            elif opcion2 == "0":
                break

            else:
                print()
                print("selecciona una opcion valida")
                pause()

        except:
            print()
            print("Introduce una opccion valida")


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
            