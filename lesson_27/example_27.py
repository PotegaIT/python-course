# Klasa Pies / Dog class
# Klasa to szablon (przepis), który opisuje jak będą wyglądały obiekty danego typu.
# A class is a template (recipe) that describes how objects of that type will look.

class Pies:
    # Metoda __init__() to konstruktor — uruchamia się automatycznie przy tworzeniu nowego obiektu.
    # The __init__() method is a constructor — it runs automatically when a new object is created.
    def __init__(self, imie, wiek):
        # self.imie i self.wiek to atrybuty obiektu (jego cechy).
        # self.imie and self.wiek are attributes (object properties).
        self.imie = imie
        self.wiek = wiek

    # Definiujemy metodę (czyli funkcję wewnątrz klasy), która sprawia, że pies szczeka.
    # We define a method (a function inside a class) that makes the dog bark.
    def szczekaj(self):
        print(f"{self.imie} mówi: Hau! Hau!")  # {self.imie} wstawia imię konkretnego psa.
        # {self.imie} inserts the dog's actual name.

# Tworzymy obiekt klasy Pies / Creating an object (instance) of class Dog
moj_pies = Pies("Reksio", 3)

# Wyświetlamy atrybuty obiektu / Displaying object attributes
print(moj_pies.imie)  # Reksio — imię psa / dog's name
print(moj_pies.wiek)  # 3 — wiek psa / dog's age

# Wywołujemy metodę obiektu / Calling the object's method
moj_pies.szczekaj()  # Reksio mówi: Hau! Hau! / Reksio says: Woof! Woof!


# Klasa Samochod / Car class
# Drugi przykład pokazujący klasę z trzema atrybutami i jedną metodą.
# Another example showing a class with three attributes and one method.
class Samochod: 
    def __init__(self, marka, model, rok): 
        # Atrybuty samochodu / Car attributes
        self.marka = marka 
        self.model = model 
        self.rok = rok 

    # Metoda opis() — wypisuje informacje o samochodzie
    # The opis() method — prints information about the car
    def opis(self): 
        print(f"Samochód: {self.marka} {self.model}, rok produkcji: {self.rok}")
        # The f-string displays car details in a formatted way.

# Tworzymy obiekt klasy Samochod / Creating an object (instance) of the Car class
moje_auto = Samochod("Toyota", "Corolla", 2020)

# Wywołujemy metodę opis(), aby zobaczyć dane samochodu
# Calling the opis() method to display the car's data
moje_auto.opis()  # Samochód: Toyota Corolla, rok produkcji: 2020
