# Ejercicio 8

# ¿Cuál es la salida del siguiente programa?

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 1 de Febrero 2021.

anchura = int(input("Anchura del rectángulo: "))
altura = int(input("Altura del rectángulo: "))

for i in range(altura):
    for j in range(anchura):
        print("* ", end="")
    print()