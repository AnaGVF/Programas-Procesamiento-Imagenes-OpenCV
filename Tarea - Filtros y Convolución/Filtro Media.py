# Filtro Media

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 24 de Abril 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

# Imagen Original con Ruido
imagenOriginal = cv2.imread('img/imapimienta.bmp', 2)

# Se aplica el filtro de Media de 3x3 en la imagen
kernel = np.ones((3,3), np.float32) / 9
imagenFiltroMedia = cv2.filter2D(imagenOriginal, -1, kernel)

# Guarda la imagen 
cv2.imwrite('img-guardadas/FiltroMedia1.bmp', imagenFiltroMedia)

# Se despliega la imagen original 
plt.subplot(1, 2, 1)
plt.imshow(imagenOriginal, 'gray')
plt.title('Imagen Original con Ruido')
plt.xticks([]), plt.yticks([])

# Se despliega la imagen etiquetada 
plt.subplot(1, 2, 2)
plt.imshow(imagenFiltroMedia, 'gray')
plt.title('Imagen con Filtro Media')
plt.xticks([]), plt.yticks([])

plt.show()


