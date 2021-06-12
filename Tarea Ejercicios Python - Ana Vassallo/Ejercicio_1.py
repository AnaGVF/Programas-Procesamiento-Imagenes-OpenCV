# 1. Realizar un programa que dados todos los tres lados de un triángulo, determine su área. Esta la calculamos aplicando la siguiente fórmula:

# Área=√(S*(S-L1)*(s-L2)*(S-L3). Donde S=(L1+L2+L3)/2.

# Nota: (Variables, L1,L2,L3 son variables de tipo real que representan los tres lados.

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 20 de Enero 2021.

import math

L1 = float(input("Ingresa el 1er lado: "))
L2 = float(input("Ingresa el 2do lado: "))
L3 = float(input("Ingresa el 3er lado: "))

S = (L1 + L2 + L3)/2

area = math.sqrt(S*(S-L1)*(S-L2)*(S-L3))

print("El área del triángulo es de: ", area, "unidades cuadradas.")