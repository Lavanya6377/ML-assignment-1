# Write a program that copies the contents of one text file to another

Ques25sourcefile = 'C:/Users/ASUS/PycharmProjects/ML Assignment 1/Ques25sourcefile.txt'           # Replace with your source file path
Ques25destination = 'C:/Users/ASUS/PycharmProjects/ML Assignment 1/Ques25destination.txt' # Replace with your destination file path

try:
    # Open the source file in read mode
    with open(Ques25sourcefile, 'r') as f_source:
        # Read the contents of the source file
        content = f_source.read()

    # Open the destination file in write mode
    with open(Ques25destination, 'w') as f_dest:
        # Write the contents to the destination file
        f_dest.write(content)

    print(f"Successfully copied content from '{Ques25sourcefile}' to '{Ques25destination}'.")
except FileNotFoundError:
    print("Error: One of the files does not exist.")

except IOError as e:
    print(f"Error: Failed to read/write data. Details: {e}")
