"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    with open("files/input/data.csv", "r") as archivo: 
        data = archivo.readlines()
    column_3 = [linea.split()[2] for linea in data]
    #print(column_3)

    contadores = {}
    meses = [f"0{i}" if i<10 else f"{i}" for i in range(1,13)]
    #print(meses)

    for mes in meses:
        contadores[mes] = 0
    
    #print(contadores)

    for fecha in column_3:
        mes = fecha.split("-")[1]
        contadores[mes] += 1

    return [(clave, contadores[clave]) for clave in contadores]
    #print(contadores)
pregunta_04()