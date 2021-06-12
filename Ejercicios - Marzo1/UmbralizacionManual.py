# Umbralización Manual

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 1 de Marzo 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

im1 = cv2.imread('img/Bear.png', 2)

dimensiones = im1.shape
r = dimensiones[0]
c = dimensiones[1]

th = np.zeros((r, c), dtype=np.int32)

# Umbralización Binaria
for i in range(r):
    for j in range(c):
        if(int(im1[i][j] >= 127)):
            th[i][j] = 255
        else:
            th[i][j] = 0

# Umbralización Binaria Inversa
# for i in range(r):
#     for j in range(c):
#         if(int(im1[i][j] >= 127)):
#             th[i][j] = 0
#         else:
#             th[i][j] = 255

# Umbralización Trunc
# for i in range(r):
#     for j in range(c):
#         if(int(im1[i][j] >= 127)):
#             th[i][j] = 127
#         else:
#             th[i][j] = im1[i][j]

# Umbralización ToZero
# for i in range(r):
#     for j in range(c):
#         if(int(im1[i][j] >= 127)):
#             th[i][j] = im1[i][j]
#         else:
#             th[i][j] = 0

# Umbralización ToZero Inv Inversa
# for i in range(r):
#     for j in range(c):
#         if(int(im1[i][j] >= 127)):
#             th[i][j] = 0
#         else:
#             th[i][j] = im1[i][j]



plt.subplot(1, 2, 1)
plt.imshow(im1, 'gray')
plt.title("Imagen original")

plt.subplot(1, 2, 2)
plt.imshow(th, 'gray')
plt.title("Imagen umbralizada")

plt.show()