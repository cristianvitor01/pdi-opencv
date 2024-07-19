import cv2

import numpy as np

BLUE = [255, 0, 0]
GREEN = [0, 255, 0]
RED = [0, 0, 255]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
GRAY = [128, 128, 128]

img = cv2.imread('logo-if.jpg')

cv2.line(img, (0, 0), (511, 511), BLUE, 2)  # desenha uma linha azul de 2px de largura
cv2.line(img, (200, 100), (200, 250), BLACK, 7)  # desenha uma linha preta de 7px de largura


cv2.rectangle(img, (250, 150), (300, 250), RED, 3)  # desenha um retangulo vermelho de 3px de largura

cv2.circle(img, (350, 200), 50, GREEN, -1)  # desenha um circulo verde preenchido

pts = np.array([(400, 270), (370, 234), (450, 85), (380, 10)], np.int32)  # pontos do poligono
cv2.polylines(img, [pts], True, GRAY, 3)  # desenha um poligono cinza de 3px de largura

cv2.putText(img, 'Texto1', (510, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, RED, 2,
            cv2.LINE_4)
cv2.putText(img, 'Texto2', (510, 70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, GREEN, 2,
            cv2.LINE_8)
cv2.putText(img, 'Texto3', (510, 110), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.9, BLUE, 2,
            cv2.LINE_AA)

cv2.imshow('Logo IF', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
