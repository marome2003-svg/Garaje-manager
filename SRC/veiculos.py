
from utilidades import *

veiculos = []

def añadir_veiculo():
    print()
    veiculos.append(input("Introduzca el veiculo que desee añadir: "))

def borrar_veiculo():
    print()
    bveiculo = input("escriba el nombre del veiculo que quiera borrar: ")

    if bveiculo in veiculos:
        veiculos.remove(bveiculo)

    else:
        print()
        print("seleccione una opcion correcta (revisa las mayusculas). ")
        pause()
