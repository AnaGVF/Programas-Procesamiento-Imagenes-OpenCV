# Ejercicio 5

# Crea un arreglo bidimensional de longitud 5x5 y 
# calcule la sumatoria de los elementos de su diagonal.
# Muestra el contenido de la tabla en pantalla.

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 1 de Febrero 2021.

import numpy as np

sumatoria = 0

matriz = np.random.randint(10, size=(5, 5))

for i in range(0, 5):
    for j in range(0, 5):
        if(i == j):
            sumatoria += matriz[i, j]


print("Matriz:")
print(matriz)
print()
print("Sumatoria:", sumatoria)