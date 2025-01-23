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
    list = {}
    with open("files/input/data.csv", "r",) as file:
        for line in file:
            letter = line.strip().split("\t")[0]
            if letter in list:
                list[letter] += 1
            else:
                list[letter] = 1
    result = sorted(list.items())
    return result

print("Lista de tuplas:", pregunta_02())
