## 🇵🇱 Wersja polska

# Lekcja 29: Praktyczny przykład – system zamówień

---

## 🧠 Wprowadzenie

> Dzisiaj pokażę Ci, jak stworzyć prosty, ale bardzo praktyczny system zamówień. W ten sposób zobaczysz,
jak klasy i obiekty mogą ze sobą współpracować w prawdziwym programie.
Nauczysz się tworzyć strukturę, która przypomina system sklepowy – 
będziemy dodawać produkty do koszyka, liczyć łączną cenę i wyświetlać podsumowanie.
Wszystko zrobimy krok po kroku i omówię każdą linię kodu.

---

## 📋 1. Plan programu

Zanim przejdziemy do kodu, opowiem Ci, jak będzie wyglądał nasz system. Zbudujemy go z trzech klas:

* **Produkt** – reprezentuje pojedynczy produkt, np. chleb, mleko.
* **PozycjaZamowienia** – łączy produkt i jego ilość (np. 2 chleby).
* **Zamowienie** – zbiór pozycji, czyli pełne zamówienie z możliwością podsumowania.

Dzięki takiemu podziałowi mamy porządek i możemy łatwo rozbudowywać program w przyszłości.

---

## 🧱 2. Klasa Produkt

Zaczynamy od podstawowego elementu – pojedynczego produktu. Klasa będzie bardzo prosta:   
potrzebujemy tylko nazwy i ceny.

```python
class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena
```

### 🗣️ Wyjaśnienie:

* `__init__` – konstruktor, metoda wywoływana automatycznie przy tworzeniu obiektu.
* `self.nazwa` i `self.cena` – przechowują nazwę i cenę produktu.
* Dzięki temu możemy tworzyć różne produkty, np. `Produkt("Chleb", 4.5)`.

---

## 🧮 3. Klasa PozycjaZamowienia

Teraz stworzymy klasę, która łączy produkt z ilością – czyli coś w rodzaju pozycji w koszyku sklepowym.
Dodatkowo dodamy metodę, która policzy koszt tej pozycji.

```python
class PozycjaZamowienia:
    def __init__(self, produkt, ilosc):
        self.produkt = produkt
        self.ilosc = ilosc

    def cena_laczna(self):
        return self.produkt.cena * self.ilosc
```

### 🗣️ Wyjaśnienie:

* Konstruktor przyjmuje obiekt `Produkt` i ilość sztuk.
* `cena_laczna()` – zwraca wartość całej pozycji (np. 3 mleka = 9.6 zł).

---

## 📦 4. Klasa Zamowienie

Teraz czas na klasę, która będzie przechowywać wszystkie pozycje zamówienia.
Dodamy możliwość dodawania pozycji i wyświetlania podsumowania.

```python
class Zamowienie:
    def __init__(self):
        self.pozycje = []

    def dodaj_pozycje(self, pozycja):
        self.pozycje.append(pozycja)

    def podsumowanie(self):
        suma = 0
        print("--- Podsumowanie zamówienia ---")
        for pozycja in self.pozycje:
            nazwa = pozycja.produkt.nazwa
            ilosc = pozycja.ilosc
            cena_jednostkowa = pozycja.produkt.cena
            cena_laczna = pozycja.cena_laczna()
            suma += cena_laczna
            print(f"{nazwa} x{ilosc} @ {cena_jednostkowa}zł = {cena_laczna}zł")
        print(f"Łączna kwota do zapłaty: {suma}zł")
```

### 🗣️ Wyjaśnienie:

* `self.pozycje = []` – lista przechowująca obiekty `PozycjaZamowienia`.
* `dodaj_pozycje()` – dodaje obiekt do listy.
* `podsumowanie()` – iteruje po wszystkich pozycjach, wyciąga nazwę, ilość, cenę jednostkową i sumę pozycji. Na końcu podaje łączną kwotę.

---

## 🧪 5. Przykładowe użycie programu

```python
# Tworzenie produktów
chleb = Produkt("Chleb", 4.5)
mleko = Produkt("Mleko", 3.2)
jajka = Produkt("Jajka", 0.8)

# Tworzenie pozycji
pozycja1 = PozycjaZamowienia(chleb, 2)
pozycja2 = PozycjaZamowienia(mleko, 3)
pozycja3 = PozycjaZamowienia(jajka, 10)

# Tworzenie zamówienia i dodanie pozycji
zamowienie = Zamowienie()
zamowienie.dodaj_pozycje(pozycja1)
zamowienie.dodaj_pozycje(pozycja2)
zamowienie.dodaj_pozycje(pozycja3)

# Wyświetlenie podsumowania
zamowienie.podsumowanie()
```

### 🗣️ Wyjaśnienie:

* Tworzymy produkty i łączymy je z ilością w obiekty `PozycjaZamowienia`.
* Dodajemy je do `Zamowienie`.
* Wywołanie `podsumowanie()` pokazuje pełny rachunek – jak mini system sklepu.

---

## 📝 6. Zadanie domowe

Rozbuduj system zamówień w jeden z poniższych sposobów:

* Dodaj możliwość naliczania rabatu procentowego na całe zamówienie.
* Dodaj metodę usuwania pozycji z zamówienia.
* Dodaj możliwość zmiany ilości danego produktu.
* Zapisz podsumowanie zamówienia do pliku tekstowego.

Dzięki temu przećwiczysz operacje na listach, metody klas i rozbudowę programu obiektowego.

---

## ✅ Podsumowanie lekcji

Dziś stworzyliśmy mini system zamówień – prosty, ale odzwierciedlający rzeczywiste zastosowania.
Widzisz, jak klasy współpracują: produkt zna swoją cenę, pozycja wie ile sztuk i jak to przeliczyć, a zamówienie potrafi zebrać wszystko i podsumować.
To właśnie siła programowania obiektowego – podział na logiczne części, które razem tworzą całość.

© 2025 PotęgaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version

# Lesson 29: Practical Example – Order System

---

## 🧠 Introduction

> Today, I’ll show you how to create a simple but very practical order system. This way, you’ll see how classes and objects can work together in a real program.  
You will learn how to create a structure similar to a store system –  
we will add products to a shopping cart, calculate the total price, and display a summary.  
We’ll do everything step by step, and I’ll explain each line of code.

---

## 📋 1. Program Plan

Before we dive into the code, let me explain how our system will look. We will build it with three classes:

* **Product** – represents a single product, e.g., bread, milk.  
* **OrderItem** – combines a product and its quantity (e.g., 2 breads).  
* **Order** – a collection of items, representing a complete order with a summary feature.

This division keeps things organized and makes it easy to extend the program in the future.

---

## 🧱 2. Product Class

We start with the basic element – a single product. The class will be very simple:  
we only need a name and a price.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
```

### 🗣️ Explanation:

* `__init__` – constructor, a method called automatically when creating an object.
* `self.name` and `self.price` – store the product’s name and price.
* This allows us to create different products, e.g., `Product("Bread", 4.5)`.

---

## 🧮 3. OrderItem Class

Now we will create a class that combines a product with a quantity – something like an item in a shopping cart.   
We’ll also add a method that calculates the total cost of the item.

```python
class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def total_price(self):
        return self.product.price * self.quantity
```

### 🗣️ Explanation:

* The constructor takes a `Product` object and the quantity.
* `total_price()` – returns the value of the entire item (e.g., 3 milk = 9.6).

---

## 📦 4. Order Class

Now it’s time for a class that will store all the order items.   
We’ll add the ability to add items and display a summary.

```python
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def summary(self):
        total = 0
        print("--- Order Summary ---")
        for item in self.items:
            name = item.product.name
            quantity = item.quantity
            unit_price = item.product.price
            item_total = item.total_price()
            total += item_total
            print(f"{name} x{quantity} @ {unit_price} = {item_total}")
        print(f"Total amount to pay: {total}")
```

### 🗣️ Explanation:

* `self.items = []` – a list to store `OrderItem` objects.
* `add_item()` – adds an object to the list.
* `summary()` – iterates over all items, retrieves the name, quantity, unit price, and total for the item. At the end, it prints the total amount.

---

## 🧪 5. Example Usage

```python
# Creating products
bread = Product("Bread", 4.5)
milk = Product("Milk", 3.2)
eggs = Product("Eggs", 0.8)

# Creating order items
item1 = OrderItem(bread, 2)
item2 = OrderItem(milk, 3)
item3 = OrderItem(eggs, 10)

# Creating an order and adding items
order = Order()
order.add_item(item1)
order.add_item(item2)
order.add_item(item3)

# Displaying summary
order.summary()
```

### 🗣️ Explanation:

* We create products and combine them with quantities in `OrderItem` objects.
* We add them to the `Order`.
* Calling `summary()` shows the full receipt – like a mini store system.

---

## 📝 6. Homework

* Extend the order system in one of the following ways:
* Add the ability to apply a percentage discount to the entire order.
* Add a method to remove an item from the order.
* Add the ability to change the quantity of a specific product.
* Save the order summary to a text file.

This will help you practice list operations, class methods, and extending an object-oriented program.

---

## ✅ Lesson Summary

Today, we created a mini order system – simple, but reflecting real-world applications.
You can see how classes interact: the product knows its price, the order item knows the quantity and how to calculate it, and the order can collect everything and summarize it.
This is the power of object-oriented programming – breaking a program into logical parts that work together as a whole.

© 2025 PotegaIT – Python Course for Beginners
