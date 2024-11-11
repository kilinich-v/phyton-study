number_input = 10

number = int(number_input)
factorial = 1

while number > 0:
    factorial = factorial * number
    number -= 1

print(f"Факторіл від числа {number_input}: {factorial}")