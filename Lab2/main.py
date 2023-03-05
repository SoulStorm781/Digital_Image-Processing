import numpy as np
import cv2


# task 1
# def padded(size, pad):
#     # Create a 2D NumPy array of size (pad + size + pad, pad + size + pad) with all ones of type uint8
#     ones = np.ones((pad + size + pad, pad + size + pad), dtype=np.uint8)
#
#     # Set the values in the first 2*pad rows to zero
#     ones[0:2 * pad, :] = 0
#     # Set the values in the last size rows to zero
#     ones[size:, :] = 0
#     # Set the values in the first 2*pad columns to zero
#     ones[:, 0:2 * pad] = 0
#     # Set the values in the last size columns to zero
#     ones[:, size:] = 0
#     cv2.imshow('ones', ones * 255)
#     # Wait for a key event
#     cv2.waitKey()
#
#
# # Ask the user to input the value of size and pad
# size = input("enter the value of ones: ")
# size = int(size)
# pad = input("enter the value of pad: ")
# pad = int(pad)
# # Call the padded function with the user-provided values
# padded(size, pad)

# home

# def padded(size, pad, choice):
#     if choice == 'square':
#      # Create a 2D NumPy array of size (pad + size + pad, pad + size + pad) with all ones of type uint8
#      ones = np.ones((pad + size + pad, pad + size + pad), dtype=np.uint8)
#
#      # Set the values in the first 2*pad rows to zero
#      ones[0:2 * pad, :] = 0
#         # Set the values in the last size rows to zero
#      ones[size:, :] = 0
#      # Set the values in the first 2*pad columns to zero
#      ones[:, 0:2 * pad] = 0
#      # Set the values in the last size columns to zero
#      ones[:, size:] = 0
#      cv2.imshow('ones', ones * 255)
#      # Wait for a key event
#      cv2.waitKey()
#
#
#     elif choice == 'corners':
#      # create an array of ones with 3 color channels and multiply by 255 to get white pixels
#         ones = np.ones((size, size, 3), dtype=np.uint8)*255
#         ones[0:pad, 0:pad, ] = [0, 0, 0]  # set the color of the top left corner
#         ones[0:pad, size-pad:size] = [0, 0, 0]  # set the color of the top right corner
#         ones[size-pad:size, 0:pad] = [0, 0, 0]  # set the color of the bottom left corner
#         ones[size-pad:size, size-pad:size] = [0, 0, 0]  # set the color of the bottom right corner
#         cv2.imshow('colored', ones)  # display the resulting image
#         cv2.waitKey()
#
#
# # Ask the user to input the value of size and pad
# size = input("enter the value of ones: ")
# size = int(size)
# pad = input("enter the value of pad: ")
# pad = int(pad)
# choice = input('square or corners: ')
# # Call the padded function with the user-provided values
# padded(size, pad, choice)


# task 3
# def colored(size, pad):
#     # create an array of ones with 3 color channels and multiply by 255 to get white pixels
#     ones = np.ones((size, size, 3), dtype=np.uint8)*255
#     ones[0:pad, 0:pad, ] = [0, 0, 255]  # set the color of the top left corner
#     ones[0:pad, size-pad:size] = [255, 0, 0]  # set the color of the top right corner
#     ones[size-pad:size, 0:pad] = [0, 255, 0]  # set the color of the bottom left corner
#     ones[size-pad:size, size-pad:size] = [0, 0, 0]  # set the color of the bottom right corner
#     cv2.imshow('colored', ones)  # display the resulting image
#     cv2.waitKey()
#
#
# size = input("enter the size of ones: ")
# size = int(size)
# pad = size//8
# pad = int(pad)
# colored(size, pad)


# # task 4
# img = cv2.imread('img1.jpg', -1)
# org_img1 = cv2.resize(img, (400, 400), interpolation=cv2.INTER_LINEAR)
# img1 = cv2.resize(img, (400, 400), interpolation=cv2.INTER_LINEAR)
# img2 = cv2.resize(img, (400, 400), interpolation=cv2.INTER_LINEAR)
# img3 = cv2.resize(img, (400, 400), interpolation=cv2.INTER_LINEAR)
#
# height = img1.shape[0]
# width = img2.shape[1]
#
# height1 = img3.shape[0]
# width1 = img3.shape[1]
# # vertical
# for i in range(height // 2):
#     temp = img1[i].copy()
#     img1[i] = img1[height - i - 1]
#     img1[height - i - 1] = temp
#
# # horizontal
# for j in range(width // 2):
#     temp1 = img2[:, j].copy()
#     img2[:, j] = img2[:, width - j - 1]
#     img2[:, width - j - 1] = temp1
#
# # both
# for i in range(height1 // 2):
#     temp_1 = img3[i].copy()
#     img3[i] = img3[height1 - i - 1]
#     img3[height1 - i - 1] = temp_1
# for j in range(width1 // 2):
#     temp_2 = img3[:, j].copy()
#     img3[:, j] = img3[:, width - j - 1]
#     img3[:, width - j - 1] = temp_2
#
# cv2.imshow('test image', org_img1)
# cv2.imshow('vertical', img1)
# cv2.imshow('horizontal', img2)
# cv2.imshow('both', img3)
# cv2.waitKey()

# task 5
# img = cv2.imread('img1.jpg', -1)
# org_img1 = cv2.resize(img, (400, 400), interpolation=cv2.INTER_LINEAR)
# img1 = cv2.resize(img, (400, 400), interpolation=cv2.INTER_LINEAR)
#
# height = img1.shape[0]
# # mirror
# for i in range(height // 2):
#     temp = img1[i].copy()
#     img1[height - i - 1] = temp
#
# cv2.imshow('test image', org_img1)
# cv2.imshow('mirror', img1)
# cv2.waitKey()


# # task 7
# def decimate(image):
#     x = int(image.shape[0] / 4)  # divide image height by 4
#     y = int(image.shape[1] / 4)  # divide image height by 4
#     one = np.ones((x, y), np.uint8)
#     for i in range(0, image.shape[0], 4):  # iterate over the image height in steps of 4
#         for j in range(0, image.shape[1], 4):  # iterate over the image width in steps of 4
#             one[int(i / 4)][int(j / 4)] = int(image[i][j])  # assign pixel values of the image to the new matrix at a reduced resolution
#     return one
#
#
# def resize(image):
#     x = int(image.shape[0] * 4)  # multiply image width by 4
#     y = int(image.shape[1] * 4)  # multiply image width by 4
#     one = np.ones((x, y), np.uint8)  # create a new matrix of shape (x, y) with all elements initialized to 1
#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             one[4 * i:4 * (i + 1), 4 * j:4 * (j + 1)] = image[i, j]
#
#     return one
#
#
# img = cv2.imread('testimg.jpg', 0)  # read the image as grayscale
# cv2.imshow('Original', img)
# decimated = decimate(img)
# cv2.imshow('Decimated', decimated)
# resized = resize(img)
# cv2.imshow('Resized', resized)
# cv2.waitKey(0)


# task 2
# def conversion(image, level):
#     rows = image.shape[0]
#     column = image.shape[1]
#     # Check the level of gray scale required and set the values accordingly
#     if level == 2:
#         # For binary gray scale level
#         for i in range(rows):
#             for j in range(column):
#                 if image[i][j] >= 0 and image[i][j] <= 128:
#                     image[i][j] = 0
#                 else:
#                     image[i][j] = 255
#     elif level == 4:
#         # For 4-level gray scale
#         for i in range(rows):
#             for j in range(column):
#                 if image[i][j] >= 0 and image[i][j] <= 64:
#                     image[i][j] = 0
#                 elif image[i][j] >= 64 and image[i][j] <= 128:
#                     image[i][j] = 100
#                 elif image[i][j] >= 128 and image[i][j] <= 192:
#                     image[i][j] = 200
#                 elif image[i][j] >= 192 and image[i][j] <= 255:
#                     image[i][j] = 255
#     elif level == 16:
#         # For 16-level gray scale
#         for i in range(rows):
#             for j in range(column):
#                 if image[i][j] >= 0 and image[i][j] <= 16:
#                     image[i][j] = 0
#                 elif image[i][j] >= 16 and image[i][j] <= 32:
#                     image[i][j] = 16
#                 elif image[i][j] >= 32 and image[i][j] <= 48:
#                     image[i][j] = 32
#                 elif image[i][j] >= 48 and image[i][j] <= 64:
#                     image[i][j] = 48
#                 elif image[i][j] >= 64 and image[i][j] <= 80:
#                     image[i][j] = 64
#                 elif image[i][j] >= 80 and image[i][j] <= 96:
#                     image[i][j] = 80
#                 elif image[i][j] >= 96 and image[i][j] <= 112 :
#                     image[i][j] = 96
#                 elif image[i][j] >= 112 and image[i][j] <= 128:
#                     image[i][j] = 112
#                 elif image[i][j] >= 128 and image[i][j] <= 144:
#                     image[i][j] = 128
#                 elif image[i][j] >= 144 and image[i][j] <= 160:
#                     image[i][j] = 144
#                 elif image[i][j] >= 160 and image[i][j] <= 176:
#                     image[i][j] = 160
#                 elif image[i][j] >= 176 and image[i][j] <= 192:
#                     image[i][j] = 176
#                 elif image[i][j] >= 192 and image[i][j] <= 208:
#                     image[i][j] = 192
#                 elif image[i][j] >= 208 and image[i][j] <= 224:
#                     image[i][j] = 208
#                 elif image[i][j] >= 224 and image[i][j] <= 240:
#                     image[i][j] = 224
#                 elif image[i][j] >= 240 and image[i][j] <= 255:
#                     image[i][j] = 240
#                 else:
#                     image[i][j] = 255
#     return image
#
#
# img1 = cv2.imread('gradi.jpg', 0)
# cv2.imshow('Original', img1)
# x = int(input('Enter the levels from 2, 4, 16: '))
# img2 = conversion(img1, x)
# cv2.imshow('Gradients', img2)
# cv2.waitKey(0)


# task 6
# def distance_map(image, formula):
#     centre = [int(image.shape[0] / 2) + 1, int(image.shape[1] / 2) + 1]
#     if formula == 'Euclidian':
#         for i in range(image.shape[0]):
#             for j in range(image.shape[1]):
#                 image[i][j] = ((centre[0] - i) ** 2 + (centre[1] - j) ** 2) ** .5
#                 if ((centre[0] - i) ** 2 + (centre[1] - j) ** 2) ** .5 > 255:
#                     image[i][j] = 255
#
#     elif formula == 'City':
#         for i in range(image.shape[0]):
#             for j in range(image.shape[1]):
#                 image[i][j] = np.abs((centre[0] - i)) + np.abs((centre[1] - j))
#                 if np.abs((centre[0] - i)) + np.abs((centre[1] - j)) > 255:
#                     image[i][j] = 255
#
#     elif formula == 'Chessboard':
#         for i in range(image.shape[0]):
#             for j in range(image.shape[1]):
#                 if np.abs((centre[0] - i)) > np.abs((centre[1] - j)):
#                     image[i][j] = np.abs((centre[0] - i))
#                     if np.abs((centre[0] - i)) > 255:
#                         image[i][j] = 255
#                 else:
#                     image[i][j] = np.abs((centre[1] - j))
#                     if np.abs((centre[1] - j)) > 255:
#                         image[i][j] = 255
#     cv2.imshow('Output', image)
#     cv2.waitKey()
#
#
# choice = input('Type your choice = Chessboard,City,Euclidian :')
# x = int(input('Number of rows:'))
# y = int(input('Number of column:'))
# image = np.zeros((x, y), np.uint8)
# distance_map(image, choice)