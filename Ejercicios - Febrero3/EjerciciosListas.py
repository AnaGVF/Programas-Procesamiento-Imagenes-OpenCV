# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 3 de Febrero 2021.

import numpy as np
import random as rd

a = [1, 2, 3, 4, 5, 6]
print(a)

print()

b = np.array([1, 2, 3, 4, 5])
print(b)

print()

ra = np.append(a, 8)
print(ra)

print()

lista2 = [v**2 for v in a]
print(lista2)

print()

# Generar una lista con los números pares elevados al cuadrado
# [for in if]

lista3 = [j**2 for j in a if j%2==0]
print(lista3)

print()

# Crear una lista a partir de un iterador que muestre números impares
lista4 = [i for i in a if i%2 != 0]
print(lista4)

# Crear una lista a partir de un iterador que muestre el cubo de los números impares
lista5 = [i**3 for i in a if i%2 != 0]
print(lista5)

print()

print(a[0:3])
print(a[:])
print(a[1:-2])
print(a[-1])
print(a[2:-1])

print()
print()

# Crear un arreglo de mxn con valores aleatorios enteros

# matriz = np.random.randint(20, size=(4, 5))
# print(matriz)

r=5
c=5

M = np.zeros((r, c), dtype=np.int)

for i in range(r):
    for j in range(c):
        M[i][j] = rd.randint(0, 10)

print(M)
print(M.shape)

r1, c1 = M.shape
print(r1)
print(c1)

print()
print()

# Crear un arreglo bidimensional de longitud 5x5 y calcular la sumatoria de los elementos de la diagonal

suma = 0
for i in range(r1):
    for j in range(c1):
        if i == j:
            suma = suma + M[i][j]

print(suma)
print(M)
print()

# Sumatoria de 2 matrices

# dimension1 = int(input("Ingrese la primera dimensión: "))
# dimension2 = int(input("Ingrese la segunda dimensión: "))

# matriz1 = np.random.randint(10, size=(dimension1, dimension2))
# matriz2 = np.random.randint(10, size=(dimension1, dimension2))
# matriz3 = np.zeros((dimension1, dimension2), dtype=int)

# for i in range(dimension1):
#     for j in range(dimension2):
#         matriz3[i][j] = matriz3[i][j] + matriz1[i][j] + matriz2[i][j]

# print("Matriz 1:")
# print(matriz1)
# print()
# print("Matriz 2:")
# print(matriz2)    
# print()
# print("Matriz 3:")    
# print(matriz3)
# print()
# print()

# Suma de la otra diagonal de una matriz
sumatoria = 0

matriz = np.random.randint(10, size=(5, 5))

for i in range(4, -1, -1):
    sumatoria += matriz[i][4-i]


print("Matriz:")
print(matriz)
print()
print("Sumatoria:", sumatoria)
print()
print()

# ------------------------------------------

r = 5
c = 5

M1 = np.zeros((r,c), dtype=int)
M2 = np.zeros((r,c), dtype=int)
R1 = np.zeros((r,c), dtype=int)

for i in range(r):
    for j in range(c):
        M1[i][j] = rd.randint(0, 10)
        M2[i][j] = rd.randint(0, 10)
print(M1)
print(M2)
print()

# R1 = M1 + M2

# R1 = np.add(M1, M2)
# R1 = np.subtract(M1, M2)
# R1 = np.multiply(M1, M2)
# R1 = np.dot(M1, 5)
# R1 = np.negative(M1)
# R1 = np.sqrt(M2)
# R1 = np.power(M2, 5)
# R1 = np.cos(M2)
# R1 = np.min(M1)
# Obtiene la diferencia del valor mínimo y máximo
R1 = M1.ptp()
print(R1)
print()
print()

# EJERCICIO
# Obtener la media aritmética de una matriz
print(M1)
R1 = M1.mean()
print("Promedio de Matriz con método:", R1)

suma = 0
for i in range(0, 5):
    for j in range(0, 5):
        suma += M1[i][j]

elementos = M1.size
promedioMatriz = suma / elementos

print("Promedio de Matriz a mano:", promedioMatriz)