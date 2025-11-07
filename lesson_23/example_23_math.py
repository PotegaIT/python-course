import matematyka  # Importuje własny moduł matematyka / Import your custom module matematyka

liczby = []  # Lista do przechowywania wprowadzonych liczb / List to store user-input numbers

# Pętla do wprowadzania 5 liczb / Loop to input 5 numbers
for i in range(5):
    n = int(input(f"Podaj liczbe {i + 1}: "))  # Pobiera liczbę od użytkownika / Get a number from the user
    liczby.append(n)  # Dodaje liczbę do listy / Add the number to the list

print("Kwadraty liczb:")  # Informacja o wyświetlanych kwadratach / Info about printing squares
for l in liczby:
    print(matematyka.kwadrat(l))  # Wywołanie funkcji kwadrat z modułu / Call the square function from the module

print("Srednia:", matematyka.srednia(liczby))  # Wywołanie funkcji średnia / Call the average function

# Sprawdzenie parzystości każdej liczby / Check if each number is even
for l in liczby:
    if matematyka.czy_parzysta(l):  # Wywołanie funkcji czy_parzysta / Call the is_even function
        print(f"{l} jest parzysta.")  # Wynik dla liczby parzystej / Result for an even number
    else:
        print(f"{l} jest nieparzysta.")  # Wynik dla liczby nieparzystej / Result for an odd number
