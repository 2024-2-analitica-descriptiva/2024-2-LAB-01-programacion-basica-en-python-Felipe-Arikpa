"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12(input_directory=r'C:\Users\arica\OneDrive\Analítica descriptiva\2024-2-LAB-01-programacion-basica-en-python-Felipe-Arikpa\files\input\data.csv'):
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    suma_por_letra = {}

    import csv
    with open(input_directory, mode='r') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        for lines in csv_reader:
            letra = lines[0]
            diccionario = dict(dato.split(':') for dato in lines[4].split(','))
            suma_valores = sum(int(valor) for valor in diccionario.values())
            if letra in suma_por_letra:
                suma_por_letra[letra] += suma_valores
            else:
                suma_por_letra[letra] = suma_valores

    suma_por_letra = dict(sorted(suma_por_letra.items()))

    return suma_por_letra