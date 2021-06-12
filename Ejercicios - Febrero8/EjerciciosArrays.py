# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 1 de Febrero 2021.

import numpy as np
import matplotlib.pyplot as plt
import math

# t = np.arange(0.1, 0.4, 0.3)
# print(t)

# print()

# tp = np.arange(8).reshape(2, 4)
# print(tp)

# print()
# print()

# x = np.arange(-4, 4, 0.1)
# y = x**2
# plt.plot(x, y)
# plt.show()

# print()

# x = np.arange(0, 10, 0.1)
# y = np.cos(4*x)
# plt.plot(x, y)
# plt.show()

# print()

# x = np.arange(0, 10, 0.1)
# y = np.sin(4*x)
# plt.plot(x, y)
# plt.show()

# print()

# x = np.arange(-4, 4, 0.1)
# y = x**3
# plt.plot(x, y)
# plt.show()

# print()

# t = np.arange(0, 2, 0.01)
# y = np.sin(4*np.pi*t)

# plt.figure(1)
# plt.clf()
# plt.plot(t, y)
# plt.xlabel('Eje x')
# plt.ylabel('Eje y')
# plt.title('Tiempo')
# plt.grid(True)
# plt.show()

# fig = plt.figure(2)
# plt.clf()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(t, y)
# ax.set_xlabel('Tiempo')
# ax.set_ylabel('Amplitud')
# ax.set_title('Titulo')
# ax.grid(True)
# plt.show()

# print()
# print()

# Histograma
# datos = np.random.randn(1000)
# plt.hist(datos, bins=10)
# plt.show()

# Ejercicio
# Crear 2 funciones

plt.figure(1)
plt.clf()
x = np.arange(0, 10, 0.1)
y = np.tan(2*x)
plt.plot(x, y)
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.title('Gráfica 1')
plt.grid(True)
plt.show()

plt.figure(2)
plt.clf()
x = np.arange(0, 50, 0.1)
y = np.cos(5*x**2)
plt.plot(x, y)
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.title('Gráfica 2')
plt.grid(True)
plt.show()