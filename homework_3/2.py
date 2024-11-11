numbers_of_try = [0, 1, 2, 3, 4, 5, 6, 7, 8]

days_of_week = {
    1: "Понеділок",
    2: "Вівторок",
    3: "Середа",
    4: "Четвер",
    5: "П'ятниця",
    6: "Субота",
    7: "Неділя"
}

for number in numbers_of_try:
    if number in days_of_week:
        print(f"{number} - {days_of_week[number]}")
    else:
        print(f"Дня з номером {number} не існує")