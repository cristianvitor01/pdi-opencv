# ▪Faça a redução da resolução de uma imagem tomando
# por base a média dos pixels na vizinhança-8.

import cv2
import numpy as np

img = cv2.imread('original.jpeg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (720, 720))


def reduz(image):
    output = np.zeros((image.shape[0] // 2, image.shape[1] // 2),
                      np.uint8)  # Cria uma matriz de zeros com metade das dimensões da imagem
    for i in range(0, image.shape[0], 2):  # Percorre a imagem de 2 em 2
        for j in range(0, image.shape[1], 2):  # Percorre a imagem de 2 em 2
            media = (int(image[i][j]) + int(image[i][j + 1]) + int(image[i + 1][j]) + int(
                image[i + 1][j + 1])) // 4  # media dos pixels na vizinhança 8
            # Garante que a média esteja dentro do intervalo correto para o tipo de dado np.uint8
            media = min(media, 255)
            output[i // 2][j // 2] = np.uint8(media)  # Atribui o valor da média para a nova imagem
    return output


img_reduzidav8 = reduz(img)  # reduz a resolução da imagem

cv2.imshow('Original', img)
cv2.imshow('Reduzida vizinhaça-8', img_reduzidav8)

cv2.waitKey(0)
cv2.destroyAllWindows()
