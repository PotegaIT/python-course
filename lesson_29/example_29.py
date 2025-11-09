# -------------------------------
# Klasa Produkt / Product class
# -------------------------------

class Produkt: 
    def __init__(self, nazwa, cena): 
        # Inicjalizacja produktu z nazwą i ceną
        # Initialize a product with a name and a price
        self.nazwa = nazwa 
        self.cena = cena 

# -------------------------------
# Klasa PozycjaZamowienia / OrderItem class
# -------------------------------

class PozycjaZamowienia: 
    def __init__(self, produkt, ilosc): 
        # Inicjalizacja pozycji zamówienia z produktem i ilością
        # Initialize an order item with a product and quantity
        self.produkt = produkt 
        self.ilosc = ilosc 

    def cena_laczna(self): 
        # Oblicza łączną cenę pozycji (cena produktu * ilość)
        # Calculate the total price of the order item (product price * quantity)
        return self.produkt.cena * self.ilosc 

# -------------------------------
# Klasa Zamowienie / Order class
# -------------------------------

class Zamowienie: 
    def __init__(self): 
        # Tworzy pustą listę pozycji zamówienia
        # Create an empty list to store order items
        self.pozycje = [] 

    def dodaj_pozycje(self, pozycja): 
        # Dodaje pozycję do zamówienia
        # Add an order item to the order
        self.pozycje.append(pozycja) 

    def podsumowanie(self): 
        # Wyświetla podsumowanie zamówienia i sumuje ceny wszystkich pozycji
        # Display the order summary and calculate the total cost
        suma = 0 
        print("--- Podsumowanie zamowienia / Order Summary ---") 
        for pozycja in self.pozycje: 
            nazwa = pozycja.produkt.nazwa       # Nazwa produktu / Product name
            ilosc = pozycja.ilosc               # Ilość sztuk / Quantity
            cena_jednostkowa = pozycja.produkt.cena  # Cena jednostkowa / Unit price
            cena_laczna = pozycja.cena_laczna()      # Cena całkowita pozycji / Total price for this item
            suma += cena_laczna                 # Sumowanie ceny całkowitej zamówienia / Add to total order sum
            print(f"{nazwa} x{ilosc} @ {cena_jednostkowa}zl = {cena_laczna}zl") 
        print(f"Laczna kwota do zaplaty / Total amount to pay: {suma}zl") 

# -------------------------------
# Tworzenie produktów / Creating products
# -------------------------------

chleb = Produkt("Chleb", 4.6)    # Produkt chleb za 4.6 zł / Product bread for 4.6 PLN
mleko = Produkt("Mleko", 3.7)    # Produkt mleko za 3.7 zł / Product milk for 3.7 PLN
jajka = Produkt("Jajka", 0.8)    # Produkt jajka za 0.8 zł / Product eggs for 0.8 PLN

# -------------------------------
# Tworzenie pozycji zamówienia / Creating order items
# -------------------------------

pozycja1 = PozycjaZamowienia(chleb, 5)  # 5 chlebów / 5 breads
pozycja2 = PozycjaZamowienia(mleko, 6)  # 6 mleka / 6 milks
pozycja3 = PozycjaZamowienia(jajka, 12) # 12 jajek / 12 eggs

# -------------------------------
# Tworzenie zamówienia i dodanie pozycji / Creating order and adding items
# -------------------------------

zamowienie = Zamowienie() 
zamowienie.dodaj_pozycje(pozycja1) 
zamowienie.dodaj_pozycje(pozycja2) 
zamowienie.dodaj_pozycje(pozycja3) 

# -------------------------------
# Wyświetlenie podsumowania / Displaying the order summary
# -------------------------------

zamowienie.podsumowanie()  # Pokazuje wszystkie produkty, ilości, ceny i sumę / Shows all products, quantities, prices and total
