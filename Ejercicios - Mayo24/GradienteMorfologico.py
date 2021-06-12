# Gradiente Morfológico

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 17 de Mayo 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("img/huesos2.bmp", 2)
kernel = np.ones((3, 3), np.uint8)

imdilate = cv2.dilate(img, kernel, iterations=1)

imerode = cv2.erode(img, kernel, iterations=1)

imgradiente = imdilate - imerode

plt.figure(1)
plt.subplot(2, 1, 1)
plt.imshow(img, 'gray')
plt.subplot(2, 1, 2)
plt.imshow(imgradiente, 'gray')
plt.title('Gradiente Morfológico')
plt.show()