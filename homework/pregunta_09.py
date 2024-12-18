"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09(input_directory=r'C:\Users\arica\OneDrive\Analítica descriptiva\2024-2-LAB-01-programacion-basica-en-python-Felipe-Arikpa\files\input\data.csv'):
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    conteo_claves = {}

    import csv
    with open(input_directory, mode='r') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        for lines in csv_reader:
            diccionario = dict(pareja.split(":") for pareja in lines[4].split(","))
            for clave in diccionario:
                if clave in conteo_claves:
                    conteo_claves[clave] += 1
                else:
                    conteo_claves[clave] = 1

    conteo_claves = dict(sorted(conteo_claves.items()))

    return conteo_claves