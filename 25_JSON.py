import json

# Create a Python dictionary
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Serialize the dictionary to JSON and write it to a file
with open("data.json", "w") as json_file:
    json.dump(data, json_file)

# Read JSON data from the file
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print("Loaded JSON data:", loaded_data)

# Modify the loaded data
loaded_data["age"] = 31

# Serialize the modified data and write it back to the file
with open("data.json", "w") as json_file:
    json.dump(loaded_data, json_file)

# Read and print the modified JSON data
with open("data.json", "r") as json_file:
    modified_data = json.load(json_file)
    print("Modified JSON data:", modified_data)
