# Kalkulator tekstowy - dodawanie, odejmowanie, mnożenie i dzielenie
# Text calculator - addition, subtraction, multiplication, and division

print("Witaj w kalkulatorze tekstowym!")
print("Welcome to the text calculator!")

print("Wybierz operacje: + (dodawanie), - (odejmowanie), * (mnożenie), / (dzielenie)")
print("Choose an operation: + (addition), - (subtraction), * (multiplication), / (division)")

# Pobieramy operację
# Get the operation from the user
operacja = input("Podaj operację: ")

# Pobieramy liczby
# Get numbers from the user
liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))

# Wykonujemy obliczenia na podstawie wybranej operacji
# Perform the calculation based on the chosen operation
if operacja == "+":
    wynik = liczba1 + liczba2
    print("Wynik dodawania:", wynik)
elif operacja == "-":
    wynik = liczba1 - liczba2
    print("Wynik odejmowania:", wynik)
elif operacja == "*":
    wynik = liczba1 * liczba2
    print("Wynik mnożenia:", wynik)
elif operacja == "/":
    # Sprawdzamy, czy druga liczba nie jest zerem
    # Check if the second number is not zero
    if liczba2 != 0:
        wynik = liczba1 / liczba2
        print("Wynik dzielenia:", wynik)
    else:
        print("Błąd: nie można dzielić przez zero!")
        print("Error: cannot divide by zero!")
else:
    print("Nieznana operacja. Użyj +, -, * lub /.")
    print("Unknown operation. Use +, -, * or /.")
