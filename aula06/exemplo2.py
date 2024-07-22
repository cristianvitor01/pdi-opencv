import cv2
import numpy as np

img = cv2.imread('ifma-caxias.jpg')

rows, cols = img.shape[:2]  # rows = altura, cols = largura

M = np.float32([[1, 0, 100], [0, 1, 50]])  # matriz de translação
M = cv2.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 90, 1)  # matriz de rotação

pts1 = [[50, 50], [200, 50], [50, 200]]  # pontos de origem
pts2 = [[10, 100], [200, 50], [100, 250]]
M = cv2.getAffineTransform(np.float32(pts1), np.float32(pts2)) # matriz de transformação afim

res = cv2.warpAffine(img, M, (cols, rows)) # aplicando a transformação

# pts1 = [[200,100],[400,100],[50,400],[550,400]]
# pts2 = [[0,0],[300,0],[0,300],[300,300]]
# M = cv2.getPerspectiveTransform(np.float32(pts1),np.float32(pts2))
# res = cv2.warpPerspective(img,M,(300,300))

# for pt in pts1:
#     cv2.circle(img,pt,5,(0,0,255),-1)

# for pt in pts2:
#     cv2.circle(res,pt,5,(0,0,255),-1)

cv2.imshow('img', img)
cv2.imshow('res', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
