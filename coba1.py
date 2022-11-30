import cv2

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.circle(gray, (50, 50), 10, (0, 0, 255), 2)
    cv2.rectangle(gray, (100, 100), (300, 300), (255, 0, 0), 1)
    cv2.line(frame, (300, 300), (500, 300), (0, 255, 0), 2)
    cv2.line(frame, (300, 300), (300, 400), (0, 255, 0), 2)
    cv2.line(frame, (300, 300), (500, 400), (0, 255, 0), 2)
    cv2.imshow("Camera", frame)
    cv2.imshow("abu-abu", gray)
    if(cv2.waitKey(1) & 0xFF == 27):
        break

cap.release()
cv2.destroyAllWindows()
