# Define a sample string
sample_string = "Hello, World! This is a Python script."

# Method 1: capitalize() - Converts the first character to uppercase
capitalized_string = sample_string.capitalize()
print("capitalize():", capitalized_string)

# Method 2: index() - Searches the string for a specified value and returns the position of where it was found
index = sample_string.index("Python")
print("index():", index)

# Method 3: slicing - Accessing and slicing the string
first_char = sample_string[0]          # Accessing the first character
sliced_text = sample_string[7:12]      # Slicing from index 7 to 11 (exclusive)
print("Indexing and Slicing:")
print("First Character:", first_char)
print("Sliced Text:", sliced_text)

# Method 4: join() - Joins elements of an iterable to the end of the string
words = ["Python", "is", "awesome"]
joined_text = " ".join(words)
print("join():", joined_text)

# Method 5: split() - Splits the string at the specified separator and returns a list
split_parts = sample_string.split(" ")
print("split():", split_parts)

# Method 6: replace() - Replaces a specified value with another value in the string
replaced_string = sample_string.replace("Python", "GPT-3")
print("replace():", replaced_string)
