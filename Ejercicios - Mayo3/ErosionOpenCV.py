# Erosión OpenCV

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 12 de Mayo 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("img/huesos2.bmp", 2)
kernel = np.ones((3, 3), np.uint8)

image = cv2.erode(img, kernel, iterations=1)

plt.imshow(image, 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.show()


