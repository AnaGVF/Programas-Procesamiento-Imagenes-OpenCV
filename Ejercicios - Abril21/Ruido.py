# Ruido

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 21 de Abril 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np
import random

def sp_ruido(imagen, prob):
    salida = np.zeros(imagen.shape, np.uint8)

    for i in range(imagen.shape[0]):
        for j in range(imagen.shape[1]):
            rdn = random.random()
            if(rdn < prob):
                salida[i][j] = 0
            else: 
                salida[i][j] = imagen[i][j]
    
    return salida

# Imagen 
imagen = cv2.imread('img/popo.bmp', 2)
ruido_img = sp_ruido(imagen, 0.05)
cv2.imwrite('img-guardadas\imapimienta.bmp', ruido_img)
plt.imshow(ruido_img, 'gray')
plt.show()

# Imagen Original
plt.subplot(1, 2, 1)
plt.imshow(imagen, 'gray')
plt.title('Imagen Original')
plt.xticks([]), plt.yticks([])

# Imagen con Ruido
plt.subplot(1, 2, 2)
plt.imshow(ruido_img, 'gray')
plt.title('Imagen con Ruido')
plt.xticks([]), plt.yticks([])

plt.show()