import cv2
import pyzbar.pyzbar as pyzbar

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()

    qr = pyzbar.decode(frame)
    for barcode in qr:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x+w, y+h),(0, 0, 255), 2)
        val = barcode.data.decode("utf-8")
        cv2.putText(frame, val, (100, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
        print(val)
        
    cv2.imshow("Camera", frame)
    
    if(cv2.waitKey(1) & 0xFF == 27):
        break


cap.release()
cv2.destroyAllWindows()


