# Descrição: Exemplo de uso de eventos do mouse com OpenCV. Cria pontos aleatórios coloridos na imagem ao usar o
# clique duplo do mouse.

from random import randint
import cv2

import numpy as np

BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)

COLORS = [BLUE, GREEN, RED, BLACK, GRAY]


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:  # evento de clique duplo
        c = randint(0, len(COLORS) - 1)  # sorteia uma cor
        cv2.circle(img, (x, y), 3, COLORS[c], -1)  # desenha um circulo preenchido


img = cv2.imread('logo-if.jpg')

cv2.namedWindow('Logo IF')

cv2.setMouseCallback('Logo IF', draw_circle)

# loop principal
while (1):
    cv2.imshow('Logo IF', img)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        cv2.imwrite('mouse.jpg', img)
        break
cv2.destroyAllWindows()
