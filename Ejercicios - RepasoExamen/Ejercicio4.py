# 4. Construye una matriz de 5x4 con valores aleatorios ceros y unos.  
    # Muestra cuantos valores 1 y 0 se generaron 

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 9 de Marzo 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

r = 5
c = 4

M = np.random.randint(2, size=(r, c))

listaValores_Cero = 0
listaValores_Uno = 0

for i in range(r):
    for j in range(c):
        if M[i][j] == 0:
            listaValores_Cero += 1
        elif M[i][j] == 1:
            listaValores_Uno += 1

print("Matriz:")
print(M)
print()

print("Número de valores = 0:", listaValores_Cero)
print("Número de valores = 1:", listaValores_Uno)