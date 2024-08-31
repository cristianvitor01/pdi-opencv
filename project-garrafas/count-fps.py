import cv2

# Carregar o vídeo
video_path = 'video_com_fps_reduzido.mp4'
cap = cv2.VideoCapture(video_path)

frame_rate = cap.get(cv2.CAP_PROP_FPS)  # Obtenha a taxa de quadros do vídeo


print(frame_rate)