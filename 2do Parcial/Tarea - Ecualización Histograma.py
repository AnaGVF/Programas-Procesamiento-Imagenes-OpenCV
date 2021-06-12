# Ecualización del Histograma

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 24 de Marzo 2021.

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Leer la imagen 
img = cv2.imread('img/little-girl.jpg', 2)

# Ecualización de imagen con OpenCV
imagenEcualizada = cv2.equalizeHist(img)

# Imagen NO Ecualizada 
plt.subplot(2, 2, 1)
plt.title("Imagen No Ecualizada")
plt.imshow(img, 'gray')

# Histograma de Imagen NO Ecualizada
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.subplot(2, 2, 2)
plt.plot(hist, color='gray')
plt.xlabel('Intensidad de los valores')
plt.ylabel('Cantidad de pixeles')

# Imagen Ecualizada 
plt.subplot(2, 2, 3)
plt.title("Imagen Ecualizada")
plt.imshow(imagenEcualizada, 'gray')

# Histograma de Imagen Ecualizada
histEcualizado = cv2.calcHist([imagenEcualizada], [0], None, [256], [0, 256])

plt.subplot(2, 2, 4)
plt.plot(histEcualizado, color='gray')
plt.xlabel('Intensidad de los valores')
plt.ylabel('Cantidad de pixeles')

plt.show()