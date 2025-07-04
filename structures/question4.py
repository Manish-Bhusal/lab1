a_string = input("Enter a string to analyzd: ")
print(f"You have entered: {a_string}.")
char_count = {}

for char in a_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("\nCharacter Frequency:")
for char, count in char_count.items():
    print(f"'{char}' : {count}")