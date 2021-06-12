# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 10 de Febrero 2021.

# Ejemplo 1

# frutas = {'Platano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}

# fruta = input('Introduce la fruta:').title()
# kg = float(input('Introduce los kg:'))

# if fruta in frutas:
#     print("Los kg de {}, son {}".format(fruta, frutas[fruta]*kg))


# Ejemplo 2

# capitales = {}
# capitales["Queretaro"] = "Qro"
# capitales["Nayarit"] = "Tepic"
# capitales["Guanajuato"] = "Gto"

# for i in capitales:
#     print("La capital de {} es {}".format(i, capitales[i]))


# Ejercicio 1

alumnos = {}
marca = "si"

while(marca == "si"):
    nombre = input("Ingrese el nombre del alumno: ").title()
    calificacion = float(input("Ingrese la calificación del alumno: "))
    alumnos[nombre] = calificacion
    print(alumnos)
    marca = input("¿Desea continuar? Ingresa si o no: ")

# Ejercicio 2
personas = {}

print("Ingrese nuevos datos.")
personas["nombre"] = input("Ingrese el nombre de la persona:").title()
personas["edad"] = input("Ingrese la edad de la persona:").title()
personas["sexo"] = input("Ingrese el sexo de la persona:").title()
personas["telefono"] = input("Ingrese el telefono de la persona:").title()
personas["correo"] = input("Ingrese el correo electrónico de la persona:").title()

print(personas)
