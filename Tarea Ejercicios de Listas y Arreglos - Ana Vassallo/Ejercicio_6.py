# Ejercicio 6

# Cree un arreglo bidimensional de 5x5 con números aleatorios del 1 al 20 
# y muestra cuantos números son mayores a 10.

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 1 de Febrero 2021.

import numpy as np

contador = 0
matriz = np.random.randint(20, size=(5, 5))

for i in range(5):
    for j in range(5):
        if(matriz[i, j] > 10):
            contador += 1

print("Matriz:")
print(matriz)
print()
print("Hay {} números mayores a 10.".format(contador))