# Aplicar os operadores de Top Hat e Black Hat para
# destacar caracteres

import cv2
import numpy as np

img = cv2.imread('ifma-caxias.png', 0)

rectKernel=cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5)) # 13x5
res=cv2.morphologyEx(img, cv2.MORPH_TOPHAT, rectKernel) # Top Hat

cv2.imshow('Result',res)

cv2.waitKey(0)
cv2.destroyAllWindows()