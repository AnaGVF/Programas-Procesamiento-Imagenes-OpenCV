# Filtro Promedio

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 26 de Abril 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

imagenOriginal = cv2.imread("img\imapimienta.bmp", 2)
img = cv2.imread("img\imapimienta.bmp", 2)

mascara = (np.ones([3, 3], dtype='int') / 9)

dimensiones = img.shape
r = dimensiones[0]
c = dimensiones[1]

i = 1
j = 1
for i in range(r-1):
    for j in range(c-1):
        img[i, j] = img[i-1, j-1]*mascara[0, 0] + img[i, j-1]*mascara[0, 1] + img[i+1, j-1]*mascara[0, 2] + img[i-1, j]*mascara[1, 0] + img[i, j]*mascara[1, 1] + img[i+1, j]*mascara[1, 2] + img[i-1, j+1]*mascara[2, 0] + img[i, j+1]*mascara[2, 1] + img[i+1, j+1]*mascara[2, 2]

# Se despliega la imagen original 
plt.subplot(1, 2, 1)
plt.imshow(imagenOriginal, 'gray')
plt.title('Imagen Original con Ruido')
plt.xticks([]), plt.yticks([])

# Se despliega la imagen etiquetada 
plt.subplot(1, 2, 2)
plt.imshow(img, 'gray')
plt.title('Imagen con Filtro Promedio')
plt.xticks([]), plt.yticks([])

plt.show()