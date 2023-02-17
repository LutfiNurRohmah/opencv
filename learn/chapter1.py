import cv2

# ---read images
# img = cv2.imread("Resources/Lenna.png")
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# --import video and  video capture
# cap = cv2.VideoCapture("Resources/test_video.mp4")
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# --use webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640) #width
cap.set(4, 480) #height
cap.set(10, 100) #brightness
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
