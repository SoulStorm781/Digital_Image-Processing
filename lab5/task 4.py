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


def local_equalization(img, window_size=9):
    img_padded = np.pad(img, ((1, 1), (1, 1)), mode='constant')

    img_eq = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            window = img_padded[i:i+window_size, j:j+window_size]
            window_eq = global_equalization(window)
            img_eq[i, j] = window_eq[1, 1]

    return img_eq


img = cv.imread('SEM.jpg', cv.IMREAD_GRAYSCALE)
img_global_eq = global_equalization(img)
img_local_eq = local_equalization(img)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].imshow(img_global_eq, cmap='gray')
axes[0].set_title('Global Histogram Equalization')
axes[1].imshow(img_local_eq, cmap='gray')
axes[1].set_title('Local Histogram Equalization')
for ax in axes:
    ax.axis('off')
# plt.show()
plt.savefig('SEM Optimized.jpg')