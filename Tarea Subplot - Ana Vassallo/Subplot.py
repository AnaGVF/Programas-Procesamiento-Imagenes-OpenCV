# TAREA
# Usa una sola figura para gráficar las siguientes funciones:
# (usa subplot, ejemplo:  subplot (2,3,6))
# Ejemplo:

# 1. f(x) = sen(x)+cos(x)
# 2. f(x) = log(x)
# 3. f(x) = sqrt(x)
# 4. f(x) = 5
# 5. f(x) = x       
# 6. f(x) = |x|   (valor absoluto)

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 8 de Febrero 2021.

import numpy as np
import matplotlib.pyplot as plt

# 1. f(x)=sen(x)+cos(x)

x = np.arange(0, 20, 0.01)
y = np.sin(x) + np.cos(x)

fig = plt.figure(1)
plt.clf()
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y)
ax.set_xlabel('Eje x')
ax.set_ylabel('Eje y')
ax.set_title('f(x)=sen(x)+cos(x)')
ax.grid(True)

# 2. f(x)=log(x)

x = np.arange(0, 20, 0.01)
y = np.log(x)

fig = plt.figure(2)
plt.clf()
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y)
ax.set_xlabel('Eje x')
ax.set_ylabel('Eje y')
ax.set_title('f(x)=log(x)')
ax.grid(True)

# 3. f(x) = sqrt(x)

x = np.arange(0, 20, 0.01)
y = np.sqrt(x)

fig = plt.figure(3)
plt.clf()
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y)
ax.set_xlabel('Eje x')
ax.set_ylabel('Eje y')
ax.set_title('f(x) = sqrt(x)')
ax.grid(True)

# 4. f(x) = 5

x = np.arange(0, 20, 100)
y = np.int(5)

fig = plt.figure(4)
plt.clf()
ax = fig.add_subplot(1, 1, 1)
plt.axhline(y)
ax.set_xlabel('Eje x')
ax.set_ylabel('Eje y')
ax.set_title('f(x) = 5')
ax.grid(True)

# 5. f(x) = x 
 
x = np.arange(0, 20, 0.01)
y = x      

fig = plt.figure(5)
plt.clf()
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y)
ax.set_xlabel('Eje x')
ax.set_ylabel('Eje y')
ax.set_title('f(x) = x')
ax.grid(True)

# 6. f(x) = |x|   (Valor Absoluto)

x = np.arange(-10, 10, 0.01)
y = np.absolute(x)

fig = plt.figure(6)
plt.clf()
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y)
ax.set_xlabel('Eje x')
ax.set_ylabel('Eje y')
ax.set_title('f(x) = |x|')
ax.grid(True)

plt.show()