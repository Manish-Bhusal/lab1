print("Armdtrong Numbers between 100 and 999.")

for num in range(100, 1000):
    digit1 = num // 100 #Hundreds digit
    digit2 = (num // 10) % 10 #Tens digit
    digit3 = num % 10 #Ones digit

    sum_of_cubes = digit1**3 + digit2**3 + digit3**3

    if sum_of_cubes == num:
        print(num, end = " ")