import cv2

img = cv2.imread('logo-if.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # converte a imagem para o espaço de cores HSV

# HSV -> Hue, Saturation, Value (3 canais de dados)

rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)  # converte a imagem de volta para o espaço de cores RGB

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converte a imagem para tons de cinza (apenas 1 canal de dados)

cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem HSV', hsv)
cv2.imshow('Imagem RGB', rgb)
cv2.imshow('Imagem em Tons de Cinza', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()


