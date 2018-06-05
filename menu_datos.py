from funcion_calculo_semanas import *

def menu_dat():
    while(True):
        print("----------------------------")
        print("ingrese sus datos")
        print("----------------------------")
        ingreso_datos()
        eleccion = input("desea modificar sus datos? (si/no)")
        if (eleccion.lower() == "si"):
            menu_dat()
        else:
            break
