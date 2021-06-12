# Umbralización Manual Binaria

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 28 de Febrero 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

im1 = cv2.imread('img/huesos2.bmp', 2)
im2 = cv2.imread('img/huesos2.bmp', 2)

# Dimensiones de la imagen 1
dimensiones = im1.shape
r = dimensiones[0]
c = dimensiones[1]

numeroUmbralizacion = 127

# Umbralización Binaria
for i in range(r):
    for j in range(c):
        if(im2[i][j] < numeroUmbralizacion):
            im2[i][j] = 0
        else:
            im2[i][j] = 255

plt.subplot(1, 2, 1)
plt.imshow(im1, 'gray')
plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(1, 2, 2)
plt.imshow(im2, 'gray')
plt.title('Umbralización Binaria')
plt.xticks([]), plt.yticks([])

plt.show()