# Get user input
age = int(input("Enter your age: "))

# Check age conditions
if age < 0:
    print("Invalid age. Please enter a positive number.")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
