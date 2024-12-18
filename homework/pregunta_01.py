"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01(input_directory=r'..\files\input\data.csv'):
    """
    Retorne la suma de la segunda columna.
    Rta/
    214
    """

    suma_2col = 0

    import csv
    with open(input_directory, mode='r') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        for lines in csv_reader:
            suma_2col += int(lines[1])

    return suma_2col