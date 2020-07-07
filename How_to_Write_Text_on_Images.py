# How to draw shapes on an empty image 

# Importing Libarary
import cv2
import numpy as np
print('Library Imported')

# Creating an empty matrix of size (512, 512) for creating a black empty image
img = np.zeros((512, 512, 3), np.uint8)
#img[:] = 255, 0, 0      To Give a specific colour to our image

# Putting a text on an image 
# cv2.putText(Image, Text, Starting point, Font, Scale, Coloue, Font Thickness)
cv2.putText(img, "Hello World", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)

# Showing the empty image
cv2.imshow("Image", img)

cv2.waitKey(0)
