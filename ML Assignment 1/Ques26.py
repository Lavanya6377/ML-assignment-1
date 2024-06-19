#Write a program in python that checks if a string starts with a given prefix
#or ends with a given suffix.


text = input("Enter a text string: ")

# Take user input for the prefix and suffix to check
prefix_to_check = input("Enter a prefix to check (or press Enter to skip): ").strip()
suffix_to_check = input("Enter a suffix to check (or press Enter to skip): ").strip()

# Check if the text starts with the prefix
if prefix_to_check and text.startswith(prefix_to_check):
    print(f"The text '{text}' starts with the prefix '{prefix_to_check}'.")
else:
    print(f"The text '{text}' does not start with the prefix '{prefix_to_check}'.")

# Check if the text ends with the suffix
if suffix_to_check and text.endswith(suffix_to_check):
    print(f"The text '{text}' ends with the suffix '{suffix_to_check}'.")
else:
    print(f"The text '{text}' does not end with the suffix '{suffix_to_check}'.")
