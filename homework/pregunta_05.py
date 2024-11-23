"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open("files/input/data.csv", "r") as archivo: 
        data = archivo.readlines()

    column_1 = [linea.split()[0] for linea in data]
    column_2 = [linea.split()[1] for linea in data]

    letras = list(set(column_1))
    letras.sort()

    maximos = {}
    minimos = {}
    for letra in letras:
        maximos[letra] = 0
    for letra in letras:
        minimos[letra] = 1000

    for letra, num in zip(column_1, column_2):
        num = int(num)
        maxi = maximos.get(letra)
        mini = minimos.get(letra)
        if num > maxi:
            maximos[letra] = num
        if num < mini:
            minimos[letra] = num

    return ([(clave, maximos[clave], minimos[clave]) for clave in maximos])
pregunta_05()