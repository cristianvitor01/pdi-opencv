import cv2

img = cv2.imread('opencv_low.png')

w,h=(int(10*img.shape[0]), int(10*img.shape[1])) # 10x aumentando a imagem

res1 = cv2.resize(img,(h,w), interpolation = cv2.INTER_CUBIC) # aplicando o método de interpolação cúbica
res2 = cv2.resize(img,(h,w), interpolation = cv2.INTER_NEAREST) # aplicando o método de interpolação mais próximo

cv2.imshow('res1',res1)
cv2.imshow('res2',res2)

cv2.waitKey(0)
cv2.destroyAllWindows()