# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 25 de Enero 2021.

# Podemos regresar una expresion
def sum(var1, var2, var3):
    return var1 + var2 + var3

print(sum(19, 20, 30))

print()
print()

# Función obtenga datos
def obtener_datos():
    return "python", "basico", "clase"

curso, nivel, materia = obtener_datos()
print(curso, nivel, materia)

print()
print()

# Factorial
def factorial(numero):
    f = 1
    for i in range(1, numero + 1):
        f=f*i
    return f

print("Factorial:", factorial(5))

print()
print()

# Factorial Recursivo
def factorialRecursivo(numero):
    if(numero == 0):
        return 1
    else:
        return numero * factorialRecursivo(numero-1)

print("Factorial Recursivo:", factorialRecursivo(5))

print()
print()