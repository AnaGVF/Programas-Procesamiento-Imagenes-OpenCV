# Ejercicio 9

# Guarda en un vector los primeros n números de la serie de Fibonacci.

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 1 de Febrero 2021.

numero = int(input("Ingrese el número hasta donde desea calcular la serie de Fibonacci: "))
listaFibo = []

def fibo(numero):
    if(numero <= 1):
        return numero
    else:
        return fibo(numero-1) + fibo(numero-2)

for i in range(numero):
    listaFibo.append(fibo(i))
    print(fibo(i))

print()
print("Lista con los números de Fibonacci: ")
print(listaFibo)