# Pętla for po liście / For loop over a list
owoce = ["jablko", "banan", "gruszka"]
for owoc in owoce:
    print("Owoc to:", owoc)  # Wypisuje każdy owoc z listy / Prints each fruit in the list

print()

# Pętla for po krotce / For loop over a tuple
osoba = ("Anna", "Nowak", 28)
for element in osoba:
    print("Element krotki:", element)  # Wypisuje każdy element krotki / Prints each element of the tuple

print()

# Pętla for po zbiorze / For loop over a set
kolory = {"czerwony", "zielony", "niebieski"}
for kolor in kolory:
    print("Kolor:", kolor)  # Wypisuje każdy element zbioru (kolejność może się różnić) / Prints each element in the set (order may vary)

print()

# Pętla for po kluczach słownika / For loop over dictionary keys
osoba = {
    "imie": "Anna",
    "nazwisko": "Nowak",
    "wiek": 28
}

for klucz in osoba:
    print("Klucz:", klucz)  # Wypisuje każdy klucz słownika / Prints each key in the dictionary

print()

# Pętla for po parach klucz-wartość / For loop over dictionary key-value pairs
for klucz, wartosc in osoba.items():
    print(f"{klucz}: {wartosc}")  # Wypisuje klucz i odpowiadającą wartość / Prints key and value

print()

# Pętla for z range – od 0 do 4 / For loop with range – from 0 to 4
for i in range(5):
    print("Liczba:", i)  # Wypisuje liczby od 0 do 4 / Prints numbers 0 to 4

print()

# Pętla while – liczenie do 2 / While loop – counting to 2
liczba = 0
while liczba < 3:
    print("Liczba to:", liczba)  # Wypisuje aktualną wartość liczby / Prints the current number
    liczba += 1  # Zwiększa liczbę o 1 / Increments the number

print()

# Pętla while – dopóki użytkownik nie wpisze "python" / While loop – until user enters "python"
haslo = ""
while haslo != "python":
    haslo = input("Podaj hasło: ")  # Powtarza dopóki użytkownik nie wpisze "python" / Repeats until user types "python"

print("Dostęp przyznany!")  # Wypisuje komunikat, gdy hasło jest poprawne / Prints access granted

print()

# Pętla while bez zmiany warunku (nieskończona, ale uwaga – zatrzymana w przykładzie!) / While loop with no condition change (infinite, but stopped in this example)
licznik = 0
while licznik < 3:
    print("Nigdy się nie kończę!")  
    # licznik += 1  #  Odkomentuj, by zakończyć pętlę po 3 iteracjach / Uncomment to end the loop after 3 iterations
    break  # Tymczasowo wstawione, by nie zablokować działania programu / Temporarily added to prevent freezing the program
