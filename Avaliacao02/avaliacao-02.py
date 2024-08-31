# utilizar seguimentação de imagens para identificar círculo na imagem e pintar de vermelhor
# identificar quadrado na imagem e pintar de verde

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Original.png')

# escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# usando a transformada de Hough para detectar os círculos com a mínima distância de 200 para identificar somente o principal
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=200, param1=50, param2=30, minRadius=0, maxRadius=0)

# preencher os círculos detectados de vermelho
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(img, (x, y), r, (0, 0, 255), thickness=-1)

# função para detectar se um contorno é um quadrado
def quadrado(contour):
    epsilon = 0.04 * cv2.arcLength(contour, True) # verifica o perímetro do contorno
    approx = cv2.approxPolyDP(contour, epsilon, True)
    if len(approx) == 4: # verifica se o contorno é um quadrado
        (x, y, w, h) = cv2.boundingRect(approx) # verifica as coordenadas do contorno
        aspect_ratio = float(w) / h # verifica a razão de aspecto
        return 0.95 <= aspect_ratio <= 1.05
    return False

# detectar as bordas utilizando Canny
edges = cv2.Canny(gray, 100, 200)

# encontrar contornos
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    if quadrado(contour):
        cv2.drawContours(img, [contour], -1, (0, 255, 0), thickness=cv2.FILLED)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
