import random

# Seed the random number generator
random.seed(42)

# Initialize a list for collecting results
results = []

# Method 1: randrange()
results.append(random.randrange(10, 20))  # Generate a random number between 10 and 19

# Method 2: randint()
results.append(random.randint(1, 100))  # Generate a random number between 1 and 100

# Method 3: choice()
my_list = ["apple", "banana", "cherry", "date", "fig"]
results.append(random.choice(my_list))  # Choose a random element from the list

# Method 4: choices()
results.append(random.choices(my_list, k=3))  # Choose 3 random elements from the list with replacement

# Method 5: shuffle()
random.shuffle(my_list)  # Shuffle the list in place
results.append(my_list)

# Method 6: sample()
results.append(random.sample(my_list, 2))  # Choose 2 unique random elements from the list

# Method 7: random()
results.append(random.random())  # Generate a random float between 0 and 1

# Method 8: uniform()
results.append(random.uniform(1.0, 10.0))  # Generate a random float between 1.0 and 10.0

# Method 9: triangular()
results.append(random.triangular(5.0, 10.0, 7.5))  # Generate a random float between 5.0 and 10.0 with a mode of 7.5

# Print the results
for i, result in enumerate(results, start=1):
    print(f"Result {i}: {result}")
