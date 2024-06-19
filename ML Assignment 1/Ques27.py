# Write a program in python that converts a string into a list of its characters.

# Take user input for the string
input_string = input("Enter a string: ")

# Initialize an empty list to store characters
characters_list = []

# Iterate over each character in the string
for char in input_string:
    # Append each character to the list
    characters_list.append(char)

# Print the list of characters
print("List of characters:", characters_list)
