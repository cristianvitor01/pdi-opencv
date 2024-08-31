import numpy as np
import cv2
import os
from pdf2image import convert_from_path


def identify_template(image):
    template_path = os.path.join(os.getcwd(), 'layouts')
    templates = os.listdir(template_path)
    cv2.setRNGSeed(2391)

    best_template = None
    max_matches = 0

    # Inicialize o detector SIFT
    sift = cv2.SIFT_create()

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Encontre os pontos-chave e descritores para a imagem de entrada
    kp_image, des_image = sift.detectAndCompute(image, None)

    # Inicialize o algoritmo FLANN
    flann = cv2.FlannBasedMatcher()

    for template_name in templates:
        template = np.array(convert_from_path(f"{template_path}/{template_name}", fmt='jpg')[0])
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        kp_template, des_template = sift.detectAndCompute(template, None)

        # Encontre as correspondências entre a imagem de entrada e o template
        matches = flann.knnMatch(des_image, des_template, k=2)

        # Aplique um limiar para selecionar correspondências de boa qualidade
        good_matches = [m for m, n in matches if m.distance < 0.12 * n.distance]

        # Atualize o melhor template se o número de correspondências for maior
        if len(good_matches) > max_matches:
            max_matches = len(good_matches)
            best_template = template_name

    return best_template


docs = os.getcwd() + '/docs'
docs = os.listdir(docs)
for x in docs:
    print(x)
    dic = identify_template(read_image(f"docs/{x}"))
    print(dic)
    print("****")