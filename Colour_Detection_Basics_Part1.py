# Colour Detection Basics

# Import Libraries
import cv2
import numpy as np 
print('Libraries Imported')

# Defining a function for creating Trackbars which actually does nothing
def empty(a):
    pass

# Creating a New Window for Trackbars 
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)

# Creating Trackbars 
# Here there is a requirement to call the function so we are calling an empty function
cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Trackbars", 179, 179, empty)       
cv2.createTrackbar("Sat Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "Trackbars", 255, 255, empty)
cv2.createTrackbar("Val Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Val Max", "Trackbars", 255, 255, empty)

while True:

    # Importing Images
    img = cv2.imread("Resources/lambo.png")
    # Converting it to HSV
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Reading the values from Trackbar
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    # Showing The Image 
    cv2.imshow("Image", img)
    cv2.imshow("HSV Image", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Img Result", imgResult)

    cv2.waitKey(1)


# My Result = 6, 20 ,91 255, 117, 255