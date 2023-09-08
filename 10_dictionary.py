# Creating an example dictionary
sample_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Method 1: clear() - Removes all elements from the dictionary
sample_dict.clear()
print("After clear():", sample_dict)

# Re-populate the dictionary
sample_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Method 2: copy() - Returns a copy of the dictionary
copy_dict = sample_dict.copy()
print("Copy of the dictionary:", copy_dict)

# Method 3: fromkeys() - Returns a dictionary with specified keys and value
keys = ['name', 'age', 'city']
value = 'Unknown'
new_dict = dict.fromkeys(keys, value)
print("fromkeys() result:", new_dict)

# Method 4: get() - Returns the value of the specified key
name = sample_dict.get('name')
print("Value for 'name':", name)

# Method 5: items() - Returns a list of tuples for each key-value pair
items = sample_dict.items()
print("Items in the dictionary:", items)

# Method 6: keys() - Returns a list of keys in the dictionary
keys = sample_dict.keys()
print("Keys in the dictionary:", list(keys))

# Method 7: pop() - Removes and returns the element with the specified key
age = sample_dict.pop('age')
print("Removed 'age' and got:", age)
print("Updated dictionary:", sample_dict)

# Method 8: popitem() - Removes and returns the last inserted key-value pair
last_item = sample_dict.popitem()
print("Removed last item:", last_item)
print("Updated dictionary:", sample_dict)

# Method 9: setdefault() - Returns the value of the specified key. If key doesn't exist, inserts it with the specified value.
country = sample_dict.setdefault('country', 'USA')
print("Value for 'country':", country)
print("Updated dictionary:", sample_dict)

# Method 10: update() - Updates the dictionary with specified key-value pairs
update_dict = {'city': 'Los Angeles', 'state': 'California'}
sample_dict.update(update_dict)
print("Updated dictionary:", sample_dict)

# Method 11: values() - Returns a list of all values in the dictionary
values = sample_dict.values()
print("Values in the dictionary:", list(values))
