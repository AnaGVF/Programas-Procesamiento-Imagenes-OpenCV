# Negativo de una Imagen

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

th = np.zeros((r, c), dtype=np.int32)

# Negativo de la imagen
for i in range(r):
    for j in range(c):
        th[i][j] = 255 - im1[i][j]

# Negativo de la imagen OpenCV
# th = cv2.bitwise_not(im1)

plt.subplot(1, 2, 1)
plt.imshow(im1, 'gray')
plt.title("Imagen original")

plt.subplot(1, 2, 2)
plt.imshow(th, 'gray')
plt.title("Imagen negativa")

plt.show()