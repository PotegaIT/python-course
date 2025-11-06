# Definicja funkcji bez parametrów / Defining a function without parameters
def przywitaj(): 
    print("Czesc! Milo Cie widziec!")  # Wyświetla proste powitanie / Prints a simple greeting

# Wywołanie funkcji – uruchomienie tego, co jest w środku / Calling the function – executes its code
przywitaj()  


# Teraz definiujemy funkcję przyjmującą jeden parametr (imię) / Defining a function with one parameter (name)
def przywitaj(imie): 
    print("Czesc", imie + "!")  # Wyświetla powitanie z podanym imieniem / Prints a greeting with the given name

# Wywołania funkcji z różnymi imionami / Calling the function with different names
przywitaj("Ania") 
przywitaj("Tomek")  


# Funkcja przyjmująca dwa argumenty i zwracająca ich sumę / Function that takes two arguments and returns their sum
def dodaj(a, b): 
    suma = a + b              # Dodawanie dwóch liczb / Adding two numbers
    return suma               # Zwrócenie wyniku do miejsca wywołania / Returning the result to the caller

wynik = dodaj(3, 5)           # Przechowanie zwróconej wartości w zmiennej 'wynik' / Storing the returned value in variable 'wynik'
print("Wynik dodawania:", wynik)         # Wypisanie wyniku (wersja 1) / Print result (version 1)
print(f"Wynik dodawania:{wynik}")        # Wypisanie wyniku z użyciem f-stringa (wersja 2) / Print result using f-string (version 2)


# Funkcja mnożąca trzy liczby / Function multiplying three numbers
def mnoz(a, b, c): 
    return a * b * c         # Zwraca wynik mnożenia trzech wartości / Returns the product of three values

wynik = mnoz(2, 3, 4)        # Wywołanie funkcji z trzema argumentami / Calling the function with three arguments
print("Wynik mnozenia:", wynik)  # Wyświetlenie wyniku / Print the result


# Funkcja bez parametrów, ale zwracająca tekst / Function without parameters, returning text
def powitanie(): 
    return "Witaj w programowaniu!"  # Zwraca łańcuch znaków / Returns a string

tekst = powitanie()          # Zapisanie zwróconej wartości do zmiennej / Store the returned value in a variable
print(tekst)                 # Wyświetlenie tekstu / Print the text
