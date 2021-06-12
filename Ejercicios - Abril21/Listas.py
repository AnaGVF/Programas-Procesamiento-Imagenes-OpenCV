# Listas

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 21 de Abril 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

lista = []

for i in range(5):
    lista.append([i, i**2])

print((lista))

while(len(lista) != 0):
    print(lista.pop())

print(lista)