import cv2

img = cv2.imread('logo-if.png')

# exemplo para mostrar apenas uma determinada região de interesse da imagem

roi = img[0:50, 0:50]  # região de interesse
cv2.imshow('ROI', roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
