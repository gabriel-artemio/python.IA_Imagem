import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def detect_shape(contour):
    # Aproxime o contorno para encontrar o número de vértices
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.04 * peri, True)

    # Se a forma tiver 3 vértices, ela é um triângulo
    if len(approx) == 3:
        return "Triângulo"
    # Se a forma tiver 4 vértices, ela pode ser um quadrado ou retângulo
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        # Calcule a razão de aspecto da forma
        aspect_ratio = float(w) / h
        # Se a razão de aspecto estiver próxima de 1, é um quadrado
        if 0.95 <= aspect_ratio <= 1.05:
            return "Quadrado"
        # Caso contrário, é um retângulo
        else:
            return "Retângulo"
    # Se a forma tiver mais de 4 vértices, provavelmente é um círculo
    else:
        return "Círculo"

def process_image():
    filename = filedialog.askopenfilename()
    if filename:
        image = cv2.imread(filename)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 220, 255, cv2.THRESH_BINARY_INV)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            shape = detect_shape(contour)
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
            else:
                cX, cY = 0, 0
            cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
            cv2.putText(image, shape, (cX - 20, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        print("A imagem selecionada é um: " + shape)

        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # image = Image.fromarray(image)
        # image.thumbnail((400, 400), Image.LANCZOS)
        # image = ImageTk.PhotoImage(image)

        # label.config(image=image)
        # label.image = image

root = tk.Tk()
root.title("Detecção de Formas")

button = tk.Button(root, text="Selecionar Imagem", command=process_image)
button.pack(padx=10, pady=10)

label = tk.Label(root)
label.pack(padx=200, pady=75)

root.mainloop()