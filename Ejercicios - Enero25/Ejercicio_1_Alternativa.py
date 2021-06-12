# 1. Crear una lista de 20 elementos impares.
# 2. Añadir un elemento al final de la lista.
# 3. Añadir el número 50 al inicio de la lista.
# 4. Borrar el último elemento de la lista.
# 5. Borrar el antepenúltimo elemento de la lista.

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 25 de Enero 2021.

li = []
for i in range(1, 40, 2):
    li.append(i)
print(li)

li.append(5)
print(li)

li.insert(0, 50)
print(li)