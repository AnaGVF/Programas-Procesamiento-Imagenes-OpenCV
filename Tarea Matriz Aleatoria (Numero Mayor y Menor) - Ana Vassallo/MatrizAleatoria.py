# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 27 de Enero 2021.

# Crear una matriz (4x8) con numeros aleatorios, determinar cual es el número mayor y el número menor 

import numpy as np

matriz = np.random.randint(100, size=(4, 8))

mayor = matriz[0][0]
menor = matriz[0][0]

for i in matriz:
    for j in i:
        if(j > mayor):
            mayor = j
        if(j < menor):
            menor = j

print("Matriz: ")
print()
print(matriz)
print()
print("El número mayor de la matriz es:", mayor)
print("El número menor de la matriz es:", menor)