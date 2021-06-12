# Método de Ordenamiento Quicksort de una lista 

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 26 de Enero 2021.

listaNumeros = [9, 7, 8, 5, 3, 4, 11, 2, 1, 6, 44]

def particionado(listaNumeros):
    pivote = listaNumeros[0]
    menores = []
    mayores = []

    for i in range(1, len(listaNumeros)):
        if(listaNumeros[i] < pivote):
            menores.append(listaNumeros[i])
        else:
            mayores.append(listaNumeros[i])

    return menores, pivote, mayores

def quicksort(listaNumeros):
    if(len(listaNumeros) < 2):
        return listaNumeros

    menores, pivote, mayores = particionado(listaNumeros)

    return quicksort(menores) + [pivote] + quicksort(mayores)


print(quicksort(listaNumeros))