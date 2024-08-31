import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Original.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=200,                # Distância mínima entre os centros dos círculos detectados
    param1=50,
    param2=30,
    minRadius=0,
    maxRadius=0
)

# Se círculos forem detectados, preenchê-los de vermelho
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(img, (x, y), r, (0, 0, 255), thickness=-1)

# Mostrar a imagem com os círculos preenchidos
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
