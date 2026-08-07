
from utilidades import *
from rutas import ruta_veiculos

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

def guardar_veiculos():
    archivo = open(ruta_veiculos, "w")
    for veiculo in veiculos:
        archivo.write(veiculo + "\n")

    archivo.close

def cargar_veiculos():
    try:
        archivo = open(ruta_veiculos, "r")
        for linea in archivo:
            veiculos.append(linea.strip())

        archivo.close

    except FileNotFoundError:
        pass