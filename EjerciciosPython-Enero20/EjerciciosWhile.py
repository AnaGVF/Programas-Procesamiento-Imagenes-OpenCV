# 1. Imprimir números del 0 al 20

numero = 0
while(numero <= 20):
    print(numero)
    numero += 1

print()
print()

# 2. Imprimir números que se encuentran entre 80 y 90

numero2 = 80
while(numero2 < 90):
    print(numero2)
    numero2 += 1

print()
print()

# 3. Imprimir números entre 5 y 40, saltando de 5 en 5

numero3 = 10
while(numero3 < 40):
    print(numero3)
    numero3 += 5

print()
print()

# 4. Imprimir la tabla del 9

numero4 = 1
while(numero4 <= 10):
    print("9 x", numero4, "=", numero4 * 9)
    numero4 += 1

print()
print()

# 5. Imprimir la sumatoria del 1 al 20

suma = 0
numero5 = 1
while(numero5 <= 20):
    suma += numero5
    numero5 += 1
print(suma)

print()
print()

# 6. Imprimir múltiplos de 3 con el rango del 1 al 30.

numero6 = 0
while(numero6 < 30):
    numero6 += 3
    print(numero6)

print()
print()

# Número Primo
print("Dame un número:")
num = int(input())

i = 2

if(num == 1 or num == 2):
    print("ES PRIMO")
else:
    while(i <= num):
        if(num % i == 0):
            print("NO es primo") 
            break
        else:
            print("SI es primo")
            break

print()
print()

# --------------------------------------------------------------------------

i = 1
while(i <= 10):
    print(i)
    i = i + 1
else:
    print("El ciclo terminó", i)