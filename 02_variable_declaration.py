# Variable declaration and assignment
my_integer = 42  # An integer variable
my_float = 3.14  # A floating-point variable
my_string = "Hello, world!"  # A string variable
my_boolean = True  # A boolean variable

# Displaying the variables
print("my_integer:", my_integer)
print("my_float:", my_float)
print("my_string:", my_string)
print("my_boolean:", my_boolean)

# Casting variables
# You can change the type of a variable using casting functions like int(), float(), str(), etc.

# Casting to integer
my_float_as_int = int(my_float)  # Casts the float to an integer (3.14 -> 3)
my_string_as_int = int("123")    # Casts the string "123" to an integer (string to int)

# Casting to float
my_int_as_float = float(my_integer)  # Casts the integer to a float (42 -> 42.0)
my_string_as_float = float("3.14")  # Casts the string "3.14" to a float (string to float)

# Casting to string
my_integer_as_string = str(my_integer)  # Casts the integer to a string (42 -> "42")
my_float_as_string = str(my_float)      # Casts the float to a string (3.14 -> "3.14")

# Displaying the casted variables
print("my_float_as_int:", my_float_as_int)
print("my_string_as_int:", my_string_as_int)
print("my_int_as_float:", my_int_as_float)
print("my_string_as_float:", my_string_as_float)
print("my_integer_as_string:", my_integer_as_string)
print("my_float_as_string:", my_float_as_string)

# Variable declaration with single quotes and double quotes
single_quoted_string = 'This is a single-quoted string.'
double_quoted_string = "This is a double-quoted string."

# Displaying the quoted strings
print("single_quoted_string:", single_quoted_string)
print("double_quoted_string:", double_quoted_string)


# Unpacking of variables from the list

fruits = ["Apple", "Banana", "Mango"]

a, b, c = fruits

print("Value of a is:", a)
print("Value of b is:", b)
print("Value of c is:", c)

# Gloabal Variable

# Step 1: Declare a global variable outside of any function or method
global_variable = 10

# Step 2: Use the global keyword to modify the global variable from within a function
def modify_global_variable():
    global global_variable  # Use the global keyword to indicate that we're modifying the global variable
    global_variable = 20     # Modify the global variable

# You can access the global variable from anywhere in your code
print("Before modification:", global_variable)

# Call the function to modify the global variable
modify_global_variable()

# Check the value of the global variable after modification
print("After modification:", global_variable)

# Global variable with same variable name
global_variable = 10

def modify_global_variable():
    global global_variable
    global_variable = 20

modify_global_variable()
print("After modification:", global_variable)  # This will print the modified global variable value (20)
