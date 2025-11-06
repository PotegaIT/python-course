# Definicja funkcji kalkulator / Definition of the calculator function
def kalkulator(): 
    try: 
        # Pobranie pierwszej liczby od użytkownika i konwersja na typ zmiennoprzecinkowy (float) / Get the first number from the user and convert to float
        a = float(input("Podaj pierwsza liczbe: ")) 
        
        # Pobranie drugiej liczby i konwersja na float / Get the second number and convert to float
        b = float(input("Podaj druga liczbe: ")) 
        
        # Próba wykonania dzielenia – może wystąpić błąd jeśli b == 0 / Attempt division – may raise error if b == 0
        wynik = a / b 
        
        # Jeśli wszystko się udało, wyświetlamy wynik / If successful, print the result
        print("Wynik dzielenia:", wynik) 

    # Obsługa błędu – jeśli użytkownik podał coś, czego nie da się zamienić na liczbę / Handle error if input cannot be converted to a number
    except ValueError: 
        print("Wprowadz prawidlowa liczbe!") 

    # Obsługa błędu – jeśli użytkownik podał 0 jako drugą liczbę (dzielenie przez zero) / Handle error if user enters 0 as the second number (division by zero)
    except ZeroDivisionError: 
        print("Nie dzielimy przez zero!") 

# Wywołanie funkcji kalkulator – uruchomienie programu / Call the calculator function to run the program
kalkulator()  
