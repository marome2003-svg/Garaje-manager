
from utilidades import *

veiculos = []

def añadir_veiculo():
    print()
    veiculos.append(input("Introduzca el veiculo que desee añadir: "))

def borrar_veiculo():
    print()
    bveiculo = input("escriba el nombre del veiculo que quiera borrar: ")
    veiculos.remove(bveiculo)