# Define a sample list
my_list = [1, 2, 3, 4, 5]

# Accessing list items
print("Accessing list items:")
print("First item:", my_list[0])
print("Last item:", my_list[-1])

# Changing list items
print("\nChanging list items:")
my_list[2] = 10
print("Modified list:", my_list)

# Adding elements to the list
print("\nAdding elements to the list:")
my_list.append(6)
my_list.insert(2, 7)
print("After appending and inserting:", my_list)

# Removing elements from the list
print("\nRemoving elements from the list:")
my_list.remove(4)
popped_item = my_list.pop()
print("After removing 4 and popping the last item:", my_list)
print("Popped item:", popped_item)

# Looping through the list
print("\nLooping through the list:")
for item in my_list:
    print(item)

# List comparison
print("\nList comparison:")
other_list = [1, 2, 7, 6, 10]
if my_list == other_list:
    print("The lists are equal")
else:
    print("The lists are not equal")

# Sorting the list
print("\nSorting the list:")
my_list.sort()
print("Sorted list:", my_list)

# Copying the list
print("\nCopying the list:")
my_list_copy = my_list.copy()
print("Copied list:", my_list_copy)

# Joining list elements into a string
print("\nJoining list elements into a string:")
list_as_string = ', '.join(map(str, my_list))
print("List as a string:", list_as_string)
