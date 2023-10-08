# Object_Recognition
Identification of objects via computer camera

Bu proje YOLO kullanılarak hazırlanmıştır. Kullanıcının kullanmak istediği veri kümesi ve cfg dosyası bu bağlantıdandır: "https://pjreddie.com/darknet/yolo/" proje dizininin bulunduğu konuma indirilmesi gerekiyor.

Kullanıcının bunu yaptıktan sonra main.py kodunda yer alan "net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")" satırı indirdiği veri kümesinin ve cfg dosyasının ismini burada vermesi gerekir. 

Daha sonra kullanıcı "coco.names" dosyasının tam yolunu burada vermesi gerekir: 
  "with open("../../../coco.names", "r") as f:"

Bunlar yapıldıysa kod çalışmak için hazır!!

======================================================================================================================================================

                ;'-. 
    `;-._        )  '---.._
      >  `-.__.-'          `'.__
     /_.-'-._         _,   ^ ---)
...  `       `'------/_.'----```
                     `

======================================================================================================================================================
# photoRecognition 

Bu uygulama için gereklilikler kod içerisinde verilmiştir. Kullanıcının yapması gereken tek şey projenin bulunduğu dizine "isim + jpg" olacak şekilde fotoğraf yerleştirmesidir (Örnek: 'ahmet.jpg'). Fotoğraf yerleştirildikten sonra kodda yer alan: "known_face_names = ["","",""]" bölümüne fotoğrafın ismi eklenmelidir (Örnek olarak 3 adet fotoğrafımız olsun. Bu fotoğrafların ismi "ahmet.jpg", "fatma.jpg", "ali.jpg" olsun. Kodumuza şu şekilde güncelleme yapmamız gerekir: 'known_face_names = ["ahmet","fatma","ali"]')

Bunu yaptıktan sonra uygulama çalışmaya hazır hale gelecektir. 
