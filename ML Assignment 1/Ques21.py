# Write a python program that counts the occurrences of a specific element
# in a list.

# Take user input for the list of numbers
input_list = input("Enter a list of numbers separated by spaces: ").strip().split()

# Convert input values to integers
my_list = [int(num) for num in input_list]

# Take user input for the element to count occurrences
element_to_count = int(input("Enter the element to count its occurrences: "))

# Initialize a counter variable
count = 0

# Iterate over each element in the list
for item in my_list:
    # Check if the current element matches the element to count
    if item == element_to_count:
        # Increment the count
        count += 1

# Print the count of occurrences
print(f"The element {element_to_count} occurs {count} times in the list.")

