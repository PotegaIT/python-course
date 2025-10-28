# --- KROTKA (tuple) ---
osoba = ("Anna", "Nowak", 28)
print("Krotka osoba:", osoba)  # Tuple 'osoba': contains multiple pieces of information, immutable

print("Imie z krotki:", osoba[0])  # Accessing the first element of the tuple (index 0)

# Rozpakowanie krotki do zmiennych / Unpacking tuple into variables
imie, nazwisko, wiek = osoba
print("Imie:", imie, "| Wiek:", wiek)  # Printing individual variables extracted from tuple

print()

# --- SŁOWNIK (dict) ---
osoba = {
    "imie": "Anna",
    "nazwisko": "Nowak",
    "wiek": 28
}
print("Słownik osoba:", osoba)  # Dictionary 'osoba': stores data in key:value pairs

print("Imie ze słownika:", osoba["imie"])  # Accessing value by key

# Dodanie nowej pary klucz-wartość / Adding a new key:value pair
osoba["miasto"] = "Krakow"

# Modyfikacja istniejącej wartości / Modifying existing value
osoba["wiek"] = 29

print("Po dodaniu miasta i zmianie wieku:", osoba)

# Usunięcie elementu ze słownika / Deleting an element from dictionary
del osoba["nazwisko"]
print("Po usunięciu nazwiska:", osoba)

print()

# --- ZBIÓR (set) ---
kolory = {"czerwony", "zielony", "niebieski", "zielony"}  # duplikaty są automatycznie usuwane / duplicates removed automatically
print("Zbiór kolory:", kolory)

# Dodanie nowego elementu do zbioru / Adding a new element to the set
kolory.add("zolty")

# Usunięcie elementu ze zbioru / Removing an element from the set
kolory.remove("czerwony")

print("Zbiór po zmianach:", kolory)

# Sprawdzenie obecności elementu w zbiorze / Checking if an element exists in the set
print("Czy 'zielony' jest w zbiorze?", "zielony" in kolory)
