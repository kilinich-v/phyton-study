import calculator

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
operation = input("Введіть операцію (додавання, віднімання, множення, ділення): ").strip().lower()

if operation == "додавання":
    result = calculator.add(num1, num2)
elif operation == "віднімання":
    result = calculator.subtract(num1, num2)
elif operation == "множення":
    result = calculator.multiply(num1, num2)
elif operation == "ділення":
    result = calculator.divide(num1, num2)
else:
    result = "Невідома операція"

print(f"Результат: {result}")