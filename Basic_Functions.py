# This code is for different basic functions

# Importing Library 
import cv2
print("Library Imported")

# Reading the Image
img = cv2.imread("Resources/Lena.jpg") 

# To Convert the image from BGR scale to Gray Scale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# To Blur the Image
blurImg = cv2.GaussianBlur(imgGray, (7,7), 0)
# Edge Detector 
imgCanny = cv2.Canny(img, 100, 100)

# Showiing the converted image
cv2.imshow("Gray Scale Imae", imgGray)
# Showing the Blurred Image 
cv2.imshow("Blurred Image", blurImg)
# Showing the Edged Image
cv2.imshow("Edged Image", imgCanny)

cv2.waitKey(0)