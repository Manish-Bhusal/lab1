# Step 1: Create an empty dictionary
my_dict = {}

# Step 2: Ask how many key-value pairs the user wants to enter
n = int(input("How many items do you want to add? "))

# Step 3: Loop to add each key-value pair
for i in range(n):
    key = input("Enter key (like a word): ")
    value = input("Enter value (like the meaning): ")
    my_dict[key] = value  # Save it in the dictionary

print("\nHere is your dictionary:")
print(my_dict)

# Step 4: Search for a key
search_key = input("\nEnter a key to search for its value: ")

# Step 5: Show the value if the key is found
if search_key in my_dict:
    print("The value for", search_key, "is:", my_dict[search_key])
else:
    print("Sorry! That key was not found.")