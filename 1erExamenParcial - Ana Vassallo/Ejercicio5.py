# 1er Examen Parcial

# 5. Realiza las operaciones básicas de una imagen y mostrar los resultados en una sola figura (utiliza subplot
# para mostrar los resultados en el orden que a continuación se ilustra (utilizar tus propias funciones).

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 17 de Marzo 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

# Imagen 1
im1 = cv2.imread('img/popo.bmp', 2)

dimensiones = im1.shape
r1 = dimensiones[0]
c1 = dimensiones[1]

# Imagen 2
im2 = cv2.imread('img/huesos2.bmp', 2)

dimensiones = im2.shape
r2 = dimensiones[0]
c2 = dimensiones[1]

# Función de Suma de Imágenes Originales
def SumaImagenes(im1, im2):
    # Matriz con la Suma de Imágenes
    im3 = np.zeros((r1, c1), dtype=np.int32)

    # Suma de Imágenes
    for i in range(r1):
        for j in range(c1):
            im3[i][j] = int(im1[i][j]) + int(im2[i][j])

            if(im3[i, j] > 255):
                im3[i, j] = 255
    
    return im3

# Función de Resta de Imágenes Originales
def RestaImagenes(im1, im2):
    # Matriz con la Suma de Imágenes
    im4 = np.zeros((r1, c1), dtype=np.int32)
    for i in range(r1):
        for j in range(c1):
            im4[i][j] = int(im1[i][j]) - int(im2[i][j])

            if(im4[i, j] < 0):
                im4[i][j] = abs(im4[i][j])
            
    return im4

# Función de Histograma de la Suma de Imágenes Originales
h1 = np.zeros((256, 1), dtype='int')
im3 = SumaImagenes(im1, im2)
def HistogramaSumaImagenes(im3):    
    for i in range(r1):
        for j in range(c1):
            h1[im3[i, j]] = h1[im3[i, j]] + 1

    return h1

print("Histograma de la Suma de Imágenes:")
print(HistogramaSumaImagenes(im3))

print()

# Función de Histograma de la Resta de Imágenes Originales
h2 = np.zeros((256, 1), dtype='int')
im4 = RestaImagenes(im1, im2)
def HistogramaRestaImagenes(im4):    
    for i in range(r1):
        for j in range(c1):
            h2[im4[i, j]] = h2[im4[i, j]] + 1

    return h2

print("Histograma de la Resta de Imágenes:")
print(HistogramaRestaImagenes(im4))

# Imagen Original 1
plt.subplot(3, 2, 1)
plt.imshow(im1, 'gray')
plt.title('Imagen Original 1')
plt.xticks([]), plt.yticks([])

# Imagen Original 2
plt.subplot(3, 2, 2)
plt.imshow(im1, 'gray')
plt.title('Imagen Original 2')
plt.xticks([]), plt.yticks([])

# Suma de Imágenes Originales
plt.subplot(3, 2, 3)
plt.imshow(SumaImagenes(im1, im2), 'gray')
plt.title('Suma de Imágenes Originales')
plt.xticks([]), plt.yticks([])

# Resta de Imágenes Originales
plt.subplot(3, 2, 4)
plt.imshow(RestaImagenes(im1, im2), 'gray')
plt.title('Resta de Imágenes Originales')
plt.xticks([]), plt.yticks([])

# Histograma de la Suma de Imágenes Originales
plt.subplot(3, 2, 5)
plt.plot(HistogramaSumaImagenes(im3))
plt.title('Histograma de la Suma de Imágenes Originales')

# Histograma de la Resta de Imágenes Originales
plt.subplot(3, 2, 6)
plt.plot(HistogramaRestaImagenes(im4))
plt.title('Histograma de la Resta de Imágenes Originales')

plt.show()