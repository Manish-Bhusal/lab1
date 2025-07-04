number = int(input("Enter a number: "))
print(f"The multiplication table of {number} is given below.")

for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")