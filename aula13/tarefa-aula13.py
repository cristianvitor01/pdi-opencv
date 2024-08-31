import cv2

# Carregar os vídeos e classificadores de faces
cap = cv2.VideoCapture('ifma-caxias.mp4')

face_cascade1 = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade2 = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
face_cascade3 = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

total_faces = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar faces usando os 3 classificadores
    faces1 = face_cascade1.detectMultiScale(gray, 1.3, 5)
    faces2 = face_cascade2.detectMultiScale(gray, 1.3, 5)
    faces3 = face_cascade3.detectMultiScale(gray, 1.3, 5)

    # Juntar as detecções de todos os classificadores
    all_faces = set(tuple(f) for f in faces1) | set(tuple(f) for f in faces2) | set(tuple(f) for f in faces3)

    total_faces += len(all_faces)

    for (x, y, w, h) in all_faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Desenhar um retângulo

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(f'Total de faces detectadas: {total_faces}')

cap.release()
cv2.destroyAllWindows()
