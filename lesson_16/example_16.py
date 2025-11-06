# Definicja funkcji z domyślnym argumentem "imie" / Defining a function with default argument "name"
def przywitaj(imie="Gosciu"):
    print("Czesc,", imie)  # Wyświetla powitanie w języku polskim / Prints a greeting in Polish

przywitaj()        # Użyje wartości domyślnej ("Gosciu") / Uses the default value ("Guest")
przywitaj("Ania")  # Nadpisze domyślną wartość – poda "Ania" / Overrides the default value – provides "Anna"


# Nadpisanie poprzedniej funkcji – teraz dodajemy obsługę języka / Overwriting the previous function – now adding language support
def przywitaj(imie="Gosciu", jezyk="polski"):
    if jezyk == "angielski":
        print("Hello,", imie)  # Jeśli język to angielski – witaj po angielsku / If language is English – greet in English
    else:
        print("Czesc,", imie)  # W przeciwnym razie – witaj po polsku / Otherwise – greet in Polish

przywitaj()                  # Używa domyślnych wartości ("Gosciu", "polski") → Czesc, Gosciu / Uses default values ("Guest", "Polish") → Czesc, Gosciu
przywitaj("Anna")            # Podaje tylko imię, język zostaje domyślny → Czesc, Anna / Provides only name, language remains default → Czesc, Anna
przywitaj("Tom", "angielski")  # Imię i język podane jawnie → Hello, Tom / Name and language explicitly provided → Hello, Tom


# Funkcja zwracająca tekst powitania (a nie tylko go drukująca) / Function returning greeting text (not just printing it)
def powitanie(imie="Przyjaciel", jezyk="polski"): 
    if jezyk == "angielski": 
        return f"Hello, {imie}!"          # Powitanie po angielsku / Greeting in English
    elif jezyk == "hiszpanski": 
        return f"Hola, {imie}!"           # Powitanie po hiszpańsku / Greeting in Spanish
    else: 
        return f"Czesc, {imie}!"          # Domyślne powitanie po polsku / Default greeting in Polish

# Wyświetlenie wyników działania funkcji powitanie() / Displaying the results of the greeting() function
print(powitanie())                            # Domyślne: Czesc, Przyjaciel! / Default: Czesc, Friend!
print(powitanie("Anna"))                      # Podano imię, ale język domyślny → Czesc, Anna! / Name provided, default language → Czesc, Anna!
print(powitanie("Carlos", "hiszpanski"))      # Imię i język hiszpański → Hola, Carlos! / Name and Spanish language → Hola, Carlos!
print(powitanie(jezyk="angielski"))           # Tylko język, imię domyślne → Hello, Przyjaciel! / Only language provided, default name → Hello, Friend!
