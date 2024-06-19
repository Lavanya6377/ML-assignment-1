# Write a python program that removes all punctuation from a given string.

import string
str1 = input("enter string:")
punctuation = string.punctuation
new_str = ""
for char in str1:
    if char not in punctuation:
        new_str+= char

print(new_str)