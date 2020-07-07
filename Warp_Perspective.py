# Importing Libarary
import cv2
import numpy as np
print('Library Imported')

# Reading the image
img = cv2.imread("Resources/cards.jpg")

# Defining the width and height 
width,height = 250,350
# Defining the points for the required image area
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
# Defining the points for the transformation
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# Converting the image in to the cropped image 
matrix = cv2.getPerspectiveTransform(pts1,pts2)
# Flattening the image
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
 
# Showing the image  
cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)