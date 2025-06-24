import cv2

# Cargar imagen
img = cv2.imread('img2.jpg')

# Copia original para restaurar canales
img_original = img.copy()

# Estado de visibilidad de cada canal
show_red = True
show_green = True
show_blue = True

while True:
    # Crear copia de la imagen para modificar canales
    img_display = img.copy()

    if not show_red:
        img_display[:, :, 2] = 0
    if not show_green:
        img_display[:, :, 1] = 0
    if not show_blue:
        img_display[:, :, 0] = 0

    # Mostrar imagen
    cv2.imshow('Canales RGB', img_display)

    key = cv2.waitKey(0) & 0xFF

    if key == 27:  # ESC para salir
        break
    elif key == ord('r'):
        show_red = not show_red  # alterna estado
    elif key == ord('g'):
        show_green = not show_green
    elif key == ord('b'):
        show_blue = not show_blue

cv2.destroyAllWindows()
