# How to resize a image

# Importing the library 
import cv2
import numpy as np
print("Library Imported")

# Reading the image 
img = cv2.imread("Resources/Lena.jpg") 

# Printing the image size
print(img.shape)
# Here in output you'll get a tuple of 3 parameters i.e. (Height, Width, Channels)

# Resizing the image
# Here we are passing a tuple as (Width, Height)
imgResize = cv2.resize(img, (300, 200))

# Showing the Image
cv2.imshow('Image', img)
# Showing the resized image
cv2.imshow('Resized Image', imgResize) 

cv2.waitKey(0)