main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
remove_list = [2, 4, 6, 8]

main_set = set(main_list)
remove_set = set(remove_list)

filtered_set = main_set - remove_set

filtered_list = list(filtered_set)

print("The filtered list after removing the common from main list is", filtered_list)