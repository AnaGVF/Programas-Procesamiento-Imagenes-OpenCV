# 1er Examen Parcial

# 2. Muestra una imagen en escala de grises y encuentra el número máximo y mínimo de intensidad (Realizar
# tu propia función para calcular los números máximos y mínimo)

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 17 de Marzo 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

im1 = cv2.imread('img/popo.bmp', 2)

dimensiones = im1.shape
r = dimensiones[0]
c = dimensiones[1]

# Funcion de Intensidad Mínima
def funcionIntensidadMinima():
    intensidadMinima = 0
    for i in range(r):
        for j in range(c):
            if(int(im1[i][j] <= intensidadMinima)):
                intensidadMinima = im1[i][j]

    print("El número mínimo de intensidad es:", intensidadMinima)

# Funcion de Intensidad Máxima
def funcionIntensidadMaxima():
    intensidadMaxima = 0
    for i in range(r):
        for j in range(c):
            if(int(im1[i][j] >= intensidadMaxima)):
                intensidadMaxima = im1[i][j]

    print("El número máximo de intensidad es:", intensidadMaxima)

# Llamada a funciones 
funcionIntensidadMinima()
funcionIntensidadMaxima()

plt.subplot(1, 1, 1)
plt.imshow(im1, 'gray')
plt.title('Imagen en escala de grises')

plt.show()