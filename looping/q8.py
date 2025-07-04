num = int(input("Enter a number to check whether it is a Palindrome or not : "))
originalNumber = num
sumOfNumber = 0

while num != 0:
    digit = num % 10
    sumOfNumber = sumOfNumber * 10 + digit
    num //= 10

if(originalNumber == sumOfNumber):
    print("Is palindrome.")
else:
    print("Just an ordinary number.")
