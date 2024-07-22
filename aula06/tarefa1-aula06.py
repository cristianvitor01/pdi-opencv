# Realizar rotação sobre o um ponto da imagem definido
# pelo clique do mouse ao pressionar a tecla 'r'

import cv2
import numpy as np
from math import cos, sin, radians

img = cv2.imread('ifma-caxias.jpg')
image_direta = img.copy()
img_inversa = img.copy()
rows, cols = img.shape[:2]
x_angle, y_angle, raio = -1, -1, 0

angle = radians(raio)


def transform_direta():
    global x_angle, y_angle, image_direta, angle, img
    h, w, _ = image_direta.shape

    output = np.zeros(image_direta.shape, np.uint8)

    M = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [-int(w / 2), -int(h / 2), 1]
    ])

    M = np.dot(M, np.array([
        [cos(angle), sin(angle), 0],
        [-sin(angle), cos(angle), 0],
        [0, 0, 1]
    ]))

    M = np.dot(M, np.array([
        [1, 0, 0],
        [0, 1, 0],
        [int(w / 2), int(h / 2), 1]
    ]))

    for linha in range(h):
        for coluna in range(w):

            matriz_pixel = np.array([linha, coluna, 1])
            mult_pixel = np.dot(matriz_pixel, M)

            x_trans = int(mult_pixel[0])
            y_trans = int(mult_pixel[1])

            if (((h > x_trans) and (x_trans > 0)) and ((w > y_trans) and (y_trans > 0))):
                output[x_trans, y_trans] = image_direta[linha, coluna]

    image_direta = output


def transform_inversa():
    global x_angle, y_angle, img_inversa, angle, img
    h, w, _ = img_inversa.shape

    output = np.zeros(img_inversa.shape, np.uint8)

    M = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [-int(w / 2), -int(h / 2), 1]
    ])

    M = np.dot(M, np.array([
        [cos(angle), sin(angle), 0],
        [-sin(angle), cos(angle), 0],
        [0, 0, 1]
    ]))

    M = np.dot(M, np.array([
        [1, 0, 0],
        [0, 1, 0],
        [int(w / 2), int(h / 2), 1]
    ]))

    M = np.linalg.inv(M)

    for linha in range(h):
        for coluna in range(w):

            matriz_pixel = np.array([linha, coluna, 1])
            mult_pixel = np.dot(matriz_pixel, M)

            x_trans = int(mult_pixel[0])
            y_trans = int(mult_pixel[1])

            if (((h > x_trans) and (x_trans > 0)) and ((w > y_trans) and (y_trans > 0))):
                output[linha, coluna] = img[x_trans, y_trans]

    img_inversa = output


while 1:

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    if cv2.waitKey(30) & 0xFF == ord('r'):
        raio += 5
        print("APE")
        angle = radians(raio)
        transform_inversa()
        transform_direta()

    cv2.imshow('Rotation Right', image_direta)

    cv2.imshow('Rotation inverse', img_inversa)

cv2.destroyAllWindows()
