import numpy as np
import cv2 as cv

img = cv.imread('newton.png', 0)
# task 3
y = img/255
PowerLaw1 = np.uint8(255*(y ** 0.2))
PowerLaw2 = np.uint8(255*(y ** 0.5))
PowerLaw3 = np.uint8(255*(y ** 1.2))
PowerLaw4 = np.uint8(255*(y ** 1.8))
cv.imshow('0.2', PowerLaw1)
cv.imshow('0.5', PowerLaw2)
cv.imshow('1.2', PowerLaw3)
cv.imshow('1.5', PowerLaw3)
cv.waitKey()
cv.destroyAllWindows()
