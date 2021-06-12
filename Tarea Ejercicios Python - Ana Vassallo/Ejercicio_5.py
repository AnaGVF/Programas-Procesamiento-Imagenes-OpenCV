# 5. Hacer un programa utilizando while que lea 10 números enteros (positivos y negativos):

# a) Imprima cuantos números fueron mayores a cero

# b) Calcule el promedio de los números positivos,

# c) Obtenga el promedio de todos los números.

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 20 de Enero 2021. 

contadorTotal = 0
contadorMayorCero = 0
sumaNumPositivo = 0
promNumPositivo = 0
sumaTodosNum = 0
promTodosNum = 0

i = 1

while(i <= 10):
    numero = int(input("Ingrese un número (positivo o negativo): "))
    i += 1
    sumaTodosNum += numero
    contadorTotal += 1
    if(numero > 0):
        contadorMayorCero += 1
        sumaNumPositivo += numero

# Promedio Números Positivos
promNumPositivo = sumaNumPositivo / contadorMayorCero
# Promedio de todos los números
promTodosNum = sumaTodosNum / contadorTotal

print()

print("Cantidad de números mayores a cero: {}".format(contadorMayorCero))
print("Promedio de los números positivos: {}".format(promNumPositivo))
print("Promedio de todos los números: {}".format(promTodosNum))

