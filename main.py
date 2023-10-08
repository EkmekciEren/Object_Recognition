import cv2
import numpy as np
import concurrent.futures

# Nesne tanıma işlemini gerçekleştiren fonksiyon
def detect_objects(frame, net, classes):
    # Görüntü ayarı 640x480 px 
    frame = cv2.resize(frame, (640, 480))
    
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(net.getUnconnectedOutLayersNames())

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:  # Belirli bir güven eşiği ayarı
                center_x = int(detection[0] * frame.shape[1])
                center_y = int(detection[1] * frame.shape[0])
                width = int(detection[2] * frame.shape[1])
                height = int(detection[3] * frame.shape[0])

                x = int(center_x - width / 2)
                y = int(center_y - height / 2)

                # Kare çizimi 
                cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)

                # Nesne adı 
                label = f"{classes[class_id]} ({confidence:.2f})"
                cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame

# Model ve sınıf etiketi
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
# Burada coco.names dosyasının tam yolu verilmelidir.
with open("/Users/erenekmekci/Desktop/everythink/face_recog/nesneTanıma/coco.names", "r") as f:
    classes = f.read().strip().split("\n")

# Kamera girişi
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Kamera yakalama ve nesne tanıma işlemlerinin paralel olarak yapılması
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(detect_objects, frame, net, classes)
        processed_frame = future.result()

    # Görüntüyü çıktılama
    cv2.imshow("Nesne Tanıma", processed_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Temizlik ve kamerayı kapatma
cap.release()
cv2.destroyAllWindows()
