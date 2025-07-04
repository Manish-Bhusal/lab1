dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 30, 'c': 40, 'd': 50}

# Create a new dictionary to store the merged result
merged_dict = {}

# Add all keys from dict1
for key in dict1:
    merged_dict[key] = dict1[key]

# Add keys from dict2, summing if key already exists
for key in dict2:
    if key in merged_dict:
        merged_dict[key] += dict2[key]
    else:
        merged_dict[key] = dict2[key]

print("Merged dictionary with summed values:", merged_dict)
