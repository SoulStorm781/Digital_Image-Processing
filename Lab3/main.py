# import numpy as np
# import cv2

# # Define the input array
# a1 = np.array([[1, 1, 0, 0, 0, 1],
#                [0, 0, 1, 1, 0, 0],
#                [1, 1, 1, 0, 1, 0],
#                [0, 0, 1, 1, 0, 1],
#                [1, 1, 1, 0, 1, 0],
#                [0, 0, 1, 1, 0, 1]])
#
# # Pad the input array with zeros
# a1 = np.pad(a1, [(1, 1), (1, 0)], mode='constant')
#
# # Initialize variables
# r, c = np.shape(a1)
# label = np.zeros_like(a1, dtype=int)
# current_label = 0
#
# # Loop over the input array and label connected components
# for i in range(1, r):
#     for j in range(1, c):
#         if a1[i, j] == 1:
#             if a1[i, j-1] == 0 and a1[i-1, j] == 0:
#                 current_label += 1
#                 label[i, j] = current_label
#             elif a1[i, j-1] == 1 and a1[i-1, j] == 0:
#                 label[i, j] = label[i, j-1]
#             elif a1[i, j-1] == 0 and a1[i-1, j] == 1:
#                 label[i, j] = label[i-1, j]
#             elif a1[i, j-1] == 1 and a1[i-1, j] == 1:
#                 label[i, j] = min(label[i, j-1], label[i-1, j])
#                 if label[i, j-1] != label[i-1, j]:
#                     for k in range(1, j+1):
#                         if label[i, k] == label[i, j-1]:
#                             label[i, k] = label[i-1, j]
#                     for k in range(j, c):
#                         if label[i-1, k] == label[i-1, j]:
#                             label[i-1, k] = label[i, j-1]
#
# # Print the labeled image
# print(label[1:-1, :])


# def distance(p1, p2, choice):
#     if choice == 1:
#         return int((((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))**.5)
#     elif choice == 2:
#         return int(np.abs((p1[0]-p2[0]))+np.abs((p1[1]-p2[1])))
#     elif choice == 3:
#         return int(max(np.abs((p1[0]-p2[0])), np.abs((p1[1]-p2[1]))))
#     else:
#         print('Error! choice should be 1, 2, or 3')
#
# p1 = []
# p2 = []
#
# for i in range(2):
#     x = int(input(f"Enter x-coordinate of point {chr(65+i)}: "))
#     y = int(input(f"Enter y-coordinate of point {chr(65+i)}: "))
#     p = [x, y]
#     if i == 0:
#         p1 = p
#     else:
#         p2 = p
#
# choice = int(input('Enter Choice of Method:\n1->Euclidean Distance\n2-> City Block Distance\n3->Chessboard Distance\nSelect:'))
# while choice not in [1, 2, 3]:
#     choice = int(input('Invalid input. Please enter 1, 2, or 3: '))
#
# mydistance = distance(p1,p2,choice)
# print(f'Distance for Point A{p1} to Point C{p2} is {mydistance}')
