# ▪Utilize thresholding e operações lógicas para aplicar
# overlay em uma imagem

# colocar uma imagem sobreponho a outra como logo

import cv2

img1 = cv2.imread('ifma-caxias.jpg')
img2 = cv2.imread('logo-if.jpg')

img2 = cv2.resize(img2, (200, 100), interpolation=cv2.INTER_AREA) # Redimensiona a imagem


rows, cols, channels = img2.shape # Pega as dimensões da imagem

roi = img1[0:rows, 0:cols]
cv2.imshow('Roi',roi)

# Cria máscara a partir de escala de cinza
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask_inv = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY)
mask = cv2.bitwise_not(mask_inv)

cv2.imshow('Gray', img2gray)
cv2.imshow('Threshold', mask)
cv2.imshow('Mask Inv', mask_inv)

# Remove máscara da região de interesse
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Filtra somente a máscara obtida pelo threshold
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)

img1[0:rows, 0:cols] = dst # Sobrepondo a imagem

cv2.imshow('Resultado', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
