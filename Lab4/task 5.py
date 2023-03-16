import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('newton.png', 0)

# task 5
# Initialize the histogram
hist = [0] * 256

# Iterate through each pixel and update the histogram
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        intensity = img[i, j]
        hist[intensity] += 1

# Normalize the histogram
total_pixels = img.shape[0] * img.shape[1]
hist = [x / total_pixels for x in hist]

# Plot the histogram
# plt.plot(hist)
plt.bar(list(range(0, 256)), hist)
plt.title('Histogram of Ein Stein')
plt.xlabel('Intensity Value')
plt.ylabel('Number of Pixels')
plt.show()