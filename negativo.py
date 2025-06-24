import cv2
import numpy as np

# Cargar imágenes
img1 = cv2.imread('img1.jpg')
img2 = cv2.imread('img2.jpg')
img3 = cv2.imread('img3.jpg')

# Obtener tamaños
h1, w1 = img1.shape[:2]
h2, w2 = img2.shape[:2]
h3, w3 = img3.shape[:2]

# Obtener el tamaño máximo
max_height = max(h1, h2, h3)
max_width = max(w1, w2, w3)

# Redimensionar todas
img1_resized = cv2.resize(img1, (max_width, max_height))
img2_resized = cv2.resize(img2, (max_width, max_height))
img3_resized = cv2.resize(img3, (max_width, max_height))

merged_img = np.zeros_like(img1_resized) # Imagen vacía

merged_img[:,:,0] = img3_resized[:,:,0]  # Canal azul
merged_img[:,:,1] = img2_resized[:,:,1]  # Canal verde
merged_img[:,:,2] = img1_resized[:,:,2]  # Canal rojo

cv2.imwrite('merged_img.jpg', merged_img)

# Negativo
negative_img = 255 - merged_img
cv2.imwrite('negative_img.jpg', negative_img)

# Escala de grises
gray_img = cv2.cvtColor(merged_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_img.jpg', gray_img)

cv2.imshow('Imagen gris', gray_img)
cv2.waitKey(0)
