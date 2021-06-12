# Filtro Menor a Mano

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 30 de Abril 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

# Imágenes Original, la que será manipulada y la imagen de Salida 
imagenOriginal = cv2.imread("img\imapimienta.bmp", 2)
img = cv2.imread("img\imapimienta.bmp", 2)
imgSalida = np.zeros(img.shape, np.uint8)

dimensiones = img.shape
r = dimensiones[0]
c = dimensiones[1]

i = 1
j = 1
for i in range(r-1):
    for j in range(c-1):
        vecinosOrdenados = []
        vecinosOrdenados.extend((img[i-1, j-1], img[i, j-1], img[i+1, j-1], img[i-1, j], img[i, j], img[i+1, j], img[i-1, j+1], img[i, j+1], img[i+1, j+1]))
        vecinosOrdenados.sort()
        imgSalida[i, j] = vecinosOrdenados[0]

# Se despliega la imagen original 
plt.subplot(1, 2, 1)
plt.imshow(imagenOriginal, 'gray')
plt.title('Imagen Original con Ruido')
plt.xticks([]), plt.yticks([])

# Se despliega la imagen etiquetada 
plt.subplot(1, 2, 2)
plt.imshow(imgSalida, 'gray')
plt.title('Imagen con Filtro Menor a Mano')
plt.xticks([]), plt.yticks([])

plt.show()