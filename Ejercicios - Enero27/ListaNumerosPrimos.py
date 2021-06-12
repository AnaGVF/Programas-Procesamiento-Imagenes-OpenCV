# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 27 de Enero 2021.

listaPrimos = []

def primo(numero):
    if(numero < 1):
        return False
    elif (numero == 1 or numero == 2):
        return True
    else:
        for i in range(2, numero):
            if(numero % i == 0):
                return False
            else:
                return True

numero = 2
contador = 0

while(contador < 10):
    if(primo(numero)):
        listaPrimos.append(numero)
        contador += 1
    numero += 1

print(listaPrimos)
