# utilizar os comandos de acesso e edição de pixels para converter a imagem em escala de cinza

import cv2

img = cv2.imread('logo-if.png')

gray = cv2.imread('logo-if.png', cv2.IMREAD_GRAYSCALE) # lendo a imagem em escala de cinza

(row, col) = img.shape[0:2]

for i in range(row):
    for j in range(col):
        media = int(sum(img[i, j]) / 3) # calculando a média dos valores dos pixels
        img[i, j] = (media, media, media) # atribuindo a média para os 3 canais de cores
        # img[i, j] = sum(img[i, j]) * 0.33 # outra forma de calcular a média

cv2.imshow('Media', img)
cv2.imshow('Imagem em Tons de Cinza', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()