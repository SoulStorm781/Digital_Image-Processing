import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math

# task 01 (a)
img = cv.imread('newton.png', 0)
img1 = - img

# task 01 (b)
my_max = np.max(img)
c = 255//np.log(1+my_max)
s = np.uint8(c * np.log((img+1)))

cv.imshow('original', img)
cv.imshow('Negative Transform', img1)
cv.imshow('Log Transform', s)
cv.waitKey()
cv.destroyAllWindows()













