# Pobieranie imienia od użytkownika / Getting the user's name
name = input("Jak masz na imię? / What is your name? ")

# Pobieranie wieku od użytkownika (jako tekst) / Getting the user's age (as text)
age = input("Ile masz lat? / How old are you? ")

# Powitanie użytkownika z użyciem f-stringa / Greeting the user using an f-string
print(f"Witaj, {name}! / Hello, {name}!")

# Wyświetlenie wieku za rok - konwersja do int potrzebna, bo input zwraca string / Showing the user's age next year - conversion to int is needed because input returns a string
print(f"Za rok będziesz miał {int(age) + 1} lat. / Next year you will be {int(age) + 1} years old.")


# Kolejne pobieranie danych od użytkownika: imię, wiek i miasto / Next, getting more data from the user: name, age and city
name = input("Jak masz na imię? / What is your name? ")
age = input("Ile masz lat? / How old are you? ")
city = input("Z jakiego jesteś miasta? / Which city are you from? ")

# Prezentacja danych znowu za pomocą f-stringów / Displaying the data again using f-strings
print(f"\nCześć, {name}! / Hi, {name}!")
print(f"Masz {age} lat i mieszkasz w {city}. / You are {age} years old and you live in {city}.")
print(f"Za 5 lat będziesz mieć {int(age) + 5} lat. To ciekawa perspektywa, prawda? / In 5 years you will be {int(age) + 5} years old. That's an interesting perspective, right?")
