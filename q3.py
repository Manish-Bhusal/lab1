number = int(input("Enter a number to find its factorial: "))
print(f"You have entered: {number}")
factorial = 1

while number > 1:
    factorial *= number
    number -= 1         

print(f"The factorial {number}! of the number is {factorial}.")
