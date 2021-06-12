# Ejercicio 4

# Programa que declare tres listas, y calcule la sumatoria de los elementos en la lista 3.
# lista3=lista1+lista2


# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 1 de Febrero 2021.

import numpy as np

lista1 = []
lista2 = []
lista3 = []

lista1 = np.random.randint(10, size=5)
lista2 = np.random.randint(10, size=5)

print(lista1)
print(lista2)

for i in range(5):
    lista3.append(lista1[i] + lista2[i])

print(lista3)
