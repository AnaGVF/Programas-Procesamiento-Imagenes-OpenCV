# Ejercicio 2

# Solicitar 4 cadenas por teclado y guardar los elementos en una lista. 
# Copia los elementos de la lista en otra lista, pero en orden inverso.

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 31 de Enero 2021.

lista = []
listaInversa = []
i = 1
while(i <= 4):
    cadena = input("Escribe una palabra: ")
    lista.append(cadena)
    i += 1

print("Lista original: ", lista)

listaInversa = lista.copy()
listaInversa.reverse()

print("Lista Invertida: ", listaInversa)