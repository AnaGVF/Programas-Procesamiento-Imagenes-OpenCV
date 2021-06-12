# Histograma con OpenCV

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 22 de Marzo 2021.

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/huesos2.bmp', 2)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
# cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
# images: Imagen de entrada, puede ser en escala de grises o a color 
# indica el canal [0, 1, 2]
# mask - region donde queremos calcular nuestro histograma
# histSize: intensidad máxima
# ranges: nuestro rango de valores [0, 256]

plt.plot(hist, color='gray')
plt.xlabel('Intensidad de los valores')
plt.ylabel('Cantidad de pixeles')
plt.show()