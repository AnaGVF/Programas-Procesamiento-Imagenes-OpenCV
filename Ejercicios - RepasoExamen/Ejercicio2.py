# 2. Muestra una imagen en escala de grises y encuentra el número máximo de intensidad.

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

intensidad = 0

for i in range(r):
    for j in range(c):
        if(int(im1[i][j] >= intensidad)):
            intensidad = im1[i][j]

print("El número máximo de intensidad es:", intensidad)

plt.subplot(1, 1, 1)
plt.imshow(im1, 'gray')
plt.title('Imagen en escala de grises')

plt.show()