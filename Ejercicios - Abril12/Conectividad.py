# Conectividad

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 12 de Abril 2021.

import matplotlib.pyplot as plt
import numpy as np

m = np.zeros((15, 15), dtype = np.int32)
# print(m)

i = 10
j = 10

m[i, j] = 1

# Cuadrado
m[i+1, j] = 1
m[i, j+1] = 1
m[i-1, j] = 1
m[i, j-1] = 1

m[i-1, j-1] = 1
m[i+1, j-1] = 1
m[i-1, j+1] = 1
m[i+1, j+1] = 1

# Diamante
m[i-7, j-6] = 2
m[i-7, j-5] = 2
m[i-7, j-4] = 2
m[i-6, j-7] = 2
m[i-6, j-6] = 2
m[i-6, j-5] = 2
m[i-6, j-4] = 2
m[i-6, j-3] = 2
m[i-5, j-7] = 2
m[i-5, j-6] = 2
m[i-5, j-5] = 2
m[i-5, j-4] = 2
m[i-5, j-3] = 2
m[i-4, j-6] = 2
m[i-4, j-5] = 2
m[i-4, j-4] = 2
m[i-3, j-5] = 2

# Piramide
m[i, j-6] = 3
m[i+1, j-7] = 3
m[i+1, j-6] = 3
m[i+1, j-5] = 3
m[i+2, j-8] = 3
m[i+2, j-7] = 3
m[i+2, j-6] = 3
m[i+2, j-5] = 3
m[i+2, j-4] = 3
m[i+3, j-9] = 3
m[i+3, j-8] = 3
m[i+3, j-7] = 3
m[i+3, j-6] = 3
m[i+3, j-5] = 3
m[i+3, j-4] = 3
m[i+3, j-3] = 3

print(m)

