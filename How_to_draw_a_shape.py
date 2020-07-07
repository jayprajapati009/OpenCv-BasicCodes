# How to draw shapes on an empty image 

# Importing Libarary
import cv2
import numpy as np
print('Library Imported')

# Creating an empty matrix of size (512, 512) for creating a black empty image
img = np.zeros((512, 512, 3), np.uint8)
#img[:] = 255, 0, 0      To Give a specific colour to our image

# Creating a line 
# cv2.line(Image, Start Point, End Point, Colour, Thickness)
cv2.line(img, (0, 0), (300, 300), (0, 255, 0), 1)

# Creating a Rectangle
# cv2.line(Image, Diagonally Starting point, Diagonally End Point, Colour, Thickness)
cv2.rectangle(img, (0, 0), (400, 400), (255, 0, 0), 1)

# Creating a filled rectangle
cv2.rectangle(img, (450, 420), (500, 500), (0, 0, 255), cv2.FILLED)

# Creating a circle 
# cv2.line(Image, Centre, Radius, Colour, Thickness)
cv2.circle(img, (450, 50), 30,(255, 0, 0), 2)

# Showing the empty image
cv2.imshow("Image", img)

cv2.waitKey(0)
