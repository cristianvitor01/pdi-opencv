import cv2

img = cv2.imread('logo-if.png')

# exemplo de como uma imagem é acessada igual uma matriz

print(img[0, 0])
print(img[0, 8])
print(img[15,0])
