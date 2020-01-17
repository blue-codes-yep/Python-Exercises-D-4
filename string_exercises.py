
# upper will capitalize every character in the string
# print (str.upper("I'm not yelling you are!"))

# Title will capitalize each starting character of a string
# print (str.title("paxton blue lindsey"))

# According to google, and the research I did
# Slicing is the fastest way to reverse a string
# The slice statement means start at string length, end at position 0, 
# move with the step -1 (or one step backward).
# print (str("You're probably reading this backwards")[::-1])

#While loop version ---- 
# str = "You're probably reading this backwards"

# reverse= ""
# len_string = len(str)
# while len_string > 0: 
#     reverse += str [ len_string - 1]
#     len_string = len_string - 1
# print (reverse)
# ---------

# Was trying to convert from two list's still wondering if it's possible ?? 
# l33t_language = ["4", "8", "<", "|)", "3", "!=", "[,", "4", "1", "_|", "|<", "|_", "44", "|\|", "0", "|o", "O_", "|2", "5", "7", "|_|", "\/", "\/\/", "%", "`/", "2"]
# ABC = ["A","B","C", "D", "E", "F", "G" "H", "I", "J", "K", "L", "M", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# WORKING LEET TRANSLATOR USING DICTONARY --
# dict = {"A" : '4', "B" : '8', "C" : '<', "D" : '|)', "E" : '3', "F" : '!=', "G" : '[,', "H" : '4', "I" : '1', "J" : '_|', "K" : '|<', "L" : '|_', "M" : '44', "N" : '|\|', "O" : '0', "P" : '|o', "Q" : '0_', "R" : '|2', "S" : '5', "T" : '7', "U" : '|_|', "V" : '\/', "W" : '\/\/', "X" : '%', "Y" : '`/', "Z" : '2'}

# speak_leet = str(input("What sentence would you like to convert to 1337 language? ").upper())

# for letter in speak_leet:
#     if letter != ' ':
#         print (dict[letter])
#     else:
#         print(' ')
# --

# --- Was going to try to figure out how to do this 
# Exercise with a list.

# vowels = ["A", "E", "I", "O", "U", "Y"]

# long_vowel = str(input("Let's exaaaggeeeerateeee some vowels"))

# for vowels in long_vowel:
#     if vowels == long_vowel:
#         print(long_vowel)


# print(long_vowel)

#----- 

# Simpler working way 

# vowels="aeiou"
# user = input("Enter: ")
# new_string = ''

# for i in range(len(user)):
#     if user[i] == user[i - 1] and user[i] in vowels:
#         new_string += user[i] * 4
#     else:
#         new_string += user[i]
# print(new_string)

#------

# Look at the documentation to understand more on maketrans, and translate *

# abc = "abcdefghijklmnopqrstuvwxyz"
# caesar_cipher="bcdefghijklmnopqrstuvwxyza"
# user = input("Enter what you want ciphered: ")
# new_string = ''

# new_string = user.translate(str.maketrans(abc, caesar_cipher))


# print(new_string)



