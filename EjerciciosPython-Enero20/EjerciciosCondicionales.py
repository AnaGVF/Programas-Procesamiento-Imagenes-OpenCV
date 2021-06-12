# Condicionales

# Nombre: Ana Graciela Vassallo Fedotkin
# Fecha: 13 de Enero 2021.

# numero = int(input("Ingresa el numero"))

if(numero > 0):
    print("El número es mayor.")
else:
    print("El número es menor.")

# Dados 3 valores verificar si son iguales
# Verificar si a es menor que b
# Verificar si b es menor que c

a = int(input("Ingresa el primer número"))
b = int(input("Ingresa el segundo número"))
c = int(input("Ingresa el tercer número"))

if(a==b):
    print("a y b son iguales")
elif(b==c):
    print("b es igual a c")
if(a < b):
    print("a es menor que b")
elif(b < c):
    print("b es menor que c")

# Dados 3 valores de entrada, determinar si están en orden creciente
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))

if((a <= b) and (b <= c) and (b <= c)):
    print("Los números están en orden creciente.")
else:
    print("Los números NO están en orden creciente")

