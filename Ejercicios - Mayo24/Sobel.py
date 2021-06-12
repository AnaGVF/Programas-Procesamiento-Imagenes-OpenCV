# Sobel con OpenCV

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 17 de Mayo 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("img/huesos2.bmp", 2)

sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3)

plt.subplot(3, 1, 1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.xticks([]), plt.yticks([])

plt.subplot(3, 1, 2)
plt.imshow(sobelx, cmap='gray')
plt.title("Sobel X")
plt.xticks([]), plt.yticks([])

plt.subplot(3, 1, 3)
plt.imshow(sobely, cmap='gray')
plt.title("Sobel Y")
plt.xticks([]), plt.yticks([])

plt.show()