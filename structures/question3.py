import random as r
list_of_random_numbers = []
for i in range(10):
    list_of_random_numbers.append(r.randint(1, 101))

print(f"The list of 10 random numbers is: {list_of_random_numbers}")
even_list = []

for num in list_of_random_numbers:
    if(num % 2 == 0):
        even_list.append(num)
print(f"The list of even numbers is: {even_list}")