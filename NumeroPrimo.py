# Nombre: Ana Graciela Vassallo Fedotkin
# Fecha: 13 de Enero 2021.

print("Dame un número:")
num = int(input())

if(num < 1):
    resultado = False
elif (num == 1 or num == 2):
    resultado = True
else:
    for i in range(2, num):
        if(num % i == 0):
            resultado = False
        else:
            resultado = True

if resultado == True:
    print("Es primo.")
elif resultado == False:
    print("No es primo.")
