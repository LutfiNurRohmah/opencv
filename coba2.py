import cv2
import numpy
import time

cap = cv2.VideoCapture(0)
hsvLow = numpy.array([0, 95, 255])
hsvHigh = numpy.array([179, 229, 255])

while True:
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, hsvLow, hsvHigh)
    contours, _ = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        #print(area)
        if(area > 1000):
            cv2.drawContours(frame, contour, -1, (255, 0, 0), 2)
            #cari banyak sudut
            sudut = len(cv2.approxPolyDP(contour, 0.02*cv2.arcLength(contour, True), True))  #nyari banyak sudut
            print(sudut)
            cv2.putText(frame, str(sudut), (200, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
            # time.sleep(1)

    cv2.imshow("Frame", frame)
    cv2.imshow("hsv", mask)

    if(cv2.waitKey(1) & 0xFF == 27):
        break

#cv2.release()
cv2.destroyAllWindows()