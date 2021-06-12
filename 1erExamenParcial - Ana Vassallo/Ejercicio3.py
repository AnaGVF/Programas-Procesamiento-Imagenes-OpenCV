# 1er Examen Parcial

# 3. Construye una matriz de 10x8 con números aleatorios entre 1 y 50 y almacena en un arreglo el número
# y la posición de los valores que se encuentran arriba de 30.

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 17 de Marzo 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

r = 10
c = 8

M = np.random.randint(51, size=(r, c))

print("Matriz:")
print(M)

diccionario = {}
       
# Almacenamiento en un arreglo el número y la posición de los valores que se encuentran arriba de 30
for i in range(r):
    for j in range(c):
        if M[i][j] > 30:
            diccionario[M[i][j]] = (i, j)

print()
print("Arreglo como diccionario donde la llave es el número mayor a 30 y el valor es la posición donde se encuentra: ")
print(diccionario)