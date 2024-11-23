"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    with open("files/input/data.csv", "r") as archivo: 
        data = archivo.readlines()

    column_1 = [linea.split()[0] for linea in data]
    column_2 = [linea.split()[1] for linea in data]

    letras = list(set(column_1))
    letras.sort()

    sumas = {}
    for letra in letras:
        sumas[letra] = 0

    for letra, num in zip(column_1, column_2):
        acumulador = int(sumas.get(letra))
        #print(letra, num)
        sumas[letra] = acumulador + int(num)
        #print(sumas)
    return ([(clave, sumas[clave]) for clave in sumas])


