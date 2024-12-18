"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05(input_directory='files/input/data.csv'):
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    datos = []

    import csv
    with open(input_directory, mode='r') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        for lines in csv_reader:
            datos.append(lines[0:2])

    letras_unicas = set([dato[0] for dato in datos])

    resultado = []

    for letra in letras_unicas:
        numeros = [int(dato[1]) for dato in datos if dato[0] == letra]
        resultado.append((letra, max(numeros), min(numeros)))

    resultado.sort()

    return resultado