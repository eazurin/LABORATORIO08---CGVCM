import cv2

img = cv2.imread('img4.jpg')

# Dibujar círculo (x, y) y radio
cv2.circle(img, (500, 250), 100, (0, 255, 0), 3)

# Agregar texto
cv2.putText(img, 'Persona', (220, 240), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

cv2.imshow("", img)
key = cv2.waitKey(0)

cv2.imwrite('figura_anotada.jpg', img)
