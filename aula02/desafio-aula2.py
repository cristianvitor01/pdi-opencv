# utilizar os comandos para filtrar partes de uma imagem com base em sua cor

import cv2
import numpy as np

img = cv2.imread('original.jpeg')
img = cv2.resize(img, (350, 505))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # converte a imagem para o espaço de cores HSV

gray = img.copy()


(row, col) = img.shape[0:2]

for i in range(row):
    for j in range(col):
        if (hsv[i, j][0]<170) or (hsv[i, j][0]>200): # filtrando as cores que estão no intervalo entre 170 e 200 (vermelho)
            gray[i, j] = sum(img[i, j]) * 0.33



cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem HSV', hsv)
cv2.imshow('Imagem Filtrada', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()