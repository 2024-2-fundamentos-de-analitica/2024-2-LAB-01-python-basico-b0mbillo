"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    with open("files/input/data.csv", "r") as archivo: 
        data = archivo.readlines()
    column_5 = [linea.split()[4] for linea in data]

    claves_1 = ('aaa','bbb','ccc','ddd','eee','fff',
              'ggg','hhh','iii','jjj')
    
    claves_2 = []
    for diccionario in column_5:
        x = diccionario.split(',')
        for i in x:
             clave = i.split(':')[0]
             claves_2.append(clave)
    
    dicc = {}
    for clave in claves_1:
        dicc[clave] = claves_2.count(clave)
    
    return dicc