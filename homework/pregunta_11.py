"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    with open("files/input/data.csv", "r") as archivo: 
        data = archivo.readlines()
    column_4 = [linea.split()[3] for linea in data]
    column_2 = [linea.split()[1] for linea in data]

    letras = ('a', 'b', 'c', 'd', 'e', 'f', 'g') #se haria haciendole flatten a la columna y luego pasando esta lista a un set y el set a lista o tupla

    dicc = {}
    for letra in letras:
        dicc[letra] = 0

    for num, letras in zip(column_2, column_4):
        for letra in letras.split(','):
            dicc[letra] += int(num)
    #print(dicc)
    return dicc
