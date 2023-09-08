# Define a lambda function to calculate the square of a number
square = lambda x: x ** 2

# Define a lambda function to add two numbers
add = lambda x, y: x + y

# Define a lambda function to check if a number is even
is_even = lambda x: x % 2 == 0

# Usage of lambda functions
print("Square of 5:", square(5))
print("Addition of 3 and 7:", add(3, 7))

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(is_even, num_list))
print("Even numbers in the list:", even_numbers)
