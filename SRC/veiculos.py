
from utilidades import *
from rutas import ruta_veiculos

veiculos = []

def añadir_veiculo():
    limpiar()
    print()
    print(" REGISTRO DE VEHICULO")
    print("======================")
    print()
    marca = input("Introduce la marca del vehiculo: ")
    print()
    modelo = input("Introduce el modelo del vehiculo: ")
    print()
    km = int(input("Introduce los KM del vehiculo: "))
    nuevo_vehiculo = {
        "marca": marca ,
        "modelo": modelo ,
        "km": km
    }
    veiculos.append(nuevo_vehiculo)

def borrar_veiculo():
    while True:
        try:
            print()
            bveiculo = int(input("Introduce el vehiculo que deseas borrar (0, 1, 2...) "))
            if bveiculo >= 0 and bveiculo < len(veiculos):
                veiculos.pop(bveiculo)
                break

            else:
                print()
                print("No existe ningun veiculo con esa numeracion")

            

        except:
            print()
            print("Introduce una opcion valida")

def guardar_veiculos():
    archivo = open(ruta_veiculos, "w")
    for veiculo in veiculos:
        archivo.write(
            veiculo["marca"] + "|" +
            veiculo["modelo"] + "|" +
            str(veiculo["km"]) + "\n"
        )

    archivo.close()

def cargar_veiculos():
    try:
        archivo = open(ruta_veiculos, "r")
        for linea in archivo:
            datos = linea.strip().split("|")
            nuevo_veiculo = {
                "marca": datos[0], 
                "modelo": datos[1],
                "km": int(datos[2])
            }
            veiculos.append(nuevo_veiculo)

        archivo.close()

    except FileNotFoundError:
        pass

