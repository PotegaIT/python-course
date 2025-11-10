class Budzet: 
    def __init__(self): 
        # Inicjalizacja pustej listy wydatków / Initialize an empty list of expenses
        self.wydatki = [] 

    def dodaj_wydatek(self, opis, kwota): 
        # Dodaje nowy wydatek do listy wydatków / Adds a new expense to the list
        self.wydatki.append({"opis": opis, "kwota": kwota}) 

    def wyswietl_wydatki(self): 
        # Wyświetla wszystkie wydatki zapisane w budżecie / Displays all recorded expenses
        if not self.wydatki: 
            print("Brak wydatkow.")  # Gdy lista jest pusta / When the list is empty
            return 
        print("--- Lista wydatkow ---")  # Nagłówek listy / List header
        for idx, wydatek in enumerate(self.wydatki, 1): 
            # enumerate() dodaje numerację wydatków od 1 / enumerate() adds numbering starting from 1
            print(f"{idx}. {wydatek['opis']}: {wydatek['kwota']} zl") 

    def usun_wydatek(self, numer): 
        # Usuwa wydatek o podanym numerze z listy / Removes an expense by its number from the list
        if 0 < numer <= len(self.wydatki): 
            usuniety = self.wydatki.pop(numer - 1)  
            # Numer - 1, ponieważ indeksy w Pythonie zaczynają się od 0 / Subtract 1 because list indices start from 0
            print(f"Usunieto: {usuniety['opis']} za {usuniety['kwota']} zl") 
        else: 
            # Gdy użytkownik poda błędny numer / When user enters an invalid number
            print("Nieprawidlowy numer wydatku.") 

    def suma_wydatkow(self): 
        # Oblicza i wyświetla sumę wszystkich wydatków / Calculates and displays the total of all expenses
        suma = sum(w["kwota"] for w in self.wydatki) 
        print(f"Laczna suma wydatkow: {suma} zl")  


# Tworzymy obiekt klasy Budzet / Create an instance of the Budzet (Budget) class
budzet = Budzet() 

# Proste menu tekstowe do obsługi budżetu / Simple text menu for managing the budget
while True: 
    print("\nWybierz opcje:") 
    print("1. Dodaj wydatek") 
    print("2. Pokaz wydatki") 
    print("3. Usun wydatek") 
    print("4. Pokaz sume wydatkow") 
    print("5. Zakoncz") 

    wybor = input("Twoj wybor: ")  # Pobranie wyboru użytkownika / Get user's choice

    if wybor == "1": 
        # Dodawanie nowego wydatku / Adding a new expense
        opis = input("Podaj opis wydatku: ") 
        try: 
            kwota = float(input("Podaj kwote: ")) 
            # Próba konwersji kwoty na liczbę zmiennoprzecinkową / Try to convert amount to a float
            budzet.dodaj_wydatek(opis, kwota) 
        except ValueError: 
            # Obsługa błędu, gdy użytkownik nie poda liczby / Handle error if user enters non-numeric value
            print("Blad: kwota musi byc liczba.") 

    elif wybor == "2": 
        # Wyświetlenie listy wszystkich wydatków / Display all expenses
        budzet.wyswietl_wydatki() 

    elif wybor == "3": 
        # Usuwanie wydatku po numerze / Remove expense by its number
        try: 
            numer = int(input("Podaj numer wydatku do usuniecia: ")) 
            budzet.usun_wydatek(numer) 
        except ValueError: 
            # Gdy użytkownik nie poda liczby / When user does not enter a valid number
            print("Blad: musisz podac numer.") 

    elif wybor == "4": 
        # Wyświetlenie sumy wszystkich wydatków / Display total of all expenses
        budzet.suma_wydatkow() 

    elif wybor == "5": 
        # Zakończenie działania programu / End the program
        print("Zamykam program. Do zobaczenia!") 
        break 

    else: 
        # Obsługa niepoprawnego wyboru z menu / Handle invalid menu choice
        print("Niepoprawny wybor. Sprobuj jeszcze raz.") 
