# 1er Examen Parcial

# 1. Realiza una matriz de 5x4 con números aleatorios y guardar en un arreglo los números impares de la
# diagonal principal.

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 17 de Marzo 2021.

import numpy as np
import matplotlib.pyplot as plt

r = 5
c = 4

M = np.random.randint(20, size=(r, c))

print("Matriz generada: ")
print(M)

numerosImpares = []

# Guarda en un arreglo los números impares de la diagonal principal.
for i in range(r):
    for j in range(c):
        if i == j:
            if(M[i][j] % 2 != 0):
                numerosImpares.append(M[i][j])

print()
print("Lista de Números Impares:")
print(numerosImpares)                 