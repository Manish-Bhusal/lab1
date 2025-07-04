list_of_random_numbers = []
for i in range(10):
    list_of_random_numbers.append(r.randint(1, 100))

a_tuple = tuple(list_of_random_numbers)
print(f"The list of 10 random numbers is: {list_of_random_numbers}")

maximum = a_tuple[0]
minimum = a_tuple[0]

for item in a_tuple:
    if item > maximum:
        maximum = item
    if item < minimum:
        minimum = item
        
print(f"The maximum number is {maximum}.")
print(f"The minimum number is {minimum}.")
#### OR
import random as r

list_of_random_numbers = []
for i in range(10):
    list_of_random_numbers.append(r.randint(1, 100))

a_tuple = tuple(list_of_random_numbers)
print(f"The list of 10 random numbers is: {list_of_random_numbers}")


print(f"The maximum number is {max(a_tuple)}.")
print(f"The minimum number is {min(a_tuple)}.")