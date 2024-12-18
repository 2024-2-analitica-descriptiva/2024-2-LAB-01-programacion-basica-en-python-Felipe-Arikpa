"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02(input_directory=r'C:\Users\arica\OneDrive\Analítica descriptiva\2024-2-LAB-01-programacion-basica-en-python-Felipe-Arikpa\files\input\data.csv'):
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    letras = []

    import csv
    with open(input_directory, mode='r') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        for lines in csv_reader:
            letras.append(lines[0])

    letras_unicas = set(letras)

    resultado = []

    for letra in letras_unicas:
        cantidad = sum(1 for x in letras if x == letra)
        resultado.append((letra, cantidad))

    resultado.sort()

    return resultado