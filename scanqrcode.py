import cv2

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    
    detect =cv2.QRCodeDetector()
    val, pts, st_code = detect.detectAndDecode(frame)
    
    print(val)
    cv2.putText(frame, str(val), (200, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
    
    cv2.imshow("Camera", frame)
    
    if(cv2.waitKey(1) & 0xFF == 27):
        break

cap.release()
cv2.destroyAllWindows()


