# Ecualización del Histograma de Forma Manual

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 24 de Marzo 2021.

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Leer la imagen y dimensiones
img = cv2.imread('img/little-girl.jpg', 2)
dimensiones = img.shape
r = dimensiones[0]
c = dimensiones[1]

img2 = np.zeros(img.shape, dtype=int)

# Función para calcular el histograma 
def histograma(img):
    dimensiones = img.shape
    r = dimensiones[0]
    c = dimensiones[1]
    h = np.zeros(256, dtype=int)

    for i in range(r):
        for j in range(c):
            h[img[i][j]] += 1
    
    return h

# Ecualización del Histograma de Forma Manual
his = histograma(img)
cumulativeCounts = np.zeros(256)
cumulative = 0

# Cumulative Distribution
for i in range(len(his)):
    cumulative += his[i] * (1.0/(r*c))
    cumulativeCounts[i] = cumulative

# Reemplazar valores originales de pixeles por los normalizados
for i in range(r):
    for j in range(c):
        img2[i][j] = round(cumulativeCounts[img[i][j]] * 255)

# Imagen NO Ecualizada 
plt.subplot(2, 2, 1)
plt.title("Imagen No Ecualizada")
plt.imshow(img, 'gray')

# Histograma de Imagen NO Ecualizada
hist = histograma(img)

plt.subplot(2, 2, 2)
plt.plot(his, color='gray')
plt.xlabel('Intensidad de los valores')
plt.ylabel('Cantidad de pixeles')

# Imagen Ecualizada 
plt.subplot(2, 2, 3)
plt.title("Imagen Ecualizada")
plt.imshow(img2, 'gray')

# Histograma de Imagen 
his2 = histograma(img2)

plt.subplot(2, 2, 4)
plt.plot(his2, color='gray')
plt.xlabel('Intensidad de los valores')
plt.ylabel('Cantidad de pixeles')

plt.show()