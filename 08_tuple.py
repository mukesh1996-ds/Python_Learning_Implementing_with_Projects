# Accessing list items
my_list = [1, 2, 3, 4, 5]
print("Accessing list items:")
print("First item:", my_list[0])  # Accessing the first item
print("Last item:", my_list[-1])  # Accessing the last item

# Changing list items
my_list[2] = 99
print("\nChanging list items:")
print("Modified list:", my_list)

# Adding items to a list
my_list.append(6)
my_list.insert(3, 42)
print("\nAdding items to a list:")
print("Updated list:", my_list)

# Removing items from a list
my_list.remove(99)
popped_item = my_list.pop(4)
print("\nRemoving items from a list:")
print("Updated list after removing 99:", my_list)
print("Popped item:", popped_item)

# Looping through a list
print("\nLooping through a list:")
for item in my_list:
    print(item)

# Tuple comparison
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
print("\nTuple comparison:")
if tuple1 == tuple2:
    print("Tuples are equal.")
else:
    print("Tuples are not equal.")

# Sorting a list
my_list.sort()
print("\nSorting a list:")
print("Sorted list:", my_list)

# Copying a list
copied_list = my_list.copy()
print("\nCopying a list:")
print("Copied list:", copied_list)

# Joining elements of a list into a string
list_of_strings = ['Hello', 'World', 'Python']
joined_string = ' '.join(list_of_strings)
print("\nJoining elements of a list:")
print("Joined string:", joined_string)

# Tuple built-in methods
my_tuple = (1, 2, 3, 4, 5)
print("\nTuple built-in methods:")
print("Tuple length:", len(my_tuple))
print("Tuple index of 3:", my_tuple.index(3))
print("Count of 4 in tuple:", my_tuple.count(4))
