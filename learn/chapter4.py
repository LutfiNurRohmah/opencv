import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img)
# img[:] =  255, 0, 0

cv2.line(img, (0, 0), (100, 300), (0, 255, 0), 3)
cv2.rectangle(img, (10, 10), (200, 250), (0,0,255), 2)
cv2.circle(img, (400, 100), 50, (255, 255, 0), 4)
cv2.putText(img, " OPENCV ", (300, 250), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 1)

cv2.imshow("Image", img)

cv2.waitKey(0)