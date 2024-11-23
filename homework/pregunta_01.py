"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    
    Rta/
    214

    """
    with open("files/input/data.csv", "r") as archivo: 
        data = archivo.readlines()
    column_2 = [linea.split()[1] for linea in data]
    mapeo = map(lambda x: int(x), column_2)
    #print(sum(mapeo))
    return(sum(mapeo))
    
#pregunta_01()