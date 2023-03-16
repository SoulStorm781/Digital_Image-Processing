import cv2 as cv
import copy
import numpy as np
import matplotlib.pyplot as plt


def global_equalization(img):
    frequencies = np.zeros(256)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            frequencies[img[i, j]] += 1

    cdf = np.cumsum(frequencies)
    cdf = 255 * cdf / cdf[-1]  # scale CDF to 0-255 range
    tf = np.round(cdf).astype('uint8')

    img_eq = tf[img]

    return img_eq



def local_equalization(img, window_size=3):
    img_padded = np.pad(img, ((1, 1), (1, 1)), mode='constant')

    img_eq = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            window = img_padded[i:i+window_size, j:j+window_size]
            window_eq = global_equalization(window)
            img_eq[i, j] = window_eq[1, 1]

    return img_eq


img = cv.imread('boxes.jpg', cv.IMREAD_GRAYSCALE)
img_global_eq = global_equalization(img)
img_local_eq = local_equalization(img)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
# Plot the histograms
ax1.hist(img_global_eq.ravel(), bins=256, range=(0, 256))
ax1.set_title('Global Histogram Equalization')
ax1.set_xlim([0, 256])
ax1.set_ylim([0, 6000])
ax2.hist(img_local_eq.ravel(), bins=256, range=(0, 256))
ax2.set_title('Local Histogram Equalization')
ax2.set_xlim([0, 256])
ax2.set_ylim([0, 6000])
plt.savefig('histograms.jpg')
