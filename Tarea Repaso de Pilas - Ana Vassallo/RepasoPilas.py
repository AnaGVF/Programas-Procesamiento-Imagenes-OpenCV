# Tarea - Repaso de Pilas

    # Realizar un programa en python que muestre las operaciones básicas de una estructura de Datos (PILA):

    # Crear (constructor): crea la pila vacía.
    # Tamaño (size): regresa el número de elementos de la pila.
    # Apilar (push): añade un elemento a la pila.
    # Desapilar (pop): lee y retira el elemento superior de la pila.
    # Leer último (top o peek): lee el elemento superior de la pila sin retirarlo.
        # https://www.youtube.com/watch?v=R1pqxPl50oU

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 14 de Marzo 2021.

# -------------------------------------------------

# EJEMPLO DEL VIDEO DE YOUTUBE

# pila = []
# print("ENTRADA")
# pila.append('T')
# print('T')
# pila.append('E')
# print('E')
# pila.append('C')
# print('C')

# print("SALIDA")
# n = pila.pop()
# print(n)
# n = pila.pop()
# print(n)
# n = pila.pop()
# print(n)

# -------------------------------------------------

class Pila:
    # Crear (constructor): crea la pila vacía.
    def __init__(self):
        self.pila = []

    # Tamaño (size): regresa el número de elementos de la pila.
    def sizePila(self):
        return len(self.pila)

    # Apilar (push): añade un elemento a la pila.
    def incluir(self, elemento):
        self.pila.append(elemento)

    # Desapilar (pop): lee y retira el elemento superior de la pila.
    def quitar(self):
        return self.pila.pop()

    # Leer último (top o peek): lee el elemento superior de la pila sin retirarlo.
    def ultimoElemento(self):
        return self.pila[len(self.pila)-1]

# Constructor
p = Pila()

# Proceso
print("Se inicializa la Pila.")
print("Tamaño inicial de la Pila:", p.sizePila())
print("Se agregan 3 elementos (1, 2, 3)...")
p.incluir(1)
p.incluir(2)
p.incluir(3)
print("Elemento superior de la pila:", p.ultimoElemento())
print("Tamaño actual de la Pila:", p.sizePila())
print("Se quita el elemento superior de la pila...")
p.quitar()
print("Tamaño actual de la Pila:", p.sizePila())
print("Elemento superior de la pila:", p.ultimoElemento())
print("Se quita el elemento superior de la pila...")
p.quitar()
print("Elemento superior de la pila:", p.ultimoElemento())
print("Tamaño actual de la Pila:", p.sizePila())
print("Se quita el elemento superior de la pila...")
p.quitar()
print("Tamaño actual de la Pila:", p.sizePila())