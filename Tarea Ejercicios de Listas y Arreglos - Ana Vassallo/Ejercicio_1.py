# Ejercicio 1

# Realizar un programa que inicialice una lista con 20 valores aleatorios (del 1 al 50) 
# y posteriormente muestre en pantalla cada elemento de la lista. 

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 31 de Enero 2021.

import numpy as np

lista = np.random.randint(50, size=20)
print("Lista:")
print(lista)

print()

print("Todos los elementos de la lista:")
for i in range(len(lista)):
    print(lista[i])