import cv2

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

# Redimensionar todas al mismo tamaño
img1_resized = cv2.resize(img1, (max_width, max_height))
img2_resized = cv2.resize(img2, (max_width, max_height))
img3_resized = cv2.resize(img3, (max_width, max_height))

cv2.imshow('Imagen 1 Redimensionada', img1_resized)
cv2.imshow('Imagen 2 Redimensionada', img2_resized)
cv2.imshow('Imagen 3 Redimensionada', img3_resized)

cv2.waitKey(0)
