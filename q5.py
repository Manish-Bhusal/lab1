list_of_number = []

how_many_numbers = int(input("Enter how many numbers are there in the list: "))
for i in range(how_many_numbers):
    num = int(input(f"Enter number {i+1}: "))
    list_of_number.append(num)

print(f"The list of {how_many_numbers} number is: {list_of_number}.")

print(f"The maximum number of the list is: {max(list_of_number)}")
print(f"The minimum number of the list is: {min(list_of_number)}")
