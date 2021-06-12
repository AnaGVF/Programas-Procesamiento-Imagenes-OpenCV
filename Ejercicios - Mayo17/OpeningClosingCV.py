# Opening & Closing con OpenCV

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 17 de Mayo 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

# Imagen Original 
img = cv2.imread('img/imapimienta.bmp', 2)

# Imagen para Opening 
im1 = cv2.imread('img/imapimienta.bmp', 2)
# Imagen para Closing 
im2 = cv2.imread('img/imapimienta.bmp', 2)

kernel = np.ones((3, 3), np.uint8)

opening = cv2.morphologyEx(im1, cv2.MORPH_OPEN, kernel)

closing = cv2.morphologyEx(im2, cv2.MORPH_CLOSE, kernel)

plt.subplot(1, 3, 1)
plt.title('Imagen Original')
plt.imshow(img, 'gray')
plt.xticks([]), plt.yticks([])

plt.subplot(1, 3, 2)
plt.title('Imagen Opening')
plt.imshow(opening, 'gray')
plt.xticks([]), plt.yticks([])

plt.subplot(1, 3, 3)
plt.title('Imagen Closing')
plt.imshow(closing, 'gray')
plt.xticks([]), plt.yticks([])

plt.show()