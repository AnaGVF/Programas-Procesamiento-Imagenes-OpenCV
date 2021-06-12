# Opening & Closing a Mano

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

# Opening 
# Erosión seguida de dilatación 
erosionOpening = cv2.erode(im1, kernel, iterations=1)
dilatacionOpening = cv2.dilate(erosionOpening, kernel, iterations=1)

# Closing 
# Dilatación seguida de erosión 
dilatacionClosing = cv2.dilate(im2, kernel, iterations=1)
erosionClosing = cv2.erode(dilatacionClosing, kernel, iterations=1)

plt.subplot(1, 3, 1)
plt.title('Imagen Original')
plt.imshow(img, 'gray')
plt.xticks([]), plt.yticks([])

plt.subplot(1, 3, 2)
plt.title('Imagen Opening')
plt.imshow(dilatacionOpening, 'gray')
plt.xticks([]), plt.yticks([])

plt.subplot(1, 3, 3)
plt.title('Imagen Closing')
plt.imshow(erosionClosing, 'gray')
plt.xticks([]), plt.yticks([])

plt.show()