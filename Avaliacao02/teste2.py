import cv2
import numpy as np
import matplotlib.pyplot as plt

# Função para detectar se um contorno é um quadrado
def is_square(contour):
    epsilon = 0.04 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    if len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
        return 0.95 <= aspect_ratio <= 1.05
    return False

# Carregar a imagem
img = cv2.imread('Original.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detectar as bordas utilizando Canny
edges = cv2.Canny(gray, 100, 200)

# Encontrar contornos na imagem
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Percorrer os contornos encontrados e preencher os quadrados de vermelho
for contour in contours:
    if is_square(contour):
        cv2.drawContours(img, [contour], -1, (0, 255, 0), thickness=cv2.FILLED)

# Mostrar a imagem com os quadrados detectados e preenchidos
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
