# Resta de Imágenes OpenCV

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 22 de Febrero 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

im1 = cv2.imread('img/huesos2.bmp', 2)
im2 = cv2.imread('img/popo.bmp', 2)

dimensiones = im1.shape
r = dimensiones[0]
c = dimensiones[1]

im3 = np.zeros((r, c), dtype=np.int32)
im3 = cv2.subtract(im1, im2)

plt.subplot(1, 3, 1)
plt.imshow(im1, 'gray')
plt.title('Imagen 1')

plt.subplot(1, 3, 2)
plt.imshow(im2, 'gray')
plt.title('Imagen 2')

plt.subplot(1, 3, 3)
plt.imshow(im3, 'gray')
plt.title('Imagen Resultado')

plt.show()