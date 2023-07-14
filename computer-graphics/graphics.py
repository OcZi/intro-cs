# Salvador Donayre - Introd. CS
import numpy
from copy import copy
from PIL import Image
from numpy import ndarray

def suma(matriz: ndarray):
    summ = 0
    for element in matriz:
        if isinstance(element, ndarray):
            summ += suma(element)
        else:
            summ += element
    return summ

def contar(matriz: ndarray):
    count = 0
    for x in matriz:
        for y in x:
            for _ in y:
                count += 1
    return count


def maximo(matriz: ndarray):
    max_value = 0
    for x in matriz:
        for y in x:
            for color in y:
                if max_value < color:
                    max_value = color
    return max_value


def minimo(matriz: ndarray):
    min_value = 0
    for x in matriz:
        for y in x:
            for color in y:
                if min_value > color:
                    min_value = color
    return min_value


# TO REMEMBER - channel color order: [R, G, B]

def get_max_colorful(matriz: ndarray, index):
    # El spaninglish
    most_colorful = numpy.zeros(shape=3, dtype=int)
    for x in matriz:
        for y in x:
            if y[index] > most_colorful[index]:
                most_colorful = y
    return most_colorful


def pixel_mas_rojo(matriz: ndarray):
    return get_max_colorful(matriz, 0)


def pixel_mas_verde(matriz: ndarray):
    return get_max_colorful(matriz, 1)


def pixel_mas_azul(matriz: ndarray):
    return get_max_colorful(matriz, 2)


def grises(matriz: ndarray):
    # Cloning real matrix
    new_m = copy(matriz)
    for x in new_m:
        for y in x:
            y: numpy.ndarray = y
            avg = int(sum(y) / len(y))

            # Using same list instance
            # Set all elements of y with avg
            y[True] = avg
    return new_m

"""
# recuerden usar la direccion de la imagen para abrirla
image = Image.open("Circulation_map.png")
# La imagen se abre como RGBA, por lo que eliminamos el A
image = image.convert("RGB")
# convertimos la imagen a matriz
matrix = numpy.array(image)

print("Suma:", suma(matrix))
print("Suma2 :", suma2(matrix))
print("Suma3 :", suma3(matrix))
print("Elements:", contar(matrix))
print("Max:", maximo(matrix))
print("Min:", minimo(matrix))
print("Most R:", pixel_mas_rojo(matrix))
print("Most G:", pixel_mas_verde(matrix))
print("Most B:", pixel_mas_azul(matrix))
print("To gray scale:", a := grises(matrix))
"""