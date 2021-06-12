# 4. Hacer un programa que lea varios números del teclado y calcule el cubo de esos números. 
#    El programa termina cuando el usuario introduce un número negativo.

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 20 de Enero 2021.

numero = 0

while(numero >= 0):
    numero = int(input("Introduce un número: "))
    resultado = numero**3
    print("El cubo de {} es: {}".format(numero, resultado))