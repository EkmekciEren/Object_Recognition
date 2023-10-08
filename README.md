# Object_Recognition
Identification of objects via computer camera

Bu proje YOLO kullanılarak hazırlanmıştır. Kullanıcının kullanmak istediği veri kümesi ve cfg dosyası bu bağlantıdandır: "https://pjreddie.com/darknet/yolo/" proje dizininin bulunduğu konuma indirilmesi gerekiyor.

Kullanıcının bunu yaptıktan sonra main.py kodunda yer alan "net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")" satırı indirdiği veri kümesinin ve cfg dosyasının ismini burada vermesi gerekir. 

Daha sonra kullanıcı "coco.names" dosyasının tam yolunu burada vermesi gerekir: 
  "with open("../../../coco.names", "r") as f:"

Bunlar yapıldıysa kod çalışmak için hazır!!
