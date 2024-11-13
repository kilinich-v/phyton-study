countries_and_capitals = {
    "Україна": "Київ",
    "Франція": "Париж",
    "Німеччина": "Берлін",
    "Італія": "Рим",
    "Іспанія": "Мадрид"
}

country = input("Введіть назву країни: ")

if country in countries_and_capitals:
    print(f"Столиця {country}: {countries_and_capitals[country]}")
else:
    print(f"Країни {country} немає у словнику")