"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08(input_directory='files/input/data.csv'):
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

    datos = []

    import csv
    with open(input_directory, mode='r') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        for lines in csv_reader:
            datos.append(lines[0:2])

    numeros_unicos = set([int(dato[1]) for dato in datos])

    resultado = []

    for numero in sorted(numeros_unicos):
        letras = set([x[0] for x in datos if int(x[1]) == numero])
        resultado.append((numero, sorted(letras)))

    return resultado
