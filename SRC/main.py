
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

            elif smenu_veiculos == "2":
                

            elif smenu_veiculos == "0":
                seguir_mveiculos = False

            else:




    elif smenu_principal == "2":
        menu_mantenimientos()

    elif smenu_principal == "3":
        menu_estadisticas()

    elif smenu_principal == "4":
        menu_config()

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
