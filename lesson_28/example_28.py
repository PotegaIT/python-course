# =========================
# DZIEDZICZENIE / INHERITANCE
# =========================

# Klasa bazowa / Base class
class Pojazd:
    def __init__(self, marka, model):
        # Inicjalizacja atrybutów marka i model
        # Initialize the attributes 'marka' (brand) and 'model'
        self.marka = marka
        self.model = model

    def opis(self):
        # Metoda wyświetlająca opis pojazdu
        # Method to print the vehicle description
        print(f"Pojazd: {self.marka} {self.model}")

# Klasa dziedzicząca / Derived class
class Samochod(Pojazd):
    def __init__(self, marka, model, typ):
        # Wywołanie konstruktora klasy bazowej oraz dodanie atrybutu typ
        # Call the constructor of the base class and add the 'typ' attribute
        super().__init__(marka, model)
        self.typ = typ

    def opis_samochodu(self):
        # Metoda wyświetlająca opis samochodu wraz z typem
        # Method to print the car description including its type
        print(f"Samochod: {self.marka} {self.model}, typ: {self.typ}")

# Użycie klasy / Using the class
moj_samochod = Samochod("Toyota", "Corolla", "sedan")
moj_samochod.opis()              # metoda odziedziczona z Pojazd / inherited method from Pojazd
moj_samochod.opis_samochodu()    # metoda z klasy Samochod / method from Samochod class

# =========================
# ENKAPSULACJA / ENCAPSULATION
# =========================

class KontoBankowe: 
    def __init__(self, saldo): 
        # Prywatny atrybut saldo
        # Private attribute 'saldo'
        self.__saldo = saldo

    def pokaz_saldo(self): 
        # Metoda wyświetlająca aktualne saldo
        # Method to show current account balance
        print(f"Twoje saldo wynosi: {self.__saldo} zl") 

    def wplata(self, kwota): 
        # Metoda umożliwiająca wpłatę środków na konto
        # Method to deposit money into the account
        if kwota > 0: 
            self.__saldo += kwota 
            print(f"Wplacono: {kwota} zl") 
        else: 
            print("Kwota musi byc wieksza od zera.")  # Amount must be greater than zero

# Użycie klasy / Using the class
konto = KontoBankowe(1000) 
konto.pokaz_saldo()    # 1000
konto.wplata(500)      # wpłata 500
konto.pokaz_saldo()    # 1500

# =========================
# MINI PROJEKT / MINI PROJECT
# =========================

# Klasa bazowa Pracownik / Base class Employee
class Pracownik: 
    def __init__(self, imie, stanowisko): 
        # Inicjalizacja atrybutów imie i stanowisko
        # Initialize attributes 'imie' (name) and 'stanowisko' (position)
        self.imie = imie 
        self.stanowisko = stanowisko 

    def przedstaw_sie(self): 
        # Metoda przedstawiająca pracownika
        # Method to introduce the employee
        print(f"Czesc! Jestem {self.imie} i pracuje jako {self.stanowisko}.") 

# Klasa dziedzicząca Programista / Derived class Programmer
class Programista(Pracownik): 
    def __init__(self, imie, jezyk_programowania): 
        # Wywołanie konstruktora klasy bazowej i dodanie języka programowania
        # Call the base class constructor and add programming language attribute
        super().__init__(imie, "Programista") 
        self.jezyk_programowania = jezyk_programowania 

    def pokaz_umiejetnosci(self): 
        # Metoda wyświetlająca umiejętności programisty
        # Method to display programmer's skills
        print(f"Pisze programy w jezyku {self.jezyk_programowania}.") 

# Użycie klasy / Using the class
programista = Programista("Ania", "Python") 
programista.przedstaw_sie()        # metoda odziedziczona z Pracownik / inherited method from Pracownik
programista.pokaz_umiejetnosci()   # metoda klasy Programista / method from Programista
