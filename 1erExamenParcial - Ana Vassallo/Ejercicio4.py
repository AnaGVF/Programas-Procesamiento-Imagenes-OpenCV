# 1er Examen Parcial

# 4. Construye una matriz de 5x4 con valores aleatorios generados ceros y unos.

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 17 de Marzo 2021.

import numpy as np
import matplotlib.pyplot as plt

r = 5
c = 4

# Matriz con valores aleatorios generados ceros y unos 
M = np.random.randint(2, size=(r, c))

print("Matriz generada: ")
print(M)