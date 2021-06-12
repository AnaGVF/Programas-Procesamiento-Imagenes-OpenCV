# Histograma Manual

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 22 de Marzo 2021.

import cv2
import numpy as np
from matplotlib import pyplot as plt

def histograma(img):
    dimensiones = img.shape
    r = dimensiones[0]
    c = dimensiones[1]
    h = np.zeros((256, 1), dtype=int)

    for i in range(r):
        for j in range(c):
            h[img[i, j]] = h[img[i, j]] + 1
    
    return h

img = cv2.imread('img/huesos2.bmp', 2)

plt.subplot(1, 2, 1)
plt.title("Imagen")
plt.imshow(img, 'gray')

plt.subplot(1, 2, 2)
plt.plot(histograma(img), color='gray')
plt.title("Histograma")
plt.xlabel('Intensidad de los valores')
plt.ylabel('Cantidad de pixeles')

plt.show()
