list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [2, 4, 6, 8, 10]
set1 = set(list1)
set2 = set(list2)
common_elements = set1.intersection(set2) #also 
# common_elements = set1 & set2

result = list(common_elements)
print(sorted(result))
