import random           # Importuje moduł do losowania liczb i wyborów / Import the module for random numbers and choices
import datetime         # Importuje moduł do pracy z datą i czasem / Import the module for working with date and time
import math             # Importuje moduł matematyczny (np. pierwiastki, potęgi, stałe) / Import the math module (e.g., square roots, powers, constants)

# --- Przykłady funkcji matematycznych / Math examples ---
print("Pierwiastek z 16:", math.sqrt(16))          # Oblicza pierwiastek kwadratowy z 16 / Calculates the square root of 16
print("2 do potegi 3:", math.pow(2, 3))            # Oblicza 2 do potęgi 3 (czyli 8) / Calculates 2 to the power of 3 (8)
print("Wartosc bezwzgledna z -5:", math.fabs(-5))  # Zwraca wartość bezwzględną liczby -5 / Returns the absolute value of -5
print("Liczba Pi:", math.pi)                        # Wypisuje wartość liczby π / Prints the value of π (Pi)

# --- Przykłady funkcji losowych / Random examples ---
print("Losowa liczba od 1 do 10:", random.randint(1, 10))                   # Losuje liczbę całkowitą od 1 do 10 / Random integer between 1 and 10
print("Losowy wybor z listy:", random.choice(["kot", "pies", "mysz"]))      # Losowo wybiera element z listy / Randomly selects an element from a list

# --- Praca z datą i czasem / Date and time examples ---
teraz = datetime.datetime.now()               # Pobiera aktualną datę i godzinę / Gets the current date and time
print("Aktualna data i godzina:", teraz)     # Wyświetla aktualną datę i godzinę / Prints the current date and time

konkretna_data = datetime.datetime(2023, 12, 31)  # Tworzy obiekt daty dla 31 grudnia 2023 / Creates a datetime object for December 31, 2023
print("Sylwester:", konkretna_data)                # Wyświetla konkretną datę / Prints the specific date

# --- Mini gra: zgadnij liczbę / Mini game: Guess the number ---
liczba = random.randint(1, 100)      # Losuje tajną liczbę od 1 do 100 / Generate a secret number between 1 and 100
start = datetime.datetime.now()       # Zapisuje czas rozpoczęcia gry / Record the start time
proby = 0                             # Licznik prób gracza / Attempt counter initialized to 0

# Pętla zgadywania / Guessing loop
while True:
    strzal = int(input("Zgadnij liczbe od 1 do 100: "))  # Pobiera strzał użytkownika jako liczbę całkowitą / Get user's guess as an integer
    proby += 1                                           # Zwiększa licznik prób / Increment the attempts counter

    if strzal == liczba:         # Jeśli zgadł poprawnie / If the guess is correct
        break                    # Kończy pętlę / Exit the loop
    elif strzal < liczba:        # Jeśli liczba jest za mała / If the guess is too low
        print("Za malo!")        # Informacja dla użytkownika / Inform the user
    else:                        # Jeśli liczba jest za duża / If the guess is too high
        print("Za duzo!")        # Informacja dla użytkownika / Inform the user

koniec = datetime.datetime.now()  # Zapisuje czas zakończenia gry / Record the end time
czas = koniec - start             # Oblicza czas trwania gry / Calculate the duration of the game

bazowa_wartosc = max(1, 10 - proby)        # Bazowa wartość punktów / Base score value (fewer attempts = higher score, min 1)
punkty = math.pow(bazowa_wartosc, 2) * 10  # Wylicza punkty na podstawie liczby prób / Calculate score: base value squared times 10

print(f"Twoj wynik punktowy: {int(punkty)} punktow!")  # Wyświetla wynik punktowy gracza / Prints the player's score
print("Zajelo Ci to:", czas)                          # Wyświetla czas trwania gry / Prints how long the game took

optymalna_liczba_prob = math.ceil(math.log2(100))      # Szacuje optymalną liczbę prób dla metody „połówek” / Estimates optimal number of attempts using "halving" method
print("🔍 Teoretycznie, przy metodzie 'połówek', można było zgadnąć w maksymalnie", optymalna_liczba_prob, "próbach.")  # Informuje o teorii / Prints theoretical maximum attempts
