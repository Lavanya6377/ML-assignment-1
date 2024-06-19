# Write a program in python that counts the frequency of each character in
# a string.
str1 = input("Enter a string: ")
frequency = {}
for char in str1:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print("Character frequencies:")
for char, count in frequency.items():
    print(f"'{char}': {count}")