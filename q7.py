n = int(input("How many Fibonacci numbers do you want?"))

a, b = 0, 1
count = 1

if n <= 0:
    print("Please, enter a positive integer.")
elif n == 1:
    print(a)
else:
    while count < n:
        print(a, end=" ")
        c = a + b
        a = b
        b = c
        count += 1