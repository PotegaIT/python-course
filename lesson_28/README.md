## 🇵🇱 Wersja polska

# 🧠 Lekcja 28: Dziedziczenie i enkapsulacja

### Programowanie obiektowe w praktyce

---

## 🎬 Wprowadzenie

> Dzisiaj pokażę dwie bardzo ważne cechy programowania obiektowego w Pythonie:   
> **dziedziczenie** i **enkapsulację**.
>   
> Brzmi poważnie ale rozłożymy to na proste kawałki.
>   
> Po tej lekcji zrozumiesz:
>   
> * jak klasy mogą korzystać z siebie nawzajem,
> * jak chronić dane wewnątrz obiektów przed przypadkowym zepsuciem.

---

## 1️⃣ Co to jest dziedziczenie?

Dziedziczenie to mechanizm, który pozwala jednej klasie (tzw. _klasie pochodnej_) przejąć cechy i zachowania innej klasy (tzw. _klasy bazowej_).

Dzięki temu nie musimy powtarzać kodu — możemy rozszerzać istniejące klasy i **dodawać nowe funkcjonalności**.

### 📖 Przykład z życia:

Wyobraź sobie, że piszesz grę.
Masz klasę **Pojazd**, która opisuje wspólne elementy wszystkich pojazdów — np. markę i model.

Teraz chcesz stworzyć **Samochód**, **Motocykl**, **Ciężarówkę**.
Każdy z nich to też pojazd, ale z dodatkowymi cechami.

Nie ma sensu pisać wszystkiego od nowa — wystarczy **odziedziczyć** klasę Pojazd`.

**📄 Kod:**

```python
# Klasa bazowa / Base class
class Pojazd:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def opis(self):
        print(f"Pojazd: {self.marka} {self.model}")

# Klasa pochodna / Derived class
class Samochod(Pojazd):
    def __init__(self, marka, model, typ):
        super().__init__(marka, model)  # wywołanie konstruktora klasy bazowej / call to base constructor
        self.typ = typ  # nowy atrybut tylko dla klasy Samochod

    def opis_samochodu(self):
        print(f"Samochód: {self.marka} {self.model}, typ: {self.typ}")
```

### 💬 Omówienie:

* `class Samochod(Pojazd)`: → oznacza, że **Samochod** dziedziczy wszystko z klasy `Pojazd`,
* `super().__init__(...)` → wywołuje konstruktor klasy bazowej (`Pojazd`),
* `typ` → to **nowy atrybut**, który nie istnieje w klasie `Pojazd`.

**📦 Użycie:**

```python
moj_samochod = Samochod("Toyota", "Corolla", "sedan")

moj_samochod.opis()              # metoda odziedziczona z klasy Pojazd
moj_samochod.opis_samochodu()    # metoda z klasy Samochod
```

**🟢 Efekt:**

```makefile
Pojazd: Toyota Corolla
Samochód: Toyota Corolla, typ: sedan
```

### 💡 Wniosek:

> Dziedziczenie pozwala **uniknąć powtarzania kodu**.   
> Możemy korzystać z tego, co już istnieje, i tylko **dodawać nowe elementy**.

---

## 2️⃣ Co to jest enkapsulacja (hermetyzacja)?

**Enkapsulacja** to ukrywanie szczegółów działania obiektu przed światem zewnętrznym.

Niektóre dane powinny być chronione — żeby nie można było ich przypadkowo zmienić lub uszkodzić.

### 📖 Porównanie z życia:

Pomyśl o samochodzie 🚗 — wciskasz pedał gazu, ale nie musisz wiedzieć, co dzieje się w silniku.   
Ważne, że działa!

Tak samo w programie — ukrywamy wnętrze obiektu i pozwalamy korzystać z niego tylko przez bezpieczne metody.

**📄 Kod:**

```python
class KontoBankowe:
    def __init__(self, saldo):
        self.__saldo = saldo  # prywatny atrybut / private attribute

    def pokaz_saldo(self):
        print(f"Twoje saldo wynosi: {self.__saldo} zł")

    def wplata(self, kwota):
        if kwota > 0:
            self.__saldo += kwota
            print(f"Wpłacono: {kwota} zł")
        else:
            print("Kwota musi być większa od zera.")
```

### 💬 Omówienie:

* `__saldo` – dwa podkreślniki (`__`) oznaczają **prywatny atrybut**, nie można się do niego dostać bezpośrednio (`konto.__saldo` nie zadziała).
* Metody `pokaz_saldo()` i `wplata()` to bezpieczny sposób na kontrolowanie danych.

**📦 Użycie:**

```python
konto = KontoBankowe(1000)
konto.pokaz_saldo()    # Twoje saldo wynosi: 1000 zł
konto.wplata(500)      # Wpłacono: 500 zł
konto.pokaz_saldo()    # Twoje saldo wynosi: 1500 zł
```

**❌ Próba dostępu do prywatnego atrybutu:**

```python
konto.__saldo = 0  # nie zadziała – atrybut jest ukryty
```

**🔒 To właśnie enkapsulacja** – dane są chronione i modyfikowane tylko w kontrolowany sposób.

---

## 3️⃣ Mini projekt: Pracownik i Programista 👩‍💻

Stwórzmy mały przykład z życia.
Mamy klasę `Pracownik`, która opisuje ogólne dane o pracowniku.

Na jej podstawie tworzymy klasę `Programista`, która dziedziczy z `Pracownik`,
ale dodaje własny atrybut — język programowania.

**📄 Kod:**

```python
class Pracownik:
    def __init__(self, imie, stanowisko):
        self.imie = imie
        self.stanowisko = stanowisko

    def przedstaw_sie(self):
        print(f"Cześć! Jestem {self.imie} i pracuję jako {self.stanowisko}.")

class Programista(Pracownik):
    def __init__(self, imie, jezyk_programowania):
        super().__init__(imie, "Programista")
        self.jezyk_programowania = jezyk_programowania

    def pokaz_umiejetnosci(self):
        print(f"Piszę programy w języku {self.jezyk_programowania}.")
```

**📦 Użycie:**

```python
programista = Programista("Ania", "Python")
programista.przedstaw_sie()
programista.pokaz_umiejetnosci()
```

**🟢 Efekt:**

```css
Cześć! Jestem Ania i pracuję jako Programista.
Piszę programy w języku Python.
```

### 💡 Omówienie:

* `Programista` dziedziczy z `Pracownik`,
* używamy `super().__init__()`, aby ustawić imię i stanowisko,
* dodajemy nowy atrybut `jezyk_programowania`,
* możemy korzystać zarówno z metod klasy bazowej (`przedstaw_sie`), jak i tych nowych (`pokaz_umiejetnosci`).

## ✅ Podsumowanie

> Dzisiaj poznałeś dwie potężne zasady programowania obiektowego:

* **Dziedziczenie** – pozwala budować nowe klasy na podstawie istniejących, bez powtarzania kodu.
* **Enkapsulacja** – chroni dane i ukrywa to, co nie powinno być dostępne z zewnątrz.

### 🧩 Co potrafisz po tej lekcji:

✔️ Tworzyć klasy bazowe i klasy pochodne,   
✔️ Używać `super()` do wywołania konstruktora klasy nadrzędnej,   
✔️ Tworzyć prywatne atrybuty (`__nazwa`),   
✔️ Budować bezpieczne metody dostępu do danych.

© 2025 PotęgaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version

# 🧠 Lesson 28: Inheritance and Encapsulation

### Object-Oriented Programming in Practice

---

## 🎬 Introduction

> Today, I’ll show you two very important features of object-oriented programming in Python:  
> **inheritance** and **encapsulation**.  
>   
> Sounds complicated? Don’t worry — we’ll break it down into simple pieces.  
>   
> After this lesson, you’ll understand:
>   
> * how classes can use each other,
> * how to protect data inside objects from accidental modification.

---

## 1️⃣ What is inheritance?

Inheritance is a mechanism that allows one class (called a _derived class_) to take over the features and behaviors of another class (called a _base class_).

This means we don’t have to repeat code — we can extend existing classes and **add new functionality**.

### 📖 Real-life example:

Imagine you’re making a game.  
You have a **Vehicle** class that describes common features of all vehicles — such as brand and model.

Now you want to create **Car**, **Motorcycle**, and **Truck**.  
Each of them is also a vehicle, but with additional properties.

There’s no need to write everything from scratch — just **inherit** from the `Vehicle` class.

**📄 Code:**

```python
# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describe(self):
        print(f"Vehicle: {self.brand} {self.model}")

# Derived class
class Car(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model)  # call to base constructor
        self.type = type  # new attribute only for the Car class

    def describe_car(self):
        print(f"Car: {self.brand} {self.model}, type: {self.type}")
```

### 💬 Explanation:

* `class Car(Vehicle)`: → means that **Car** inherits everything from the `Vehicle` class,
* `super().__init__(...)` → calls the constructor of the base class (`Vehicle`),
* `type` → is a **new attribute** that doesn’t exist in the `Vehicle` class.

**📦 Usage:**

```python
my_car = Car("Toyota", "Corolla", "sedan")

my_car.describe()           # method inherited from Vehicle
my_car.describe_car()       # method from Car
```

**🟢 Output:**

```makefile
Vehicle: Toyota Corolla
Car: Toyota Corolla, type: sedan
```

### 💡 Conclusion:

> Inheritance helps **avoid repeating code**.   
> We can use what already exists and simply **add new elements**.

---

## 2️⃣ What is encapsulation?

**Encapsulation** means hiding the internal details of how an object works from the outside world.

Some data should be protected — so it can’t be accidentally changed or damaged.

### 📖 Real-life comparison:

Think of a car 🚗 — you press the gas pedal, but you don’t need to know what’s happening inside the engine.   
What matters is that it works!

It’s the same in programming — we hide the internal logic of an object and allow access only through safe methods.

**📄 Code:**

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def show_balance(self):
        print(f"Your balance is: {self.__balance} zł")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount} zł")
        else:
            print("The amount must be greater than zero.")
```

### 💬 Explanation:

* `__balance` – two underscores (`__`) mean a **private attribute**, which can’t be accessed directly (`account.__balance` won’t work).
* Methods `show_balance()` and `deposit()` are safe ways to control data.

**📦 Usage:**

```python
account = BankAccount(1000)
account.show_balance()   # Your balance is: 1000 zł
account.deposit(500)     # Deposited: 500 zł
account.show_balance()   # Your balance is: 1500 zł
```

**❌ Attempt to access private attribute:**

```python
account.__balance = 0  # won't work – the attribute is hidden
```

**🔒 That’s encapsulation** – data is protected and can only be modified in a controlled way.

---

## 3️⃣ Mini project: Employee and Programmer 👩‍💻

Let’s create a small real-world example.
We have an `Employee` class that describes general employee data.

Based on it, we’ll create a `Programmer` class that inherits from `Employee`,
but adds its own attribute — programming language.

**📄 Code:**

```python
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def introduce(self):
        print(f"Hi! I'm {self.name} and I work as a {self.position}.")

class Programmer(Employee):
    def __init__(self, name, programming_language):
        super().__init__(name, "Programmer")
        self.programming_language = programming_language

    def show_skills(self):
        print(f"I write programs in {self.programming_language}.")
```

**📦 Usage:**

```python
programmer = Programmer("Ania", "Python")
programmer.introduce()
programmer.show_skills()
```

**🟢 Output:**

```css
Hi! I'm Ania and I work as a Programmer.
I write programs in Python.
```

### 💡 Explanation:

* `Programmer` inherits from `Employee`,
* we use `super().__init__()` to set the name and position,
* we add a new attribute `programming_language`,
* we can use both base class methods (`introduce`) and new ones (`show_skills`).

## ✅ Summary

> Today you’ve learned two powerful principles of object-oriented programming:

* **Inheritance** – lets you build new classes based on existing ones without repeating code.
* **Encapsulation** – protects data and hides what shouldn’t be accessible from the outside.

### 🧩 What you can do after this lesson:

✔️ Create base and derived classes,  
✔️ Use `super()` to call the parent class constructor,  
✔️ Create private attributes (`__name`),  
✔️ Build safe methods for accessing data.

© 2025 PotegaIT – Python for Beginners Course
