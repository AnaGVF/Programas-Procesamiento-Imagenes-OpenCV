# Ejercicio 3

# Hacer un programa que inicialice una lista de números con 10 valores aleatorios, 
# y posterior ordene los elementos de menor a mayor.

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 1 de Febrero 2021.

import numpy as np

lista = np.random.randint(100, size=10)
print("Lista de números aleatorios:", lista)
lista.sort()
print("Lista ordenada:", lista)