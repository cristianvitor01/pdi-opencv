# manipulação de arquivos e eventos

# processando videos

import cv2

capture = cv2.VideoCapture('video-teste.mp4')

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH) # obtendo a largura do frame
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT) # obtendo a altura do frame

print('WIDTH:', frame_width)
print('HEIGHT:', frame_height)

if not capture.isOpened():
    print('Erro ao abrir o arquivo de vídeo')
else:
    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:
            cv2.imshow('Video', frame)

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            cv2.imshow('Video em Tons de Cinza', gray)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            if cv2.waitKey(20) & 0xFF == ord('w'):
                print('Salvando frame...')
                cv2.imwrite('frame.png', frame)
                cv2.imwrite('frame-gray.png', gray)
        else:
            break

capture.release()
cv2.destroyAllWindows()

