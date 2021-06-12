# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 10 de Febrero 2021.

import cv2
import numpy as np
import matplotlib.pyplot as plt

im = cv2.imread('img/Gato.jpg', cv2.IMREAD_GRAYSCALE)
print(im)
cv2.imshow('Titulo', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
