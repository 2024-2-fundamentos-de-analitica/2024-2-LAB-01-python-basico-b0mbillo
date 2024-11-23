"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    with open("files/input/data.csv", "r") as archivo: 
        data = archivo.readlines()
    column_5 = [linea.split()[4] for linea in data]
    column_4 = [linea.split()[3] for linea in data]
    column_1 = [linea.split()[0] for linea in data]

    lista = []
    for letra, letras, diccionario in zip(column_1, column_4, column_5):
        lista.append((letra, len(letras.split(',')), len(diccionario.split(','))))

    #print(lista)
    return lista