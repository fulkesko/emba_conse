from datetime import datetime
import os

def gifto():
    travo = os.system('travolta.gif')
    print(travo)

def ultima_regla():
    fecha1 = datetime.now()
    formato_fecha = "%d/%m/%Y"
    print("ingrese la fecha de su ultima regla")
    fecha2 = datetime.strptime(input("ingrese fecha (dia/mes/año): "), formato_fecha)
    while (fecha2 > fecha1):
        fecha2 = datetime.strptime(input("ingrese una fecha valida (dia/mes/año): "), formato_fecha)
    diferencia = fecha1 - fecha2
    semanas = diferencia / 7
    return (semanas.days)



datos = {'nombre': "nada", 'semanas': "nada", 'tipo_parto': "nada"}

def ingreso_datos():
    while(True):
        nombre = input("ingrese su nombre: ")
        datos['nombre'] = nombre.strip()
        t_emba = ultima_regla()
        datos['semanas'] = t_emba
        t_part = input("¿Que tipo de parto espera tener?(c/n): ").strip()

        datos['tipo_parto'] = t_part
        if (t_part == "cesarea" or t_part.__contains__("c")):
            print("toma estos consejos te pueden ayudar: "," cesarea",
                  "https://www.bebesymas.com/salud-de-la-madre/parto-por-cesarea-siete-consejos-que-te-ayudaran-a-recuperarte-mas-facilmente")
        elif (t_part == "normal" or t_part.__contains__("n")):
            print("estos consejos pueden ser de utilidad: ","parto normal" ,"https://elpais.com/elpais/2016/11/16/media/1479322247_869545.html")
        break

def menu_dat():
    while(True):
        print("----------------------------------------")
        print("ingrese sus datos")
        print("----------------------------------------")
        ingreso_datos()
        eleccion = input("desea modificar sus datos? (si/no): ")
        if (eleccion.lower() == "si" or eleccion.lower().strip().__contains__("s") or eleccion.lower().strip().__contains__("yes")):
            menu_dat()
        else:
            break
