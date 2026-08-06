
import menu
import veiculos
from utilidades import *

seguir_mprincipal = True


while seguir_mprincipal:
    smenu_principal = menu.menu_principal()

    if smenu_principal == "1":
        seguir_mveiculos = True

        while seguir_mveiculos:
            smenu_veiculos = menu.menu_veiculos()
            if smenu_veiculos == "1":
                veiculos.añadir_veiculo()

            elif smenu_veiculos == "2":
                seguir_mmostrar_veiculos = True
                while seguir_mmostrar_veiculos:
                    smenu_mostrarveiculos = menu.menu_mostrar_veiculos()
                    if smenu_mostrarveiculos == "1":
                        veiculos.borrar_veiculo()

                    elif smenu_mostrarveiculos == "2":
                        seguir_mmostrar_veiculos = False

                    else:
                        print()
                        print("seleccione una opcion correcta.")
                        pause()
                

            elif smenu_veiculos == "3":
                funcion_nodisponible()

            elif smenu_veiculos == "4":
                funcion_nodisponible()

            elif smenu_veiculos == "0":
                seguir_mveiculos = False

            else:
                print()
                print("seleccione una opcion correcta.")
                pause()




    elif smenu_principal == "2":
        funcion_nodisponible()
        #menu_mantenimientos()

    elif smenu_principal == "3":
        funcion_nodisponible()
        #menu_estadisticas()

    elif smenu_principal == "4":
        funcion_nodisponible()
        #menu_config()

    elif smenu_principal == "0":
        print()
        print("Hasta luego!")
        pause()
        limpiar()
        seguir_mprincipal = False

    else:
        print()
        print("Selecciona una opcion valida")
        pause()
