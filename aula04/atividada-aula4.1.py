"""
Faça a redução da resolução de uma imagem tomando
por base a eliminação dos pixels da vizinhança-8.
"""

import cv2
import numpy as np

img = cv2.imread('original.jpeg', cv2.IMREAD_GRAYSCALE)  # Carregando a imagem em escala de cinza
img = cv2.resize(img, (350, 505))  # Redimensionando a imagem


def reduz(image):
    output = np.zeros((image.shape[0] // 2, image.shape[1] // 2),
                      np.uint8)  # Cria uma matriz de zeros com metade das dimensões da imagem
    for i in range(0, image.shape[0], 2):  # Percorre a imagem de 2 em 2
        for j in range(0, image.shape[1], 2):  # Percorre a imagem de 2 em 2
            output[i // 2][j // 2] = image[i][j]  # Atribui o valor do pixel da imagem original para a nova imagem
    return output


img_reduzida = reduz(img)  # reduz a resolução da imagem

cv2.imshow('Original', img)
cv2.imshow('Reduzida', img_reduzida)

cv2.waitKey(0)
cv2.destroyAllWindows()
