"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    with open("files/input/data.csv", "r") as archivo: 
        data = archivo.readlines()
    column_1 = [linea.split()[0] for linea in data]
    column_2 = [linea.split()[1] for linea in data]

    nums = [i for i in range(10)]
    dicc = {}
    for i in nums:
        dicc[i] = []
    
    for letra, num in zip(column_1,column_2): 
            if letra not in dicc[int(num)]:
                dicc[int(num)].append(letra)
                dicc[int(num)].sort()
    #print(dicc)
    return ([(clave, dicc[clave]) for clave in dicc])
