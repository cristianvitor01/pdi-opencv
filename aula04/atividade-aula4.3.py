# ▪Aplique um efeito de ruído do tipo sal e pimenta em
# um arquivo de vídeo ou imagem da webcam, variando
# sua intensidade por comandos de teclado.

import cv2
import numpy as np
import random


def noise(image, prob):
    output = np.zeros(image.shape, np.uint8)  # Cria uma matriz de zeros com as mesmas dimensões da imagem
    thres = 1 - prob  # Calcula o limiar para a probabilidade
    # Percorre a imagem (matriz de pixels) e adiciona ruído
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()  # Gera um número aleatório entre 0 e 1
            if rdn < prob:  # Se o número aleatório for menor que a probabilidade
                output[i][j] = 0  # Adiciona ruído preto
            elif rdn > thres:  # Se o número aleatório for maior que o limiar
                output[i][j] = 255  # Adiciona ruído branco
            else:
                output[i][j] = image[i][j]  # Mantém o pixel original
    return output


capture = cv2.VideoCapture("video-teste.mp4")  # load video

noise_prob = 0.03  # prob inicial

while True:
    ret, frame = capture.read()
    if ret:
        cv2.imshow('Original', frame)

        noisy_frame = noise(frame, noise_prob)  # Adiciona ruído a cada frame
        cv2.imshow('Salt & Pepper', noisy_frame)

        # Verifica comandos de teclado
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break
        elif key == ord('+'):  # Aumenta a intensidade do ruído
            noise_prob = min(1.0, noise_prob + 0.01)  # Garante que a probabilidade esteja entre 0 e 1
            print("Intensidade do ruído aumentada para:", noise_prob)
        elif key == ord('-'):  # Diminui a intensidade do ruído
            noise_prob = max(0.0, noise_prob - 0.01)
            print("Intensidade do ruído diminuída para:", noise_prob)
    else:
        break

capture.release()
cv2.destroyAllWindows()
