# This code is for different basic functions

# Importing Library 
import cv2
import numpy as np
print("Library Imported")

# Reading the Image
img = cv2.imread("Resources/Lena.jpg") 

# To Convert the image from BGR scale to Gray Scale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# To Blur the Image
blurImg = cv2.GaussianBlur(imgGray, (7,7), 0)
# Edge Detector 
imgCanny = cv2.Canny(img, 100, 100)
# To reduce the edges
imgCanny2 = cv2.Canny(img, 150, 200)
# To dilate Image (Edges becomes Thick)
# A kernel is a matrix to define the image
kernel = np.ones((5, 5),np.uint8)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# To Erode image (Edges becomes thin)
imgErode = cv2.erode(imgDilation, kernel, iterations=1)

# Showiing the converted image
cv2.imshow("Gray Scale Imae", imgGray)
# Showing the Blurred Image 
cv2.imshow("Blurred Image", blurImg)
# Showing the Edged Image
cv2.imshow("Edged Image", imgCanny)
# Showing the second Edged Image
cv2.imshow("Reduced Edge Image", imgCanny2)
# Showing Dilated Image
cv2.imshow("Dilated Image", imgDilation)
# Showing the eroded image
cv2.imshow("Eroded Image", imgErode)

cv2.waitKey(0)