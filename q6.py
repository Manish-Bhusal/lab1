positive = 0
negative = 0
zero = 0

print("Enter 10 integers:")

for i in range(10):
    num = int(input(f"Number {i+1}: "))

    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    elif num == 0:
        zero += 1
    else:
        print("Invalid input!")

print(f"\nCount of Positive numbers: {positive}")
print(f"Count of Negative numbers: {negative}")
print(f"Count of Zeros: {zero}")