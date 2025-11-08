# Kalkulator tekstowy - dodawanie i odejmowanie  
# Text calculator - addition and subtraction

print("Witaj w kalkulatorze tekstowym!")  
print("Welcome to the text calculator!")

print("Wybierz operacje: + (dodawanie), - (odejmowanie)")  
print("Choose an operation: + (addition), - (subtraction)")

# Powitanie użytkownika i wyświetlenie dostępnych operacji  
# Greet the user and display available operations

# Pobieramy operację  
# Get the chosen operation from the user
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
    # Wyświetlamy wynik dodawania  
    # Display the result of addition
elif operacja == "-":  
    wynik = liczba1 - liczba2  
    print("Wynik odejmowania:", wynik)  
    # Wyświetlamy wynik odejmowania  
    # Display the result of subtraction
else:  
    print("Nieznana operacja. Użyj + lub -.")  
    print("Unknown operation. Use + or -.")  
    # Obsługa błędnego symbolu operacji  
    # Handle an invalid operation symbol
