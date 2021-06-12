# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 25 de Enero 2021.

Nature = ["Arbol", "Flor", "Planta", "Arbusto", "Pasto", "Fruta", "Vegetal", "Semilla", "Tierra", "Agua"]

for elemento in Nature:
    print(elemento)

print()
print()

# Imprimir números del 0 al 19 de una lista
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

for i in range(len(L)):
    print(L[i])

print()
print()

# Imprimir los números 12, 13, 14, 15, 16
for i in range(12, 17):
    print(L[i])

print()
print()

# Subindexación
print(L[12:17])

print()
print()

# Crear una lista con múltiplos de 6 hasta el 90
listaMultiplos6 = []
for i in range(0, 91, 6):
    listaMultiplos6.append(i)
print(listaMultiplos6)

print()
print()

# -------------------------------------------------------

# Ejemplo de cómo añadir un item al final de la lista
lista = [1, 2, 3, 4, 5, 6, 7, 8]
lista.append(10)
print(lista)

print()
print()

# Unir dos listas
a = [1, 3, 4]
b = [15, 16, 17]
a.extend(b)
print(a)

# El primer parámetro es la posición y el segundo el valor que queremos
a.insert(0, 0)
print(a)

a.insert(-1, 20)
print(a)

print()
print()

# Otro ejemplo
M = [5, 7, 8, 9, 10]
n = len(M)
M.insert(n, 50)
print(M)

print()
print()

# POP podemos indicarle un índice con el elemento a sacar(0 es el primer elemento)
L = [3, 4, 5, 6, 7, 8, 9]
print(L.pop())
print(L)

print()
print()

# MÉTODO remove
# Borrar el primer elemento donde el valor concuerde con el indicado
l = [10, 20, 30, 40, 50]
print(l)
l.remove(30)
print(l)

# MÉTODO reverse
l.reverse()
print(l)

print()
print()

# MÉTODO sort
lista = [8, 5, 22, 30]
lista.sort()
print(lista)