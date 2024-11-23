"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    with open("files/input/data.csv", "r") as archivo: 
        data = archivo.readlines()
    column_5 = [linea.split()[4] for linea in data]

    claves = ('aaa','bbb','ccc','ddd','eee','fff',
              'ggg','hhh','iii','jjj')
    
    maximos = {}
    minimos = {}
    for clave in claves:
        maximos[clave] = 0
    for clave in claves:
        minimos[clave] = 1000

    pares = []
    for diccionario in column_5:
        x = diccionario.split(',')
        for i in x:
             pares.append(i)

    #print(pares)

    for par in pares:
        clave, valor = par.split(':')
        if clave in claves: # siempre van a estar ya que las claves fueron puestas explicitamente
            if int(valor) > maximos[clave]:
                maximos[clave] = int(valor)
            if int(valor) < minimos[clave]:
                minimos[clave] = int(valor)

    return([(clave, minimos[clave], maximos[clave]) for clave in maximos])
