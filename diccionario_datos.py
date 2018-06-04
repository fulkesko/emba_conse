from funcion_calculo_semanas import *
def ingreso_datos():
    datos = {'nom': "", 'semanas': "", 'pelo_p': "", 'pelo_m': "", 'tipo_part': ""}

    while(True):
        nombre = input("ingrese su nombre: ")
        datos['nom'] = nombre
        ultima_regla()
        datos['semanas'] = diferencia
        
ingreso_datos()