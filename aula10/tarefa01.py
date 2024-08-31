# utilize o algoritmo de inpaintg para remover alguns elementos da imagem

import cv2
import numpy as np

img1 = cv2.imread('ifma-caxias.png')
img2 = cv2.imread('logo-if.jpg')

# Redimensiona logo
img2 = cv2.resize(img2, (200, 100), interpolation=cv2.INTER_AREA)

# adiciona a logo no topo esquerdo
rows, cols, channels = img2.shape

# Trecho da imagem onde o logo ficará
roi = img1[0:rows, 0:cols]
cv2.imshow('Roi',roi)

# Cria máscara a partir de escala de cinza
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask_inv = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY)
mask = cv2.bitwise_not(mask_inv)

# Remove máscara da região de interesse
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Filtra somente a máscara obtida pelo threshold
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)

img1[0:rows, 0:cols] = dst

cv2.imshow('Imagem', img1)

telea = cv2.inpaint(dst, mask, 3, cv2.INPAINT_TELEA)
ns = cv2.inpaint(dst, mask, 3, cv2.INPAINT_NS)
img1[0:rows, 0:cols] = telea

cv2.imshow('Resultado', img1)
cv2.imshow('Mask', mask)
cv2.imshow('Area', dst)
cv2.imshow('Telea', telea)
cv2.imshow('NS', ns)
cv2.waitKey(0)
cv2.destroyAllWindows()
