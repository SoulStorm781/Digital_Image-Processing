from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = Image.open("input.png")

gray_img = img.convert("L")

img_arr = np.array(gray_img)
# Create an array to store the histogram
hist = np.zeros(256, dtype=int)

for i in range(img_arr.shape[0]):
    for j in range(img_arr.shape[1]):
        hist[img_arr[i, j]] += 1

# Plot the histogram
plt.bar(range(256), hist)
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.title("Histogram of Image")
# plt.show()
plt.savefig("Figure_1.jpg")
cum_hist = np.cumsum(hist)
norm_cum_hist = cum_hist / (img_arr.shape[0] * img_arr.shape[1])

new_vals = np.round(norm_cum_hist * 255)
eq_img_arr = np.zeros_like(img_arr)
for i in range(img_arr.shape[0]):
    for j in range(img_arr.shape[1]):
        eq_img_arr[i, j] = new_vals[img_arr[i, j]]
eq_img = Image.fromarray(eq_img_arr)
# Save the output image
eq_img.save("hist_input.jpg")


# -------------task 2 b
# Calculate the PDF
pdf = hist / (img_arr.shape[0] * img_arr.shape[1])
# Plot the PDF
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(range(256), pdf)
ax.set_xlabel("Pixel Value")
ax.set_ylabel("PDF")
ax.set_title("Probability Density Function of Image")
# Save the PDF as Figure_2.jpg
fig.savefig("Figure_2.jpg")

# ---------- task 2 c---------
# Calculate the CDF
cdf = np.cumsum(pdf)
# Plot the CDF
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(range(256), cdf)
ax.set_xlabel("Pixel Value")
ax.set_ylabel("CDF")
ax.set_title("Cumulative Density Function of Image")
# Save the CDF as Figure_3.jpg
fig.savefig("Figure_3.jpg")

# ---------- task 2 d---------
trans_func = pdf * 255
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(range(256), trans_func)
ax.set_xlabel("Pixel Value")
ax.set_ylabel("Transformed Pixel Value")
ax.set_title("Transformation Function of Image")
# Save the transformation function as Figure_4.jpg
fig.savefig("Figure_4.jpg")

# ---------- task 2 e---------
eq_img_arr = np.zeros_like(img_arr)
for i in range(img_arr.shape[0]):
    for j in range(img_arr.shape[1]):
        eq_img_arr[i, j] = trans_func[img_arr[i, j]]
eq_img = Image.fromarray(eq_img_arr)
# Save the contrast-enhanced image as Figure_5.jpg
eq_img.save("Figure_5.jpg")

# ---------- task 2 f---------
eq_img = Image.open("Figure_5.jpg")
eq_img_arr = np.array(eq_img)
# Create an array to store the histogram
eq_hist = np.zeros(256, dtype=int)

for i in range(eq_img_arr.shape[0]):
    for j in range(eq_img_arr.shape[1]):
        eq_hist[eq_img_arr[i, j]] += 1


fig, ax = plt.subplots()
# Plot the histogram
ax.bar(np.arange(256), eq_hist)
ax.set_xlim([0, 255])
ax.set_ylim([0, np.max(eq_hist)*1.1])
plt.savefig("Figure_6.jpg")


