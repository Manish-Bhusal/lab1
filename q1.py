number = int(input("Enter a number to check if it's prime: "))
count = 0
for i in range(1, number+1):
    if number % i == 0:
        count += 1
if count == 2:
    print(f"{number} is a prime.")
else:
    print(f"{number} is not a prime.")

