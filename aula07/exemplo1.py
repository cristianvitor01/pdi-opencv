# calculo de histograma de uma imagem

import cv2
from matplotlib import pyplot as plt

imagem = cv2.imread('logo-if.jpg')

# Escala de cinza
imagem_pb = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# cv2.imshow('Escala de Cinza', imagem_pb)
#
# hist = cv2.calcHist([imagem_pb], [0], None, [256], [0, 256]) # [0] é o canal, None é a máscara e [256] é o número de bins e [0, 256] é o intervalo
# plt.plot(hist)
# plt.xlim([0, 256]) # limita o eixo x de 0 a 256
# plt.show()

#Colorido
cv2.imshow('Colorido',imagem)
color = ('b','g','r')
for i,c in enumerate(color):
    hist = cv2.calcHist([imagem],[i],None,[256],[0,256])
    plt.plot(hist,color = c)
    plt.xlim([0,256])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
