# Locally Executed file
#===========================
f = open("text.txt",'r')
print(f.readline())
#===========================
# File path
file_path = "text.txt"

# Create and write to a file
with open(file_path, "w") as file:
    file.write("This is a sample text file.\n")
    file.write("It contains some lines of text.\n")
    file.write("We will read and manipulate this file.\n")

# Read and display the contents of the file
with open(file_path, "r") as file:
    print("File Contents:")
    for line in file:
        print(line.strip())  # Remove newline characters

# Append additional content to the file
with open(file_path, "a") as file:
    file.write("Now, we are appending more text to the file.\n")

# Read and display the updated contents of the file
with open(file_path, "r") as file:
    print("\nUpdated File Contents:")
    for line in file:
        print(line.strip())

# Count the number of lines in the file
with open(file_path, "r") as file:
    line_count = sum(1 for line in file)
    print("\nNumber of Lines in the File:", line_count)

# Search for a specific word in the file
search_word = "sample"
with open(file_path, "r") as file:
    for line in file:
        if search_word in line:
            print(f"'{search_word}' found in the line: {line.strip()}")

# Create a copy of the file
copy_file_path = "copy_example.txt"
with open(file_path, "r") as source_file, open(copy_file_path, "w") as dest_file:
    dest_file.write(source_file.read())

print("\nFile copied to", copy_file_path)

