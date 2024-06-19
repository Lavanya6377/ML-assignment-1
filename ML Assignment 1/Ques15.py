# Write a program that reads data from a CSV file and prints it to the
# console.

import csv

# Specify the path to your CSV file
file_path = 'C:/Users/ASUS/Downloads/ques15.csv.csv'  # Replace with your CSV file path

try:
    # Open the CSV file in read mode
    with open(file_path, mode='r', newline='') as file:
        # Create a CSV reader object
        reader = csv.reader(file)

        # Iterate over each row in the CSV file
        for row in reader:
            # Print each row to the console
            print(row)

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")

except IOError:
    print(f"Error: Failed to read data from file '{file_path}'.")
