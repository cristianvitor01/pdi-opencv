"""
Utilizar o mouse para rabiscar sobre os frames de um
arquivo de vídeo conforme as especificações abaixo
- A tecla espaço deve limpar os rascunhos
- A tecla 'c' deve alterar a cor das marcações
- Todas os rascunhos e alterações devem ficar
    salvos em um outro arquivo de vídeo
"""

import cv2
import numpy as np
from random import randint

capture = cv2.VideoCapture('video-teste.mp4')

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)

COLORS = [BLUE, GREEN, RED, BLACK, GRAY]

cv2.namedWindow('Desenhar no video')

drawings = []  # lista para armazenar os rascunhos


def draw_circle(event, x, y, flags, param):
    global drawings
    if event == cv2.EVENT_LBUTTONDOWN:
        c = randint(0, len(COLORS) - 1)
        cv2.circle(frame, (x, y), 3, COLORS[c], -1)
        drawings.append((x, y, COLORS[c]))


cv2.setMouseCallback('Desenhar no video', draw_circle)

while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        for x, y, color in drawings:
            cv2.circle(frame, (x, y), 3, color, -1)

        cv2.imshow('Desenhar no video', frame)

        key = cv2.waitKey(20)
        if key & 0xFF == ord('q'):
            break
        elif key & 0xFF == ord(' '):  # limpa os rascunhos com a tecla espaço
            drawings = []

        if cv2.waitKey(20) & 0xFF == ord('w'):  # salvar rascunho (tecla w)
            print("Salvando rascunho...")
            fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
            output = cv2.VideoWriter("rascunho.mp4", fourcc, int(fps), (int(frame_width), int(frame_height)), False)
    else:
        break

capture.release()
cv2.destroyAllWindows()
