# Utilize os conhecimentos de seguimentação de imagens para identificar o círculo e pintar de vermelho
# edges = cv2.Canny(gray, 100, 200)

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Original.png', 0)
