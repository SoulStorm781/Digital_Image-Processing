import cv2
import numpy as np

# Load the image
img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)
p5, p95 = np.percentile(img, (5, 95))

# Apply contrast stretching
img_rescaled = (img - p5) * (255 / (p95 - p5))
img_rescaled[img_rescaled < 0] = 0
img_rescaled[img_rescaled > 255] = 255
img_rescaled = np.uint8(img_rescaled)

# Display the original and the stretched images
cv2.imshow('Original', img)
cv2.imshow('Contrast Stretched', img_rescaled)
cv2.waitKey(0)
cv2.destroyAllWindows()
