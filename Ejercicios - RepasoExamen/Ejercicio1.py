# 1. Realiza una matriz con números aleatorios y calcula la sumatoria de la diagonal.

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 9 de Marzo 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

r = 5
c = 5

M = np.random.randint(20, size=(r, c))

sumatoria = 0

for i in range(r):
    for j in range(c):
        if i == j:
            sumatoria += M[i][j]

print("Matriz:")
print(M)

print("La sumatoria de la diagonal es:", sumatoria)

