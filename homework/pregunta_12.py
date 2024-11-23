"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    with open("files/input/data.csv", "r") as archivo: 
        data = archivo.readlines()
    column_5 = [linea.split()[4] for linea in data]
    column_1 = [linea.split()[0] for linea in data]

    letras = list(set(column_1))
    letras.sort()
    
    dicc = {}
    for letra in letras:
        dicc[letra] = 0


    for letra, diccionario in zip(column_1, column_5):
        duplas = diccionario.split(',')
        #print(duplas)
        for dupla in duplas:
            valor = dupla.split(':')[1]
            dicc[letra] += int(valor)
        #print(letra, duplas)
    #print(dicc)
    return dicc
