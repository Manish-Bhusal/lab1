list_of_prime = []

for num in range(1, 51):
    count = 0
    for i in range(1, num+1):
        if(num % i == 0):
            count += 1
    if count == 2:
        list_of_prime.append(num)
set_of_prime = set(list_of_prime)

number_to_check = int(input("Enter a number to check if it is in the set."))
print(f"You have entered: {number_to_check}.")
if number_to_check in set_of_prime:
    print(f"And {number_to_check} is a prime number.")
else:
    print(f"And {number_to_check} is not a prime number.")
