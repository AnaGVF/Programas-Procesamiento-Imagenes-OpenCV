# Histograma

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 1 de Marzo 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('img/popo.bmp', 2)

dimensiones = img.shape
r = dimensiones[0]
c = dimensiones[1]

h = np.zeros((256, 1), dtype='int')

def histograma(img):
    for i in range(r):
        for j in range(c):
            h[img[i, j]] = h[img[i, j]] + 1

    return h

print(histograma(img))


# Todos los valores de la imagen en una lista 
l = []

for i in range(r):
    for j in range(c):
        l.append(img[i][j])

print(l)


# Contar cuántos pixeles hay
print(len(l))

