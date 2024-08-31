import cv2

# Carregar o vídeo
video_path = 'video_com_fps_reduzido.mp4'
cap = cv2.VideoCapture(video_path)

frame_rate = cap.get(cv2.CAP_PROP_FPS)  # Obtenha a taxa de quadros do vídeo
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Salvar cada frame como uma imagem
    frame_name = f'frame_{frame_count}.jpg'
    cv2.imwrite(frame_name, frame)

    # Exibir o frame (opcional)
    # cv2.imshow('Frame', frame)

    frame_count += 1

    # Pule para o próximo frame desejado
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_count)

    # Para pausar e fechar ao pressionar 'q' (opcional)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
