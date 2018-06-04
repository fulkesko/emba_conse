from datetime import datetime
def ultima_regla():
    print("ingrese la fecha de su ultima regla")
    dia = int(input("dia: "))
    mes = int(input("mes: "))
    año = int(input("año: "))
    fecha1 = datetime.now()
    fecha2 = datetime(año, mes, dia, 0, 0, 0)
    diferencia = fecha1 - fecha2
    diferencia = diferencia / 7
    print("semanas de embarazo:", diferencia.days, "semanas")


datos = {'nombre' : "" }
def registro_datos():
    print("uwu")