
# Sum the Numbers --

# Multiplying each interger in the list by 5.

# numbers = [14, 123, 14]
# multiplied_list = [i * 5 for i in numbers]

# print (multiplied_list)

# ---

# Largest Number --

# numbers = [1, 13, 5, 23, 500, 32, 14]

# Sort is ascending by default if reversed
# It will then be in descending order

# numbers.sort(reverse=True)

# print(numbers)

# --- 

# Smallest Number --

# numbers = [1, 13, 5, 23, 500, 32, 14]

# numbers.sort()

# print(numbers)

# ---

# Even Numbers --

# numbers = [1, 13, 5, 23, 500, 32, 14]
# empty_list=[]
# for i in numbers:
#     if i%2==0:
#         empty_list+=[i]
# print(empty_list)

# -- 

# Positive Numbers --

# numbers = [-1, 13, -5, -23, 500, -32, 14]
# empty_string= ''
# for i in numbers:
#     if i >=0:
#         print(i, empty_string)

# -- 

# Positive Numbers II -- 

# numbers = [-1, 13, -5, -23, 500, -32, 14]
# empty_list=[]
# for i in numbers:
#     if i >=0:
#         empty_list+=[i]
# print(empty_list)

# -- 

# Multiply a list -- 

# Not sure if this how it has to be done 

# numbers = [3, 4, 16, 12, -1]
# empty_list=[]

# for i in numbers: 
#     empty_list.append(i * 3)
# print (empty_list)

# -- 

# Multiplying Vectors -- 

# The zip() function returns a zip object, which is an 
# iterator of tuples where the first item in each passed iterator is paired together, 
# and then the second item in each passed iterator are paired together etc.

# Pass both lists into zip(*iterables) to get a list of tuples that pair elements with
#  the same position from both lists. Use a for loop to multiply 
# these elements together and append them to a new list.

# list_num1 = [5, 13, 45]
# list_num2 = [3, 15, 55]
# empty_list = []

# for num1, num2 in zip(list_num1,list_num2):
#     empty_list.append(num1 * num2)
# print(empty_list)

# --

# Matrix Addition I and II ?-- 

# nes_list1 = [[8, 3],
#             [12, 4]]
# nes_list2 = [[12, 1],
#              [3, 12]]

# sum = [[0, 0],
#       [0, 0]]
# for i in range (len(nes_list1)):
#     for x in range (len(nes_list1[0])):
#         sum[i][x] = nes_list1[i][x] + nes_list2[i][x]

# for s in sum:
#     print(s)

# -- 

# De-dup -- 

# the easiest way to remove dupes in a list is 
# to convert it to a set and then back to a list again.

list_1 = [1, 2, 3, 4, 5, 1, 2, 4, 'hey', 'hey']
conver_list = list(set(list_1))

print(conver_list)