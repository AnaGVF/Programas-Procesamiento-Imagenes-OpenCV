# Operadores Aritméticos
print(3+2/2*5)
print(8/2)
print(8//2)
print(3.5/2)
print(3.5//2)
print(8%2)
print(4-2)

print()

# Operadores Lógicos
x = True
y = False

print(x and y)
print(x or y)
print(not x)

print()

# Operadores Comparación
x = 8
print(x>12)
print(x==8)

print()

# Orden de Prioridad
x = 10
y = 5

print(x+3*y)
print((x+3)*y)

print()

# Texto y Variables
print("Cual es tu nombre ", end="")
print('Cual es tu apellido')

# Se utiliza una coma para concatenar variables.
nombre="Ana"
edad=23

print("Su nombre es", nombre, "y tiene", edad, "años.")

print(f"Hola, {nombre}")

print("Su nombre es {} y tiene {} años.".format(nombre, edad))

# Concatenar con el +
print("La edad es " + str(edad) + " años.")

print()
print()

# Ejercicio
nombre = input("Dame el nombre: ")
apellido1 = input("Dame el primer apellido: ")
apellido2 = input("Dame el segundo apellido: ")
dia = int(input("Dame el día de tu nacimiento: "))
mes = input("Dame el mes de tu nacimiento: ")
anio = int(input("Dame el año de tu nacimiento: "))

edad = 2021 - anio

print("Tu nombre es {} {} {}, tienes {} años y naciste el {} de {} de {}.".format(nombre, apellido1, apellido2, edad, dia, mes, anio))