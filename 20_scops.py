# Global variable
global_variable = "I am a global variable"

def my_function():
    # Local variable
    local_variable = "I am a local variable"
    print("Inside my_function:")
    print(local_variable)  # Accessing the local variable
    print(global_variable)  # Accessing the global variable

# Accessing the global variable outside the function
print("Outside my_function:")
print(global_variable)  # Accessing the global variable

# Attempting to access the local variable outside the function will result in an error
# Uncomment the next line to see the error
# print(local_variable)  # This will raise a NameError

my_function()  # Calling the function
