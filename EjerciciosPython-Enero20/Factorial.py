# Factorial de un número.

# Nombre: Ana Graciela Vassallo Fedotkin
# Fecha: 20 de Enero 2021.

numero = int(input("Ingresa un número: "))
factorial = 1

for i in range(1, numero+1):
    factorial *= i

print("El factorial de {} es igual a: {}.".format(numero, factorial))