# Número Primo Ingresado por el Usuario

# Nombre: Ana Graciela Vassallo Fedotkin
# Fecha: 13 de Enero 2021.

numero = int(input("Dame el número: "))
contador = 0
for i in range(1, numero+1):
    if(numero%i == 0):
        contador = contador + 1

if(contador > 2):
    print("NO ES PRIMO")
else:
    print("ES PRIMO")

