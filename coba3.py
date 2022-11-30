import cv2
import numpy

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
        luas = [cv2.contourArea(contour) for contour in contours]
        idx = luas.index(max(luas))
        print(luas)
        # print(area)
        if(area > 1000):
            # cv2.drawContours(frame, contour, -1, (255, 0, 0), 2)
            (x, y), radius = cv2.minEnclosingCircle(contours[idx])
            cv2.circle(frame, (int(x), int(y)), 10, (0, 0, 255), 2)

    cv2.imshow("Frame", frame)
    cv2.imshow("hsv", mask)

    if(cv2.waitKey(1) & 0xFF == 27):
        break

#cv2.release()
cv2.destroyAllWindows()