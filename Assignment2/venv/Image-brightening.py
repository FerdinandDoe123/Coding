#Import all necessary libraries
import cv2
import numpy as np

#Load original image
imagedata_brt = cv2.imread('dog.jpg')
cv2.imshow("Original", imagedata_brt)

#Matrix of ones which is multiplied by a scalar value of 60, matrix has dimensions same as our input image
Intensity_Matrix = np.ones(imagedata_brt.shape,  dtype = "uint8") * 90

#Print intensity Matrix
print(Intensity_Matrix)

#Add intensity matrix to imput image in order to increase the brightness
brightened_image = cv2.add(imagedata_brt, Intensity_Matrix)
cv2.imshow("Bright", brightened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

