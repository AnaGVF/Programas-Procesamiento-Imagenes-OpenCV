# Dilatación

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 3 de Mayo 2021.
# Continuado el 12 de Mayo 2021

import cv2
from matplotlib import pyplot as plt
import numpy as np

imagenOriginal = cv2.imread("img\EtiquetadoObjetos.PNG", 2)
imgSalida = cv2.imread("img\EtiquetadoObjetos.PNG", 2)
# img = np.zeros(img.shape, np.uint8)

dimensiones = imgSalida.shape
r = dimensiones[0]
c = dimensiones[1]

def dilatacionBasica(imgSalida):
    i = 1
    j = 1

    for i in range(r-1):
        for j in range(c-1):
            if(imgSalida[i, j] < imgSalida[i+1, j]):
                imgSalida[i, j] = imgSalida[i+1, j]

    for i in range(r-1):
        for j in range(c-1):
            if(imgSalida[i, j] < imgSalida[i, j+1]):
                imgSalida[i, j] = imgSalida[i, j+1]

    return imgSalida

dilatacionBasica(imgSalida)

# Se despliega la imagen original 
plt.subplot(1, 2, 1)
plt.imshow(imagenOriginal, 'gray')
plt.title('Imagen Original')
plt.xticks([]), plt.yticks([])

# Se despliega la imagen etiquetada 
plt.subplot(1, 2, 2)
plt.imshow(imgSalida, 'gray')
plt.title('Imagen con Dilatación')
plt.xticks([]), plt.yticks([])

plt.show()