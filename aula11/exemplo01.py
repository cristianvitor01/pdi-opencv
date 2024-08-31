import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Original.png', 0)

kernel = np.ones((7, 7), np.uint)

dilation = cv2.dilate(img, kernel, iterations=3)
erosion = cv2.erode(img, kernel, iterations=3)
# opening = cv2.morphologyEx(img_open, cv2.MORPH_OPEN, kernel)
grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

plt.subplot(221), plt.imshow(img)
plt.title('Imagem')
plt.subplot(222), plt.imshow(dilation)
plt.title('Dilation')
plt.subplot(223), plt.imshow(erosion)
plt.title('Erosion')
plt.subplot(224), plt.imshow(grad)
plt.title('Gradient')

plt.tight_layout()
plt.show()
