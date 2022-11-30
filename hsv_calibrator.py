import cv2 as cv
import numpy as np
from time import sleep

def nothing(x) :
    pass

def track(hsv_low, hsv_high) :
    hsv_low[0]=cv.getTrackbarPos("H_low","HSV")
    hsv_low[1]=cv.getTrackbarPos("S_low","HSV")
    hsv_low[2]=cv.getTrackbarPos("V_low","HSV")
    hsv_high[0]=cv.getTrackbarPos("H_high","HSV")
    hsv_high[1]=cv.getTrackbarPos("S_high","HSV")
    hsv_high[2]=cv.getTrackbarPos("V_high","HSV")

def camera_track() :

    hsv_low=[0, 0, 0]
    hsv_high=[179, 255, 255]
    cap = cv.VideoCapture(0)

    cv.namedWindow("HSV")
    cv.createTrackbar("H_high","HSV",0,179,nothing)
    cv.setTrackbarPos("H_high","HSV",hsv_high[0])
    cv.createTrackbar("S_high","HSV",0,255,nothing)
    cv.setTrackbarPos("S_high","HSV",hsv_high[1])
    cv.createTrackbar("V_high","HSV",0,255,nothing)
    cv.setTrackbarPos("V_high","HSV",hsv_high[2])

    cv.createTrackbar("H_low","HSV",0,179,nothing)
    cv.setTrackbarPos("H_low","HSV",hsv_low[0])
    cv.createTrackbar("S_low","HSV",0,255,nothing)
    cv.setTrackbarPos("S_low","HSV",hsv_low[1])
    cv.createTrackbar("V_low","HSV",0,255,nothing)
    cv.setTrackbarPos("V_low","HSV",hsv_low[2])

    while True :
        boolean, frame = cap.read()
        if (boolean==1) :
            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            track(hsv_low, hsv_high)
            hsv_l = np.array(hsv_low)
            hsv_h = np.array(hsv_high)
            mask = cv.inRange(hsv, hsv_l, hsv_h)
            (contours, _) = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
            if len(contours)>0 :
                area = [cv.contourArea(cnt) for cnt in contours]
                print('h,s,v low', hsv_l)
                print('h,s,v high', hsv_h)
            
            cv.putText(frame, "C", (240, 320), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            cv.imshow("HSV",mask)
            cv.imshow('cal_now',frame)
            sleep(0.01)
            key = cv.waitKey(1)
            if (key == 27) :
                break
            elif (key == ord('q')) :
                print("PAUSE>>press Q to continue")
                while True :
                    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
                    track(hsv_low, hsv_high)
                    hsv_l = np.array(hsv_low)
                    hsv_h = np.array(hsv_high)
                    mask = cv.inRange(hsv, hsv_l, hsv_h)
                    cv.imshow("HSV",mask)
            
                    sleep(0.1)
                    key = cv.waitKey(1)
                    if (key == ord('q')) :
                        break
        else :
            print('Cannot open video_result .avi')
            break
        
    cap.release()
    cv.destroyAllWindows()

while True :
    camera_track()
    nx = int(input("Calibration again ? (1/0)"))
    if (nx==0) :
        break
