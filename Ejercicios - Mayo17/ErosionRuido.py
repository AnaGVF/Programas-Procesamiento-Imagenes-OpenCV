# Erosion y Ruido

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 17 de Mayo 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

# Imagen Original 
img = cv2.imread('img/imapimienta.bmp', 2)

# Función para calcular el Complemento de una Imagen 
def complemento(im):
    for j in range(len(im)):
        for i in range(len(im)):
            im[i, j] = 255 - im[i, j]

    return im

# Aplicación del Complemento de una imagen
im = cv2.imread('img/imapimienta.bmp', 2)
# im2 = complemento(im)
kernel = np.ones((2, 2), np.uint8)
# Se obtiene la imagen dilatada del complemento de la imagen 
imdilate = cv2.dilate(im, kernel, iterations=1)
# imErosion = cv2.erode(im, kernel, iterations=3)
# Se obtiene la erosión mediante el complemento de la imagen dilatada del complemento de la primera imagen 
# imErosion = complemento(imdilate)

plt.subplot(1, 2, 1)
plt.title('Imagen Original')
plt.imshow(img, 'gray')
plt.xticks([]), plt.yticks([])

plt.subplot(1, 2, 2)
plt.title('Imagen Dilatada sin ruido')
plt.imshow(imdilate, 'gray')
plt.xticks([]), plt.yticks([])

plt.show()