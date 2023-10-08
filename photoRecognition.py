import face_recognition
import cv2

# Tanıdık yüzlerin adlarını ve yüz kodlarını tanımlayın
known_face_names = ["","",""]  # Tanıdık yüzlerin adlarını burada değiştirin
known_face_encodings = []  # Tanıdık yüzlerin kodlarını burada saklayacağız

# Her tanıdık yüz için bir kod ekleyin
for name in known_face_names:
    image = face_recognition.load_image_file(name + ".jpg")
    encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(encoding)

# Kamerayı başlatın
video_capture = cv2.VideoCapture(0)

while True:
    # Kameradan bir frame alın
    ret, frame = video_capture.read()

    # Frame üzerinde yüz tanıma yapın
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # Bu yüzü tanıyabilir miyiz?
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Bilinmiyor"

        # Eğer tanıdık bir yüz bulursak, adını alın
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        face_names.append(name)

    # Yüzleri çerçeveye çiz
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Yüzü çerçeve etrafına çiz
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Adı çerçeve üzerine yaz
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Görüntüyü göster
    cv2.imshow('Video', frame)

    # Çıkış için 'q' tuşuna basmayı bekleyin
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı ve pencereyi kapat
video_capture.release()
cv2.destroyAllWindows()
