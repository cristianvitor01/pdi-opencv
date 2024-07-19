# aplicando um efeito impulsivo em uma imagem (ruido sal e pimenta)

import cv2
import numpy as np
import random

img = cv2.imread('logo-if.jpg', cv2.IMREAD_GRAYSCALE) # carrega a imagem em escala de cinza


def noise(image, prob):
    output = np.zeros(image.shape, np.uint8) # cria uma imagem com o mesmo tamanho da imagem original
    thres = 1 - prob # calcula o limiar para definir se o pixel será preto ou branco
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random() # gera um número aleatório entre 0 e 1
            if rdn < prob: # se o número gerado for menor que a probabilidade, o pixel será preto
                output[i][j] = 0
            elif rdn > thres: # se o número gerado for maior que o limiar, o pixel será branco
                output[i][j] = 255
            else:
                output[i][j] = image[i][j] # caso contrário, o pixel será o mesmo da imagem original
    return output


noise = noise(img, 0.03)

cv2.imshow('Sal e Pimenta', noise)

cv2.waitKey(0)
cv2.destroyAllWindows()