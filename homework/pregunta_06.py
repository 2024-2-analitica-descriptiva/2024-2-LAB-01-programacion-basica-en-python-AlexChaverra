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
    list = {}
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()
        
        for line in lines:
            colums = line.split("\t")
            colum_5 = colums[4].split(",")

            for item in colum_5:
                i = item.split(":")
                key = i[0]
                value = int(i[1])
                
                if key in list:
                    list[key].append(value)
                else: 
                    list[key] = [value]
        result = sorted([(key, min(values), max(values)) for key, values in list.items()])
        
    return result

print(pregunta_06())