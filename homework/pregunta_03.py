"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03(input_directory=r'C:\Users\arica\OneDrive\Analítica descriptiva\2024-2-LAB-01-programacion-basica-en-python-Felipe-Arikpa\files\input\data.csv'):
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    datos = []

    import csv
    with open(input_directory, mode='r') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        for lines in csv_reader:
            datos.append(lines[0:2])

    suma_por_letra = {}

    for letra, numero in datos:
        if letra in suma_por_letra:
            suma_por_letra[letra] += int(numero)
        else:
            suma_por_letra[letra] = int(numero)

    resultado = sorted(suma_por_letra.items())

    return resultado