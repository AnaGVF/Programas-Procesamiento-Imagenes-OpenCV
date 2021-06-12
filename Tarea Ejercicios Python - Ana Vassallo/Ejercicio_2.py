# 2. Realizar un programa que, dado como entrada el monto de la compra de un cliente, determine lo que debe pagar dado el siguiente criterio:

# Si el monto es menor que $500 no hay descuento, 
# Si el monto está comprendido entre $500 y $1000 se aplica el 5%, 
# Si el monto está comprendido entre $1000 y $7000 se aplica el 11% de descuento, 
# Si el monto ésta comprendido entre $7000 y $15000 se aplica el 18 % de descuento.

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 20 de Enero 2021.

monto = float(input("Ingrese el monto total de compra: "))

if(monto < 500):
    print("No hay descuento.")
    print("Se debe pagar ${}".format(monto))
elif (monto >= 500 and monto < 1000):
    print("Se aplica el 5% de descuento")
    resultado = monto - (monto*0.05)
    print("Se debe pagar ${}".format(resultado))
elif (monto >= 1000 and monto < 7000):
    print("Se aplica el 11% de descuento")
    resultado = monto - (monto*0.11)
    print("Se debe pagar ${}".format(resultado))
elif (monto >= 7000 and monto < 15000):
    print("Se aplica el 18% de descuento")
    resultado = monto - (monto*0.18)
    print("Se debe pagar ${}".format(resultado))
else:
    print("El monto es demasiado alto.")