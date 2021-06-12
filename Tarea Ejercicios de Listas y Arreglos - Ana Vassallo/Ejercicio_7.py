# Ejercicio 7

# Realiza un programa que pida al usuario la anchura del triángulo y 
# dibuje sus puntos como se ilustra e la siguiente figura.

# *
# * *
# * * *
# * * * *
# * * *
# * *
# *

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 1 de Febrero 2021.

anchura = int(input("Ingrese la anchura del triángulo: "))

for i in range(0, anchura+1):
    for j in range(i):
        print("*", end=" ")
    print(" ")

for i in range(anchura-1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print(" ")