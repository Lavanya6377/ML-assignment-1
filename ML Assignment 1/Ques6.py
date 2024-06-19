# Write a program that reads the content of a text file and prints it to the
# console
# Specify the file path
ques6 = 'C:/Users/ASUS/PycharmProjects/ML Assignment 1/ques6.txt'  # Replace with your file path

try:
    # Open the file in read mode
    with open(ques6, 'r') as file:
        # Read and print each line of the file
        for line in file:
            print(line, end='')  # end='' prevents adding extra newline (since 'line' already includes newline)

except FileNotFoundError:
    print(f"Error: The file '{ques6}' was not found.")

except IOError:
    print(f"Error: Failed to read data from file '{ques6}'.")
