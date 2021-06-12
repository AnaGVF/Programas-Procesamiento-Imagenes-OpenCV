# 3. Crear un programa que pida un número al usuario (entre 1 y 20) y muestre los números del 1 al 20, 
#    excepto el indicado por el usuario, usando "continue" para evitar ese valor.

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 20 de Enero 2021.

numero = int(input("Ingrese un número entre el 1 y 20: "))

if(numero < 1 or numero > 20):
    print("Ingrese un número dentro del rango especificado.")
else:
    for i in range(1, 21):
        if(i == numero):
            continue
        else:
            print(i)