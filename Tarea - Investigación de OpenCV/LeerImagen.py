# Tarea - Imágenes en OpenCV

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 14 de Febrero 2021.

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Función para mostrar una imagen
def mostrarIm(imagen, titulo):
    plt.figure()
    plt.title(titulo)
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    figura = plt.imshow(imagen)
    plt.show()
    return figura

# Se carga la imagen en una variable ---------------------------------------------------------
imagen = cv2.imread('img/Gato.jpg')
# imagen = cv2.imread('img/Ardilla.jpg')

# Se extraen las dimensiones de la imagen
h, w = imagen.shape[:2]

# Se despligan las dimensiones de la imagen en consola
print("Altura = {}, Anchura = {}".format(h, w))
mostrarIm(imagen, "Ejemplo de Imagen")

# ACCESO A LOS VALORES DE LA IMAGEN ---------------------------------------------------------
# Extracción de la Información de Color RGB
# Se selecciona una región de la imagen de 1 a 100, para "X" y "Y"
(B, G, R) = imagen[100, 100]

print("R = {}, G = {}, B = {}".format(R, G, B))

# Selección de información de un canal específico
NumeroCanal = 0
i = 100
j = 100
Bij = imagen[i, j, NumeroCanal]
print("B = {}".format(Bij))

# EXTRACCIÓN DE UNA REGIÓN DE INTERÉS ---------------------------------------------------------
roi = imagen[100 : 500, 200 : 700]
# roi es la submatriz sobre la imagen
mostrarIm(roi, "Ejemplo de Imagen")

# RE ESCALAR UNA IMAGEN ---------------------------------------------------------
imEscalada = cv2.resize(imagen, (800, 800))
mostrarIm(imEscalada, "Ejemplo de Imagen re escalada")

# ROTAR UNA IMAGEN ---------------------------------------------------------

# Centro de la imagen
centro = (w // 2, h // 2)

# Se genera una rotación en el plano de -45° a una distancia 1.0
matriz = cv2.getRotationMatrix2D(centro, -45, 1.0)

# Proyección sobre la matriz de rotación
imRotada = cv2.warpAffine(imagen, matriz, (w, h))
mostrarIm(imRotada, "Ejemplo de Imagen Rotada")

# DIBUJAR UN RECTÁNGULO ---------------------------------------------------------

# Generar imagen de salida, tomando como referencia una imagen previamente cargada
salida = imagen.copy()

# Generar un rectángulo de dimensiones conocidas en los lugares que determinan (1500, 900) - (600, 400) con el color en RGB (255, 0, 0)
rectangulo = cv2.rectangle(salida, (1500, 900), (600, 400), (255, 0, 0), 2)

mostrarIm(rectangulo, "Rectángulo")

# INSERCIÓN DE TEXTO ---------------------------------------------------------

# Generar una imagen de salida, tomando como referencia una imagen previamente cargada
salida = imagen.copy()

# Se añade el texto con las características que se desean 
texto = cv2.putText(salida, 'OpenCV Demo de texto', (500, 550), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)

mostrarIm(texto, "Texto")