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

    list = {}
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()

        for line in lines:
            columns = line.split()
            num = int(columns[1])
            letters = columns[3].split(",")

            for letter in letters:

                if letter not in list:
                    list[letter] = 0
                list[letter] += num
    
    result = dict(sorted(list.items()))

    return result

print(pregunta_11())