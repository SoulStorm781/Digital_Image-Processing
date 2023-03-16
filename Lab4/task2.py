import numpy as np
import cv2 as cv

img = cv.imread('newton.png', 0)
# task 2
my_mean = np.mean(img)
lower = my_mean-20
upper = my_mean+20
img_a = ((img > my_mean).astype(np.uint8)) * 255
img_b = ((img < my_mean).astype(np.uint8))*255
img_c = img
img_c[(img_c < lower) | (img_c > upper)] = 255
img_c[(img_c > lower) & (img_c < upper)] = 0
cv.imshow('Greater T Mean', img_a)
cv.imshow('Less T Mean', img_b)
cv.imshow('Others', img_c)
cv.waitKey()
cv.destroyAllWindows()