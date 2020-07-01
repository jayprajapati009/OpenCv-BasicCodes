# How to read Webcam

#importing Library
import cv2 
print('Library Imported!')

#Capturing Video Object
# 0 is ID for the default webcam for external you can try 1 or 2 
cap = cv2.VideoCapture(0)

# Here you can set the height and width of your frame 
cap.set(3, 640)     # 3 id the ID for width
cap.set(4, 480)     # 4 id the ID for Height
cap.set(10, 100)    # 10 id the ID for brightness     

# Running a loop to display each frame of the video 
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break