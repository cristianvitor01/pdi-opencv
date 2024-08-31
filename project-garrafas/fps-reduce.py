import cv2

# Carregar o vídeo original
video_path = 'garrafas.mp4'
cap = cv2.VideoCapture(video_path)

# Obter o FPS original do vídeo
original_fps = cap.get(cv2.CAP_PROP_FPS)
print(f"FPS Original: {original_fps}")

# Defina o novo FPS desejado
new_fps = 10  # Por exemplo, 10 FPS

# Obter largura, altura e o codec do vídeo original
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec para salvar o vídeo (MP4)

# Defina o caminho para salvar o novo vídeo
output_path = 'video_com_fps_reduzido.mp4'
out = cv2.VideoWriter(output_path, fourcc, new_fps, (width, height))

frame_interval = int(original_fps / new_fps)  # Intervalo de frames a serem pulados

frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Salva o frame a cada 'frame_interval' frames
    if frame_count % frame_interval == 0:
        out.write(frame)

    frame_count += 1

# Liberar recursos
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Vídeo com FPS reduzido salvo como: {output_path}")
