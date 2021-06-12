# Ejercicio 10

# Utiliza indexamiento para extraer los elementos marcados 
# (por ejemplo: a[0,3:5] extrae los elementos 3 y 4 )

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 1 de Febrero 2021.

import numpy as np

matriz = np.array([[0, 1, 2, 3, 4, 5], [10, 11, 12, 13, 14, 15], 
                   [20, 21, 22, 23, 24, 25], [30, 31, 32, 33, 34, 35], 
                   [40, 41, 42, 43, 44, 45], [50, 51, 52, 53, 54, 55]])

amarillo = matriz[0, 3:5]

rojo = matriz[0:6, 2]

verde = matriz[2:5:2, 0:5:2]

azul = matriz[4:6, 4:6]

print("Matriz:")
print(matriz)

print()
print("Amarillo:")
print(amarillo)
print()
print("Rojo:")
print(rojo)
print()
print("Verde:")
print(verde)
print()
print("Azul:")
print(azul)