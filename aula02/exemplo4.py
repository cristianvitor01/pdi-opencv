# informações sobre a imagem

import cv2

img = cv2.imread('logo-if.png', cv2.IMREAD_COLOR) # carrega a imagem
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converte a imagem para tons de cinza

print(img.shape) # imprime as dimensões da imagem
print(img.size) # imprime o número de pixels da imagem
print('=' * 20)
print(img.dtype) # imprime o tipo de dados da imagem
print(gray.shape) # imprime as dimensões da imagem em tons de cinza
print(gray.size) # imprime o número de pixels da imagem em tons de cinza

cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem em Tons de Cinza', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
