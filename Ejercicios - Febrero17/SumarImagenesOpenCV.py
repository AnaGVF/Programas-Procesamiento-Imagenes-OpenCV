# Suma Imágenes con Métodos

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 17 de Febrero 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

im1 = cv2.imread('img/girl.jpg', 2)
im2 = cv2.imread('img/goldhill.png', 2)

# Dimensiones de la imagen 1
dimensiones = im1.shape
r = dimensiones[0]
c = dimensiones[1]

# Dimensiones de la imagen 2
dimensiones = im2.shape
r2 = dimensiones[0]
c2 = dimensiones[0]

# Crear una tercera matriz para almacenar el resultado de la suma
im3 = np.zeros((r, c), dtype=np.int32)

im3 = cv2.add(im1, im2)

plt.subplot(1, 3, 1)
plt.imshow(im1, 'gray')
plt.title('Girl')

plt.subplot(1, 3, 2)
plt.imshow(im2, 'gray')
plt.title('Goldhill')

plt.subplot(1, 3, 3)
plt.imshow(im3, 'gray')
plt.title('Suma')

plt.show()