# Kalkulator tekstowy - dodawanie i odejmowanie  
# Text calculator - addition and subtraction

print("Witaj w kalkulatorze tekstowym!")  
print("Wybierz operacje: + (dodawanie), - (odejmowanie)")  
# Powitanie użytkownika i wyświetlenie dostępnych operacji  
# Greet the user and display available operations

# Pobieramy operacje  
# Get the chosen operation from the user
operacja = input("Podaj operacje: ")

# Pobieramy liczby  
# Get numbers from the user
liczba1 = float(input("Podaj pierwszą liczbe: "))  
liczba2 = float(input("Podaj druga liczbe: "))

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
    print("Nieznana operacja. Uzyj + lub -.")  
    # Obsługa błędnego symbolu operacji  
    # Handle an invalid operation symbol
