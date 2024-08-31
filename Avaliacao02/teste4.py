import cv2
import numpy as np
import matplotlib.pyplot as plt

# Função para detectar se um contorno é um quadrado
def quadrado(contour):
    approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
    if len(approx) == 4:
        _, _, w, h = cv2.boundingRect(approx)
        aspect_ratio = w / float(h)
        return 0.95 <= aspect_ratio <= 1.05
    return False

# Carregar a imagem em colorido
img = cv2.imread('Original.png')

# Converter para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Usar a transformada de Hough para detectar os círculos com a mínima distância de 200 para identificar somente o principal
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=200, param1=50, param2=30, minRadius=0, maxRadius=0)

# Preencher os círculos detectados de vermelho
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(img, (x, y), r, (0, 0, 255), thickness=-1)

# Detectar as bordas utilizando Canny
edges = cv2.Canny(gray, 100, 200)

# Encontrar contornos na imagem
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Percorrer os contornos encontrados e preencher os quadrados de verde
for contour in contours:
    if quadrado(contour):
        cv2.drawContours(img, [contour], -1, (0, 255, 0), thickness=cv2.FILLED)

# Mostrar a imagem com os círculos e quadrados detectados e preenchidos
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
