# Filtro de Mediana

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 24 de Abril 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

# Imagen Original con Ruido
imagenOriginal = cv2.imread('img/imapimienta.bmp', 2)

# Se aplica el filtro de Mediana de 3x3 en la imagen
imagenFiltroMediana = cv2.medianBlur(imagenOriginal, 3)

# Guarda la imagen 
cv2.imwrite('img-guardadas/FiltroMediana1.bmp', imagenFiltroMediana)

# Se despliega la imagen original 
plt.subplot(1, 2, 1)
plt.imshow(imagenOriginal, 'gray')
plt.title('Imagen Original con Ruido')
plt.xticks([]), plt.yticks([])

# Se despliega la imagen etiquetada 
plt.subplot(1, 2, 2)
plt.imshow(imagenFiltroMediana, 'gray')
plt.title('Imagen con Filtro de Mediana usando OpenCV')
plt.xticks([]), plt.yticks([])

plt.show()