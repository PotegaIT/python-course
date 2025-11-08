# Kalkulator tekstowy z pętlą i możliwością powtarzania operacji  
# Text calculator with a loop and the ability to repeat operations

while True:
    print("\nWitaj w kalkulatorze tekstowym!")  
    print("Welcome to the text calculator!")

    print("Wybierz operację: + (dodawanie), - (odejmowanie), * (mnożenie), / (dzielenie)")  
    print("Choose an operation: + (addition), - (subtraction), * (multiplication), / (division)")

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
        print("Result of addition:", wynik)
        # Wyświetlamy wynik dodawania  
        # Display the result of addition
    elif operacja == "-":  
        wynik = liczba1 - liczba2  
        print("Wynik odejmowania:", wynik)  
        print("Result of subtraction:", wynik)
        # Wyświetlamy wynik odejmowania  
        # Display the result of subtraction
    elif operacja == "*":  
        wynik = liczba1 * liczba2  
        print("Wynik mnożenia:", wynik)  
        print("Result of multiplication:", wynik)
        # Wyświetlamy wynik mnożenia  
        # Display the result of multiplication
    elif operacja == "/":  
        if liczba2 != 0:  
            wynik = liczba1 / liczba2  
            print("Wynik dzielenia:", wynik)  
            print("Result of division:", wynik)
            # Wyświetlamy wynik dzielenia  
            # Display the result of division
        else:  
            print("Błąd: nie można dzielić przez zero!")  
            print("Error: cannot divide by zero!")  
            # Obsługa błędu dzielenia przez zero  
            # Handle division by zero error
    else:  
        print("Nieznana operacja. Użyj +, -, * lub /.")  
        print("Unknown operation. Use +, -, * or /.")  
        # Obsługa błędnego symbolu operacji  
        # Handle an invalid operation symbol

    # Pytamy, czy użytkownik chce kontynuować  
    # Ask the user if they want to perform another operation
    kontynuować = input("Czy chcesz wykonać kolejną operację? (tak/nie): ").lower()  
    if kontynuować != "tak":  
        print("Dziękujemy za korzystanie z kalkulatora!")  
        print("Thank you for using the calculator!")  
        # Pożegnanie użytkownika i zakończenie programu  
        # Say goodbye to the user and end the program
        break
