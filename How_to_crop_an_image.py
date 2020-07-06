# How to resize a image

# Importing the library 
import cv2
import numpy as np
print("Library Imported")

# Reading the image 
img = cv2.imread("Resources/Lena.jpg") 

# Cropping the image
imgCropped = img[100:400, 100:400]
# Here we consider the image as a matrix of size (512,512)
# And simply define a new matrix of required elements and show the image

# Showing the Image
cv2.imshow('Image', img)
# Showing the Cropped Image
cv2.imshow('Cropped Image', imgCropped)

cv2.waitKey(0)