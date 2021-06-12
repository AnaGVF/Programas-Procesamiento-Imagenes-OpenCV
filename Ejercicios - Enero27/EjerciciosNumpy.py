# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 27 de Enero 2021.

import numpy as np

a = np.array([1, 3, 4, 5, 5])
print(a)

print()
print()

# 2x3
b = np.array([[1, 2, 3], [3, 5, 6]])
print(b)

print()
print()

# 3x2
c = b.reshape(3, 2)
print(c)

print()
print()

d = np.arange(0, 10, 3)
print(d)

print()
print()

print(np.pi)
print(np.sin(0.5))
print(np.cos(0.5))

print()
print()

# Crear una matriz con ceros 5x5
m = np.zeros((5, 5))
print(m)

print()

m2 = np.zeros((5, 5), dtype=int)
print(m2)

print()

m3 = np.ones((5, 7))
print(m3)

print()

mat = np.random.randint(10, size=(5, 5))
print(mat)

print()

mat = np.eye(3, dtype=int)
print(mat)

print()

# Crear matriz con números aleatorios 5x5 y poner 1s en su diagonal principal
matriz = np.random.randint(100, size=(5, 5))

for i in range(0, 5):
    for j in range(0, 5):
        if(i == j):
            matriz[i, j] = 1

print(matriz)

print()
print()

# Otra manera
m3 = np.random.randint(10, size=(5, 5))
print(m3)

dimensiones = m3.shape
r = dimensiones[0]
c = dimensiones[1]
print(r)
print(c)

for i in range(r):
    for j in range(c):
        if(i == j):
            m3[i, j] = 1

print(m3)

print()
print()

# Otra manera
m = np.random.randint(10, size=(5,5))
np.fill_diagonal(m, 1)
print(m)
print()

# Función np.full
full = np.full((4, 4), 10)
print(full)

print()
print()

# Función fromiter: array con valores DECRECIENTES devueltos
# por repetidor o iterador 
iterador = [i for i in range(50, 1, -3)]
k = np.fromiter(iterador, int, count=17)
print(k)

print()

# Función fromiter: array con valores CRECIENTES devueltos
# por repetidor o iterador 
iterable = [i for i in range(1, 40, 2)]
l = np.fromiter(iterable, int)
print(l)

print()

# Crear arreglo que de [0, 1, 4, 9, 16]
itera = [i ** 2 for i in range(0, 5)]
n = np.fromiter(itera, int)
print(n)

print()