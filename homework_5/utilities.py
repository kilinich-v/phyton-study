def calculate_average(numbers):
    for number in numbers:
        if(type(number) != int and type(number) != float):
            return print("The list contains a non-number value")
    return sum(numbers) / len(numbers)

def find_max(numbers):
    for number in numbers:
        if(type(number) != int and type(number) != float):
            return print("The list contains a non-number value")
    return max(numbers)