1. Write a Python program to remove all duplicates from a list and print the unique elements.

# `METHOD_1:` Just converting the old list into a new list.
old_list = [1, 2, 1, 2, 2]
new_list = list(set(old_list))

print(new_list)
# `METHOD_2`: Just append the items to the new list that are not in the old list.
old_list = [1, 2, 1, 1, 1, 2]
new_list = []
for items in old_list:
    if items not in new_list:
        new_list.append(items)

print(new_list)
