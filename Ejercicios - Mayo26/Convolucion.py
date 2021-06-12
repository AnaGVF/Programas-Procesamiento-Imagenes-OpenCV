# Convolución

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Fecha: 26 de Mayo 2021.

# import cv2
# from matplotlib import pyplot as plt
# import numpy as np

# img = cv2.imread("img/huesos2.bmp", 2)

# # Prewitt
# kxp = np.array([[-1, 0, 1],
#               [-1, 0, 1],
#               [-1, 0, 1]])

# kyp = np.array([[-1, -1, 1],
#               [0, 0, 0],
#               [1, 1, 1]])

# # Sobel 
# kxS = np.array([[-1, -2, -1],
#               [0, 0, 0],
#               [1, 2, 1]])

# kyS = np.array([[-1, 0, 1],
#               [-2, 0, 2],
#               [-1, 0, 1]])

# # Roberts
# kxR = np.array([[1, 0],
#               [0, -1]])

# kyR = np.array([[0, 1],
#               [-1, 0]])

# gx = cv2.filter2D(img, cv2.CV_64F, kxp)
# gy = cv2.filter2D(img, cv2.CV_64F, kyp)


import cv2
import matplotlib.pyplot as plt
import numpy as np

# Sobel
Sx = np.array([[-1,0.,1.],[-2, 0, 2], [-1, 0, -1]])
Sy = np.array([[-1, -2, -1],[0, 0, 0],[1, 2, 1]])
# Prewitt
Px = np.array([[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]])
Py = np.array([[1, 1, 1],[0, 0, 0],[-1, -1, -1]])
# Roberts
Rx = np.array([[-1, 0, 0],[0, 1, 0],[0, 0, 0]])
Ry = np.array([[0, 0, -1],[0, 1, 0],[0, 0, 0]])

img=cv2.imread("img/huesos2.bmp",2)

plt.subplot(3,3,1)
plt.imshow(img,'gray')
plt.title("Imagen Original"), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,2)
plt.imshow(cv2.filter2D(img, -1, Sx),'gray')
plt.title("Sobel x"), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,3)
plt.imshow(cv2.filter2D(img, -1, Sy),'gray')
plt.title("Sobel y"), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,4)
plt.imshow(cv2.filter2D(img, -1, Px),'gray')
plt.title("Prewitt x"), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,5)
plt.imshow(cv2.filter2D(img, -1, Py),'gray')
plt.title("Prewitt y"),plt.xticks([]), plt.yticks([])

plt.subplot(3,3,6)
plt.imshow(cv2.filter2D(img, -1, Rx),'gray')
plt.title("Roberts x"),plt.xticks([]), plt.yticks([])
plt.subplot(3,3,7)
plt.imshow(cv2.filter2D(img, -1, Ry),'gray')
plt.title("Roberts y"),plt.xticks([]), plt.yticks([])

# dst = cv2.filter2D( img ,-1, Kv )
# plt.imshow(dst,"gray")
plt.show()
