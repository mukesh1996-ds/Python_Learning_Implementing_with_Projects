# Initialize a sample set
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# Add an element to the set
my_set.add(6)
print("After add(6):", my_set)

# Remove all elements from the set
my_set.clear()
print("After clear():", my_set)

# Create a new set and copy it
set1 = {1, 2, 3}
set2 = set1.copy()
print("set1:", set1)
print("set2 (copy of set1):", set2)

# Create two sets and find their difference
set3 = {1, 2, 3, 4}
set4 = {3, 4, 5, 6}
difference = set3.difference(set4)
print("Difference between set3 and set4:", difference)

# Remove items from a set that are in another set
set3.difference_update(set4)
print("After difference_update(set4):", set3)

# Remove a specific item from the set
set3.discard(1)
print("After discard(1):", set3)

# Find the intersection of two sets
set5 = {1, 2, 3}
set6 = {3, 4, 5}
intersection = set5.intersection(set6)
print("Intersection of set5 and set6:", intersection)

# Remove items from a set that are not in other sets
set5.intersection_update(set6)
print("After intersection_update(set6):", set5)

# Check if two sets are disjoint
set7 = {1, 2, 3}
set8 = {4, 5, 6}
is_disjoint = set7.isdisjoint(set8)
print("Are set7 and set8 disjoint?", is_disjoint)

# Check if a set is a subset of another
subset_check = set5.issubset(set6)
print("Is set5 a subset of set6?", subset_check)

# Check if a set is a superset of another
superset_check = set3.issuperset(set4)
print("Is set3 a superset of set4?", superset_check)

# Remove and return an arbitrary element from the set
popped_element = set4.pop()
print("Popped element from set4:", popped_element)
print("Set4 after pop:", set4)

# Remove a specific element from the set
set3.remove(2)
print("After remove(2):", set3)

# Find the symmetric difference between two sets
set9 = {1, 2, 3, 4}
set10 = {3, 4, 5, 6}
symmetric_difference = set9.symmetric_difference(set10)
print("Symmetric difference between set9 and set10:", symmetric_difference)

# Update a set with the symmetric differences of two sets
set9.symmetric_difference_update(set10)
print("After symmetric_difference_update(set10):", set9)

# Find the union of two sets
set11 = {1, 2, 3}
set12 = {3, 4, 5}
union = set11.union(set12)
print("Union of set11 and set12:", union)

# Update a set with the union of other sets
set11.update(set12)
print("After update(set12):", set11)
