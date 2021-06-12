# Pilas con Clases

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 19 de Abril 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

class Pila:
    def __init__(self):
        self.Pila = []
    # apilar(push): añade elementos a mi pila 
    def anadir(self, dato):
        self.pila.append(dato)

    def append(self, dato):
        self.pila.extend(dato)

    # desapilar(quitar): lee y quita elemento superior
    def quitar(self):
        return self.pila.pop()

    def tamanio(self):
        return len(self.pila)