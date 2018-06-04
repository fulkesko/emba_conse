from datetime import datetime

def ultima_regla():

    print("ingrese la fecha de su ultima regla")
    dia = int(input("dia: "))
    mes = int(input("mes: "))
    anio = int(input("año: "))
    fecha1 = datetime.now()
    fecha2 = datetime(anio, mes, dia, 0, 0, 0)
    diferencia = fecha1 - fecha2
    semanas = diferencia / 7
    return (semanas.days)




datos = {'nom': "", 'semanas': "", 'pelo_papa': "", 'pelo_mama': "", 'tipo_part': ""}

def ingreso_datos():
    while(True):
        nombre = input("ingrese su nombre: ")
        datos['nom'] = nombre
        t_emba = ultima_regla()
        print (t_emba,"semanas de embarazo")
        datos['semanas'] = t_emba
        pelo_p = input("ingrese color de pelo del papá: ")
        datos['pelo_papa'] = pelo_p
        pelo_m = input("ingrese color de pelo de la mamá: ")
        datos['pelo_mama'] = pelo_m
        t_part = input("¿Que tipo de parto espera tener?: ")
        datos['tipo_part'] = t_part
