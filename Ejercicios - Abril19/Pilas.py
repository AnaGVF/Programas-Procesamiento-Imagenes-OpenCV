# Pilas

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 19 de Abril 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

# Crear una pila vacía
pila = []

# Añadir un elemento
r=1
while(r==1):
    dato = input("Ingresa el primer elemento: ")
    pila.append(dato)
    r = int(input("¿Deseas agregar otro elemento? Sí:1, No: 0:"))

# Retirar un elemento
r=1
while(r==1):
    e = int(input("¿Deseas eliminar el elemento superior de la pila? Sí:1, No: 0:"))
    if(e==1):
        pila.pop()    
    r = int(input("¿Deseas eliminar otro elemento de la pila? Sí:1, No: 0:"))

# Tamaño de la pila
len(pila)

# Leer el elemento superior de la pila sin retirarlo
for i in range(0, len(pila)):
    print(pila[i])