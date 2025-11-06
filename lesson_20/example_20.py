# Próbujemy wykonać operacje, które mogą zakończyć się błędem / We try to perform operations that may cause an error
try:
    liczba = int(input("Podaj liczbe: "))  # Pobieramy liczbę od użytkownika i zamieniamy na typ całkowity / Get a number from the user and convert it to an integer
    wynik = 10 / liczba                    # Dzielimy 10 przez podaną liczbę (może wystąpić dzielenie przez 0) / Divide 10 by the given number (division by zero may occur)
    print("Wynik to:", wynik)              # Wyświetlamy wynik dzielenia / Display the division result

# Obsługa wyjątku, gdy użytkownik poda 0 – nie można dzielić przez zero / Handle exception when the user enters 0 – division by zero is not allowed
except ZeroDivisionError: 
    print("Nie mozna dzielic przez zero!")    # Komunikat o błędzie dzielenia przez zero / Error message for division by zero

# Obsługa wyjątku, gdy użytkownik wpisze coś, co nie jest liczbą (np. tekst) / Handle exception when user enters something that is not a number (e.g., text)
except ValueError: 
    print("Musisz podac poprawna liczbe!")    # Komunikat o błędnym typie danych / Error message for invalid input type

# Kolejna instrukcja try-except – operacja na pliku / Another try-except block – file operation
try: 
    plik = open("dane.txt", "r")          # Próbujemy otworzyć plik "dane.txt" w trybie do odczytu / Try to open the file "dane.txt" in read mode
    zawartosc = plik.read()               # Czytamy całą zawartość pliku / Read the entire content of the file
    print(zawartosc)                      # Wyświetlamy zawartość pliku / Display the file content

# Obsługa wyjątku, gdy plik nie istnieje w katalogu / Handle exception when the file does not exist in the directory
except FileNotFoundError: 
    print("Plik nie istnieje.")           # Informacja o braku pliku / Information that the file does not exist

# Blok finally wykona się zawsze – niezależnie czy wystąpił wyjątek, czy nie / The finally block always executes – whether an exception occurred or not
finally: 
    print("Koniec operacji na pliku.")    # Komunikat kończący operację na pliku / Message indicating the end of the file operation
