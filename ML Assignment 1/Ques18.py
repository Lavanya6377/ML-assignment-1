# Write a python program that checks if two strings are anagrams of each
# other.
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Remove spaces and convert to lowercase
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

# Check if lengths are the same
if len(str1) != len(str2):
    print("The strings are not anagrams.")
else:
    # Sort characters in both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Compare sorted strings
    if sorted_str1 == sorted_str2:
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")