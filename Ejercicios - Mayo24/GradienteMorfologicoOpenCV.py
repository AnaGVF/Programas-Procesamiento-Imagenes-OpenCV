# Gradiente Morfológico OpenCV

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 17 de Mayo 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("img/huesos2.bmp", 2)
kernel = np.ones((3, 3), np.uint8)

gradiente = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

plt.figure(1)
plt.subplot(2, 1, 1)
plt.imshow(img, 'gray')
plt.subplot(2, 1, 2)
plt.imshow(gradiente, 'gray')
plt.title('Gradiente Morfológico OpenCV')
plt.show()