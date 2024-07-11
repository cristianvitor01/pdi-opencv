import cv2

img = cv2.imread('logo-if.png')

b, g, r = cv2.split(img)  # separa os canais de cores da imagem

cv2.imshow('Imagem Original', img)
cv2.imshow('Canal Azul', b)
cv2.imshow('Canal Verde', g)
cv2.imshow('Canal Vermelho', r)

res = cv2.merge((b, g, r))  # junta os canais de cores da imagem
cv2.imshow('Imagem Original', res)

cv2.waitKey(0)
cv2.destroyAllWindows()