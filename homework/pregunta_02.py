"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    with open("files/input/data.csv", "r") as archivo: 
        data = archivo.read()
    data = data.split("\n")
    data.pop()
    column_1 = [linea.split()[0] for linea in data]
    
    letras = list(set(column_1))
    letras.sort()

    conteos = [(letra, column_1.count(letra)) for letra in letras]
    
    #print(conteos)
    return conteos
    
pregunta_02()
