# 5. Convertir una imagen en escala de grises a una imagen binaria.

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 9 de Marzo 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

im1 = cv2.imread('img/popo.bmp', 2)

dimensiones = im1.shape
r = dimensiones[0]
c = dimensiones[1]

imBin = np.zeros((r, c), dtype=np.int32)

# Umbralización Binaria
for i in range(r):
    for j in range(c):
        if(int(im1[i][j] >= 127)):
            imBin[i][j] = 255
        else:
            imBin[i][j] = 0

plt.subplot(1, 2, 1)
plt.imshow(im1, 'gray')
plt.title("Imagen Original")

plt.subplot(1, 2, 2)
plt.imshow(imBin, 'gray')
plt.title("Imagen Binaria")

plt.show()