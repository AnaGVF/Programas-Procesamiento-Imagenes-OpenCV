# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 10 de Febrero 2021.

import matplotlib.pyplot as plt

lista = [3, 4, 5, 6, 9, 16, 19]
plt.plot(lista, marker='x', linestyle='--', color='b', label='enero')
plt.title('Datos')
plt.grid(True)

lista2 = [2, 1, 3, 2, 5, 10, 9]
plt.plot(lista2, marker='d', linestyle='--', color='r', label='enero')
plt.show()