# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv
from time import process_time_ns


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    csvfile = open('stock.csv')

    stock = list(csv.DictReader(csvfile))
    totalTorn = 0
    for i in range(len(stock)):
        a = stock[i]
        for k,v in a.items():
            if k == 'tornillos':
                totalTorn += int(v)
                print(totalTorn)          


    csvfile.close()

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    


def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    prop = open('propiedades.csv')
    propiedade = list(csv.DictReader(prop))
    prop.close()

    depto2Amb = 0
    depto3Amb = 0

    for i in propiedade:
        for k,v in i.items():
            if k == 'ambientes':
                if v == '2':
                    depto2Amb += 1
                elif v == '3':
                    depto3Amb += 1

    print(f'Cantidad de deptos de 2 ambientes:{depto2Amb}')
    print(f'Cantidad de deptos de 3 ambientes:{depto3Amb}')

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
