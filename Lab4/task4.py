import numpy as np
import cv2 as cv

img = cv.imread('newton.png', 0)

# task 4
Sliced_image = img
Sliced_image[(Sliced_image > 100) & (Sliced_image < 200)] = 210
cv.imshow('Gray scale slicing', Sliced_image)
cv.waitKey()
cv.destroyAllWindows()