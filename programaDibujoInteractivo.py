import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# VENTANA DE SELECCIÓN DE IMAGEN 
def seleccionar_imagen():
    Tk().withdraw()  
    filename = askopenfilename(title="Selecciona una imagen", filetypes=[("Archivos de imagen", "*.jpg *.png *.bmp")])
    return filename

imagen_path = seleccionar_imagen()

if imagen_path:
    canvas = cv2.imread(imagen_path)
else:
    canvas = np.ones((600, 800, 3), dtype=np.uint8) * 255

undo_stack = []
drawing = False
start_point = (-1, -1)
current_shape = 'line'

# FUNCIÓN DE DIBUJO 
def draw_shape(event, x, y, flags, param):
    global drawing, start_point, canvas, undo_stack

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)
        undo_stack.append(canvas.copy())

        if current_shape == 'line':
            cv2.line(canvas, start_point, end_point, (0, 0, 255), 2)
        elif current_shape == 'rectangle':
            cv2.rectangle(canvas, start_point, end_point, (0, 255, 0), 2)
        elif current_shape == 'circle':
            center = start_point
            radius = int(np.sqrt((end_point[0] - center[0])**2 + (end_point[1] - center[1])**2))
            cv2.circle(canvas, center, radius, (255, 0, 0), 2)

# CREAR VENTANA Y CALLBACK 
cv2.namedWindow('Dibujo Interactivo')
cv2.setMouseCallback('Dibujo Interactivo', draw_shape)

# MENSAJE EN PANTALLA 
instructions = np.zeros((100, canvas.shape[1], 3), dtype=np.uint8)
cv2.putText(instructions, 'Teclas: l=linea, r=rectangulo, c=circulo, u=deshacer, s=guardar, esc=salir', (10, 60),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

# BUCLE PRINCIPAL
while True:
    combined = np.vstack((instructions, canvas))
    cv2.imshow('Dibujo Interactivo', combined)
    key = cv2.waitKey(1) & 0xFF

    if key == 27:  # ESC para salir
        break
    elif key == ord('l'):
        current_shape = 'line'
        print("Modo: Línea")
    elif key == ord('r'):
        current_shape = 'rectangle'
        print("Modo: Rectángulo")
    elif key == ord('c'):
        current_shape = 'circle'
        print("Modo: Círculo")
    elif key == ord('u') and undo_stack:
        canvas = undo_stack.pop()
        print("Deshacer")
    elif key == ord('s'):
        cv2.imwrite('dibujo_final.png', canvas)
        print("Imagen guardada como dibujo_final.png")

cv2.destroyAllWindows()
