# How to Read 

#importing Library
import cv2 
print('Library Imported!')

# importing the image with defing the address
img = cv2.imread("Resources/Lena.jpg")

# Showing the image as in output
cv2.imshow("Output", img)
cv2.waitKey(0)

