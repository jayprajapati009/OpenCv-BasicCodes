# How to Read Video

#importing Library
import cv2 
print('Library Imported!')

#Capturing Video Object
cap = cv2.VideoCapture("Resources/vtest.avi")

# Running a loop to display each frame of the video 
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
