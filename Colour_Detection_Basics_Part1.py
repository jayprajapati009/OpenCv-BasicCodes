# Colour Detection Basics

# Import Libraries
import cv2
import numpy as np 
print('Libraries Imported')

# Importing Images
img = cv2.imread("Resources/lambo.png")

# Showing The Image 
cv2.imshow("Image", img)

cv2.waitKey(0)