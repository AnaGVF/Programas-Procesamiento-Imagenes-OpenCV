# 1. Crear una lista de 20 elementos impares.
# 2. Añadir un elemento al final de la lista.
# 3. Añadir el número 50 al inicio de la lista.
# 4. Borrar el último elemento de la lista.
# 5. Borrar el antepenúltimo elemento de la lista.

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 25 de Enero 2021.


# 1.
listaNumeroImpares = []

while(len(listaNumeroImpares) != 20):
    numero = int(input("Escribe un número impar: "))
    if(numero % 2 == 0):
        print("El número es par. Escribe un número impar.")
    else:
        print("Número impar correcto.")
        listaNumeroImpares.append(numero)

print("Lista de números impares: ", listaNumeroImpares)
print()

# 2.
numeroInsertar = int(input("Ingresa un número para agregarlo al final de la lista: "))
listaNumeroImpares.insert(len(listaNumeroImpares), numeroInsertar)
print("Lista con número insertado al final: ", listaNumeroImpares)
print()

# 3.
listaNumeroImpares.insert(0, 50)
print("Número 50 añadido a la primera posición: ", listaNumeroImpares)

# 4.
listaNumeroImpares.pop()
print("Último elemento de la lista eliminado: ", listaNumeroImpares)

# 5. 
listaNumeroImpares.pop(len(listaNumeroImpares)-3)
print("Antepenúltimo elmeento de la lista borrado: ", listaNumeroImpares)
