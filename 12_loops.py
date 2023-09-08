# Example using a for loop to iterate through a list
fruits = ["apple", "banana", "cherry"]
print("Using a for loop:")
for fruit in fruits:
    print(f"I like {fruit}!")

# Example using a while loop to count from 1 to 5
print("\nUsing a while loop:")
count = 1
while count <= 5:
    print(count)
    count += 1

# Example using a nested loop to create a multiplication table
print("\nUsing a nested loop to create a multiplication table:")
for i in range(1, 6):
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")
    print()  # Add an empty line after each row

# Example using a loop to iterate through a dictionary
print("\nUsing a loop to iterate through a dictionary:")
student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
for student, grade in student_grades.items():
    print(f"{student}: {grade}")

# Example using a loop with break and continue statements
print("\nUsing a loop with break and continue:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        continue  # Skip odd numbers
    if number == 6:
        break  # Exit the loop when we reach 6
