"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06(input_directory=r'..\files\input\data.csv'):
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

    valores_clave = {}

    import csv
    with open(input_directory, mode='r') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        for lines in csv_reader:
            diccionario = dict(pareja.split(":") for pareja in lines[4].split(","))
            for clave, valor in diccionario.items():
                valor = int(valor)
                if clave not in valores_clave:
                    valores_clave[clave] = {"min": valor, "max": valor}
                else:
                    if valor < valores_clave[clave]["min"]:
                        valores_clave[clave]["min"] = valor
                    if valor > valores_clave[clave]["max"]:
                        valores_clave[clave]["max"] = valor

    resultado = [(clave, valores_clave[clave]["min"], valores_clave[clave]["max"]) for clave in valores_clave]
    resultado.sort()

    return resultado