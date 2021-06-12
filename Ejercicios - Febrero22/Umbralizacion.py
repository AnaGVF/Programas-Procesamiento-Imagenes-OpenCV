# Umbralización

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 22 de Febrero 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

im1 = cv2.imread('img/popo.bmp', 2)

ret, th1 = cv2.threshold(im1, 127, 255, cv2.THRESH_BINARY)
ret2, th2 = cv2.threshold(im1, 127, 255, cv2.THRESH_BINARY_INV)
ret3, th3 = cv2.threshold(im1, 127, 255, cv2.THRESH_TRUNC)
ret4, th4 = cv2.threshold(im1, 127, 255, cv2.THRESH_TOZERO)
ret5, th5 = cv2.threshold(im1, 127, 255, cv2.THRESH_TOZERO_INV)

dimensiones = im1.shape
r = dimensiones[0]
c = dimensiones[1]

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [im1, th1, th2, th3, th4, th5]
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()