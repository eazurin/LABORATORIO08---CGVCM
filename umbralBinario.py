import cv2

img = cv2.imread('img1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Umbral simple binario
ret, thresh_bin = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('THRESH_BINARY', thresh_bin)

# Umbral binario invertido
ret, thresh_inv = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('THRESH_BINARY_INV', thresh_inv)

cv2.waitKey(0)
cv2.destroyAllWindows()
