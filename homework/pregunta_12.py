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

    list = {}
    with open("files/input/data.csv", "r") as file:

        for line in file:
            letter = line.strip().split("\t")[0]
            colum_5 = line.strip().split("\t")[4]
            value_colum_5 = [int(value.split(":")[1]) for value in colum_5.split(",")]
            suma = sum(value_colum_5)
            if letter in list:
                list[letter] += suma
            else:
                list[letter] = suma

        result = dict(sorted(list.items()))
    
    return result

print(pregunta_12())
