# # -----------------Task2---------------
# def binary(num):
#     bit = []
#     while num:
#         bit.append(num % 2)
#         num >>= 1
#     return bit[::-1]
#
#
# def octal(num):
#     bit1 = []
#     while num:
#         bit1.append(num % 8)
#         num //= 8
#     return bit1[::-1]
#
#
# def hex_conv(num):
#     bit2 = []
#     while num:
#         bit2.append(num % 16)
#         num //= 16
#     return bit2[::-1]
#
#
# int1 = input('Enter any integer: ')
# int1 = int(int1)
# num_sys = input('Enter the number system: ')
# print(int1, "into", num_sys)
# if num_sys == 'binary':
#     convert = binary(int1)
#     print('In Binary', convert)
# if num_sys == 'octal':
#     convert_oct = octal(int1)
#     print('In octal', convert_oct)
# if num_sys == 'hex':
#     convert_hex = hex_conv(int1)
#     print('In hex', convert_hex)


# # -----------------Task1---------------
# def sorter(my_input_list, sort_criteria, order):
#     sub_list = ['Age', 'CGPA', 'city']
#     sort_index = sub_list.index(sort_criteria)
#
#     if order == 'Ascending':
#         for i in range(len(my_input_list)):
#             for j in range(len(my_input_list) - 1):
#                 if my_input_list[j][sort_index] > my_input_list[j+1][sort_index]:
#                     my_input_list[j], my_input_list[j+1] = my_input_list[j+1], my_input_list[j]
#     elif order == 'Descending':
#         for i in range(len(my_input_list)):
#             for j in range(len(my_input_list) - 1):
#                 if my_input_list[j][sort_index] < my_input_list[j+1][sort_index]:
#                     my_input_list[j], my_input_list[j+1] = my_input_list[j+1], my_input_list[j]
#     else:
#         print("Invalid order specified, please use 'Ascending' or 'Descending'.")
#
#     return my_input_list
#
#
# my_input_list = [[29, 3.2, 'Rawalpindi'], [22, 4.0, 'Islamabad'], [12, 0, 'Karachi']]
# sorted_list = sorter(my_input_list, 'Age', 'Ascending')
# print(sorted_list)
#

# # -------------------task4----------------
# # Morse code mappings
# MORSE_CODE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
#
# # Reverse Morse code mappings
# REVERSE_MORSE_CODE = {value: key for key, value in MORSE_CODE.items()}
#
#
# def engtomorse(eng1):
#     morse_code = ''
#     for char in eng1.upper():
#         if char == ' ':
#             morse_code += ' '
#         else:
#             morse_code += MORSE_CODE[char] + ' '
#     return morse_code.strip()
#
#
# def morsetoeng(morse1):
#     eng_text = ''
#     words = morse1.split('  ')
#     for word in words:
#         chars = word.split(' ')
#         for char in chars:
#             eng_text += REVERSE_MORSE_CODE[char]
#         eng_text += ' '
#     return eng_text.strip()
#
#
# eng = 'OMNI CHRONE'
# morse_encode = engtomorse(eng)
# print(morse_encode)  # prints morse of eng_text
# decoded_text = morsetoeng(morse_encode)
# print(decoded_text)  # prints text of morse code


# -------------------task6----------------
# def garland(str1):
#     for i in range(1, len(str1)):
#         if str1[:i] == str1[-i:]:
#             return i
#     return 0
#
# print(garland("gonawazgo"))  # 2
# print(garland("neon"))  # 1
# print(garland("onion"))  # 2
# print(garland("moonamoon"))  # 4
#

# -------------------task7----------------

# def minmax_normalization(list1):
#     min_val = min(list1)
#     max_val = max(list1)
#     if min_val == max_val:
#         return [0] * len(list1)
#     normalized_list = []
#     for x in list1:
#         scaled_x = (x - min_val) / (max_val - min_val)
#
#         normalized_list.append(scaled_x)
#     return normalized_list
#
# mylist = [15, 3, 6, 54, 9, 1, 69, 29, 99]
# print(minmax_normalization(mylist))



# # -------------------task8----------------
# def sum1(mymatrix):
#     mat_sums = []
#     n = len(mymatrix)
#     for i in range(0, n, 3):
#         for j in range(0, n, 3):
#             grid_sum = 0
#             for k in range(3):
#                 for l in range(3):
#                     grid_sum += mymatrix[i+k][j+l]
#             mat_sums.append(grid_sum)
#     return mat_sums
#
#
# MATRIX1 = [
#     [12, 28, 34, 4, 55, 61, 79, 8, 96],
#     [23, 3, 4, 54, 6, 7, 83, 95, 1],
#     [31, 41, 53, 6, 76, 8, 92, 1, 21],
#     [47, 50, 61, 79, 8, 95, 1, 23, 3],
#     [55, 64, 7, 81, 93, 1, 24, 3, 41],
#     [67, 71, 8, 96, 1, 23, 31, 43, 55],
#     [79, 8, 9, 12, 29, 30, 47, 5, 6],
#     [84, 95, 1, 28, 35, 4, 58, 6, 70],
#     [92, 14, 22, 3, 43, 5, 64, 76, 88]
# ]
# result = sum1(MATRIX1)
# print(result)
# -------------------task5----------------
import random
import string


def find_word(puzzle, word):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == word[0]:
                # check horizontally
                if ''.join(puzzle[i][j:j+len(word)]) == word:
                    return True
                # check vertically
                if ''.join([puzzle[k][j] for k in range(i, i+len(word))]) == word:
                    return True
    return False


def two_D_puzzle():
    n = 9
    puzzle = []
    for j in range(n):
        row = []
        for i in range(n):
            letter = random.choice(string.ascii_uppercase)
            row.append(letter)
        puzzle.append(row)
    return puzzle


def printpuzzle(puzzle):
    for i in range(9):
        for j in range(9):
            print(puzzle[i][j], end=' ')
        print()


puzzle = two_D_puzzle()
printpuzzle(puzzle)

word = input('Enter the word you want to find: ')
if find_word(puzzle, word):
    print('The word you want is in the puzzle!')
else:
    print('The word you want is not in the puzzle')
