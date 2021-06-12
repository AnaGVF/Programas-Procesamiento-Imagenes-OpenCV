# Multiplicación

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 1 de Marzo 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

im1 = cv2.imread('img/popo.bmp', 2)

dimensiones = im1.shape
r = dimensiones[0]
c = dimensiones[1]

ime = np.zeros((r, c), dtype=np.int32)

for i in range(r):
    for j in range(c):
        ime[i, j] = im1[i, j]*2
        
        if(ime[i, j] > 255):
            ime[i, j] = 255

plt.subplot(1, 2, 1)
plt.imshow(im1, 'gray')
plt.title('Imagen original')

plt.subplot(1, 2, 2)
plt.imshow(ime, 'gray')
plt.title('Imagen multiplicada por un escalar')

plt.show()
