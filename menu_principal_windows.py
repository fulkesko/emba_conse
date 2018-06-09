from funcion_calculo_semanas import *

def menu_p():
    print("                            ")
    print("bienvenida a el programa registros de datos y consejos")
    print("                            ")
    print("por favor seleccione la opcion que desea")


    while(True):
        print("----------------------------------------")
        print("para registar sus datos escriba: registrar")
        print("si desea ver sus datos escriba: ver")
        print("o para salir escriba: salir")
        print("----------------------------------------")
        opci = input("eliga su opcion: ")

        if(opci.lower().strip() == "registrar"):
            menu_dat()
        elif(opci.lower().strip() == "ver"):
            if (datos['nombre'] == "nada"):
                gifto()
                for x in datos:
                    print(x, ":", datos[x])
        if (opci.lower().strip() == "salir"):
            print("gracias por usar esta app")
            break
        print("ingrese una opcion valida!!")


menu_p()
