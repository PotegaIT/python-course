# © 2025 PotęgaIT – Python Course for Beginners

# Przykład 1 – sprawdzenie temperatury / Example 1 – checking the temperature
temperatura = 30
if temperatura > 25:
    print("Jest goraco!")  # Gdy temperatura przekracza 25 stopni / When the temperature is above 25 degrees

# Przykład 2 – if z else / Example 2 – if with else
temperatura = 25
if temperatura > 20:
    print("Cieplo")  # Gdy temperatura przekracza 20 stopni / When the temperature is above 20 degrees
else:
    print("Zimno")  # W przeciwnym razie / Otherwise

# Przykład 3 – if, elif i else z większą liczbą warunków / Example 3 – if, elif and else with more conditions
temperatura = 26
if temperatura > 25:
    print("Goraco")  # Gdy temperatura przekracza 25 / When the temperature is above 25
elif temperatura > 15:
    print("W sam raz")  # Gdy temperatura między 15 a 25 / When the temperature is between 15 and 25
else:
    print("Zimno")  # Gdy temperatura 15 lub mniej / When the temperature is 15 or less

# Przykład 4 – sprawdzenie wieku użytkownika / Example 4 – checking the user's age
wiek = int(input("Ile masz lat? "))  # Pobieramy wiek od użytkownika / We get the user's age from input

if wiek >= 18:
    print("Mozesz prowadzic samochod!")  # Gdy wiek to 18 lub więcej / When the age is 18 or more
    if wiek >= 70:
        print("Pamietaj o badaniach lekarskich  moga byc wymagane.")  # Osoby starsze – dodatkowe przypomnienie / Older people – additional reminder
elif wiek >= 16:
    print("Jeszcze troche poczekaj. Ale mozesz juz zaczac uczyc sie teorii!")  # 16–17 lat / 16–17 years old
else:
    print("Na razie jestes za mlody, ale wszystko przed Toba!")  # Mniej niż 16 lat / Less than 16 years old
