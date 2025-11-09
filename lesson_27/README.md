## 🇵🇱 Wersja polska

# 🧩 Lekcja 27 — Klasy, obiekty, atrybuty i metody

---

## 🎯 Cel lekcji

W tej lekcji poznasz podstawy programowania obiektowego **(OOP)** w Pythonie.   
Dowiesz się, czym są klasy, obiekty, atrybuty oraz metody, i nauczysz się budować własne typy danych, które łączą w sobie dane i zachowanie.

To bardzo ważny etap w nauce Pythona — od teraz zaczynasz myśleć o programach jak o zestawie obiektów, które ze sobą współpracują.

---

## 🧠 Wprowadzenie

> 🎙️ _„Dzisiaj przechodzimy do bardzo ważnego tematu – programowania obiektowego w Pythonie.   
> Brzmi groźnie? Spokojnie, wszystko Ci pokażę krok po kroku.”_

Dzięki klasom i obiektom:

* program staje się bardziej czytelny i modułowy,
* możesz łatwiej organizować dane i logikę,
* możesz tworzyć własne „klocki”, z których budujesz aplikacje.

---

## 1️⃣ Co to jest klasa?

Klasa to szablon lub przepis na tworzenie obiektów.
Definiuje, jakie cechy (atrybuty) i zachowania (metody) będą miały obiekty tego typu.

### 📖 Porównanie z życia:

**Przykład 1**:

Wyobraź sobie, że masz przepis na pizzę 🍕.   
W tym przepisie zapisane są wszystkie szczegóły — jak zrobić ciasto, ile dodać sera, jakie składniki użyć.

Ten przepis to **klasa**.   
A każda pizza, którą zrobisz na jego podstawie, to już **obiekt**.

**📄 Kod:**

```python
class Pizza:
    pass
```

### 📘 Omówienie:

* `class` — słowo kluczowe do tworzenia klasy,
* `Pizza` — nazwa klasy (zaczyna się zawsze wielką literą),
* `pass` — oznacza, że klasa jest pusta (na razie nic nie robi).

**Przykład 2**:

```python
class Pies:
    pass
```

Ta klasa `Pies` to szablon każdego psa.
Możemy teraz stworzyć psy czyli obiekty tej klasy.

---

## 2️⃣ Co to jest obiekt?

Skoro mamy **psa** (klasę), możemy utworzyć z niego konkretny obiekt.

**📄 Kod:**

```python
mój_pies = Pies()
```

---

## 3️⃣ Atrybuty — cechy obiektu

Każdy obiekt może mieć **swoje własne dane**, np. imię i wiek psa.
To właśnie są **atrybuty**.

**📄 Kod:**

```python
class Pies:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
```

### 📘 Wyjaśnienie:

* `__init__()` – specjalna metoda wywoływana automatycznie przy tworzeniu obiektu,
* `self` – odnosi się do konkretnego obiektu, który właśnie powstaje,
* `self.imie` i `self.wiek` – tworzą atrybuty obiektu.

**📄 Utworzenie obiektu:**

```python
mój_pies = Pies("Reksio", 3)
print(mój_pies.imie)  # Reksio
print(mój_pies.wiek)  # 3
```

---

## 4️⃣ Metody — działania obiektu

**Metody** to funkcje zdefiniowane **wewnątrz klasy**.
Pozwalają, aby **obiekt** coś robił.

**📄 Kod:**

```python
class Pies:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def szczekaj(self):
        print(f"{self.imie} mówi: Hau! Hau!")
```

**📄 Użycie:**

```python
mój_pies = Pies("Reksio", 3)
mój_pies.szczekaj()  # Reksio mówi: Hau! Hau!
```

### 📘 Wyjaśnienie:

* Metody działają podobnie do funkcji,
* Zawsze mają jako pierwszy argument `self`, dzięki czemu wiedzą, do którego obiektu się odnoszą.

### 🧩 Dodatkowe przykłady

#### 🔹 Tworzenie wielu obiektów z jednej klasy:

```python
pies1 = Pies("Azor", 4)
pies2 = Pies("Burek", 7)

pies1.szczekaj()  # Azor mówi: Hau! Hau!
pies2.szczekaj()  # Burek mówi: Hau! Hau!
```

Każdy obiekt ma **własne dane**, ale **dzieli metody** z klasy.


## 5️⃣ Mini projekt — Klasa `Samochod`

Zróbmy prosty projekt, w którym utworzysz własną klasę z kilkoma atrybutami i metodą.

**📄 Kod:**

```python
class Samochod:
    def __init__(self, marka, model, rok):
        self.marka = marka
        self.model = model
        self.rok = rok

    def opis(self):
        print(f"Samochód: {self.marka} {self.model}, rok produkcji: {self.rok}")
```

**📄 Użycie:**

```python
moje_auto = Samochod("Toyota", "Corolla", 2020)
moje_auto.opis()
# Samochód: Toyota Corolla, rok produkcji: 2020
```

### 📘 Co warto zapamiętać:

* Klasy łączą dane (atrybuty) i logikę (metody),
* Dzięki nim tworzysz własne **typy danych** – Twoje „klocki LEGO” w programie,
* To fundament dużych aplikacji, które składają się z wielu współpracujących klas.

---

## 💡 Ciekawostka

W Pythonie **wszystko jest obiektem** — liczby, napisy, listy, a nawet funkcje.
To oznacza, że możesz używać ich metod, np.:

```python
tekst = "python"
print(tekst.upper())  # PYTHON
```

---

## ✅ Podsumowanie

W tej lekcji poznałeś podstawy **programowania obiektowego (OOP)** w Pythonie.

Teraz wiesz, że:

* **Klasa** to przepis na tworzenie obiektów,
* **Obiekt** to konkretna instancja klasy,
* **Atrybuty** to dane przypisane do obiektu,
* **Metody** to działania, które obiekt może wykonywać.

---

## 🚀 Co dalej?

W kolejnych lekcjach nauczysz się:

* jak klasy mogą **dziedziczyć** po innych klasach,
* jak współpracować między sobą,
* oraz jak budować **bardziej złożone aplikacje obiektowe**.


© 2025 PotęgaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version

# 🧩 Lesson 27 — Classes, Objects, Attributes, and Methods

---

## 🎯 Lesson Goal

In this lesson, you will learn the basics of **Object-Oriented Programming (OOP)** in Python.  
You’ll find out what classes, objects, attributes, and methods are, and learn how to build your own data types that combine data and behavior.

This is a very important stage in learning Python — from now on, you’ll start thinking about programs as a collection of objects that work together.

---

## 🧠 Introduction

> 🎙️ _“Today we’re moving on to a very important topic — object-oriented programming in Python.  
> Sounds scary? Don’t worry, I’ll show you everything step by step.”_

Thanks to classes and objects:

* your program becomes more readable and modular,
* you can organize data and logic more easily,
* you can create your own “blocks” to build applications.

---

## 1️⃣ What is a class?

A class is a template or recipe for creating objects.  
It defines what features (attributes) and behaviors (methods) the objects of that type will have.

### 📖 Real-life comparison:

**Example 1**:

Imagine you have a pizza recipe 🍕.  
This recipe describes all the details — how to make the dough, how much cheese to add, and which ingredients to use.

That recipe is a **class**.  
And every pizza you make based on it is an **object**.

**📄 Code:**

```python
class Pizza:
    pass
```

### 📘 Explanation:

* `class` — a keyword for creating a class,
* `Pizza` — the class name (always starts with a capital letter),
* `pass` — means the class is empty for now (does nothing yet).

**Example 2**:

```python
class Dog:
    pass
```

The class `Dog` is a template for every dog. We can now create dogs — objects of this class.

---

## 2️⃣ What is an object?

Since we have a `Dog` class, we can now create a specific object from it.

**📄 Code:**

```python
my_dog = Dog()
```

---

## 3️⃣ Attributes — object properties

Each object can have **its own data**, such as a dog’s name and age.
These are called **attributes**.

**📄 Code:**

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### 📘 Explanation:

* `__init__()` – a special method automatically called when an object is created,
* `self` – refers to the specific object being created,
* `self.name` and self.age – create the object’s attributes.

**📄 Creating an object:**

```python
my_dog = Dog("Rex", 3)
print(my_dog.name)  # Rex
print(my_dog.age)   # 3
```

---

## 4️⃣ Methods — object actions

**Methods** are functions defined **inside a class**.
They allow an object to perform actions.

**📄 Code:**

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")
```

**📄 Usage:**

```python
my_dog = Dog("Rex", 3)
my_dog.bark()  # Rex says: Woof! Woof!
```

### 📘 Explanation:

* Methods work like regular functions,
* They always have `self` as the first argument, so they know which object they refer to.

### 🧩 Additional examples

####🔹 Creating multiple objects from one class:

```python
dog1 = Dog("Buddy", 4)
dog2 = Dog("Rocky", 7)

dog1.bark()  # Buddy says: Woof! Woof!
dog2.bark()  # Rocky says: Woof! Woof!
```

Each object has **its own data** but **shares methods** from the class.

---

## 5️⃣ Mini project — The `Car` class

**Code:**

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def describe(self):
        print(f"Car: {self.brand} {self.model}, year: {self.year}")
```

**📄 Usage:**

```python
my_car = Car("Toyota", "Corolla", 2020)
my_car.describe()
# Car: Toyota Corolla, year: 2020
```

### 📘 Key takeaways:

* Classes combine data (attributes) and logic (methods),
* They let you create your own **data types** — your “LEGO blocks” in a program,
* They are the foundation of large applications made up of many cooperating classes.

---

##  💡 Fun fact

In Python, **everything is an object** — numbers, strings, lists, and even functions.
That means you can use their methods, for example:

```python
text = "python"
print(text.upper())  # PYTHON
```

---

## ✅ Summary

In this lesson, you’ve learned the basics of **Object-Oriented Programming (OOP)** in Python.

Now you know that:

* **A class** is a recipe for creating objects,
* **An object** is a specific instance of a class,
* **Attributes** are the data assigned to an object,
* **Methods** are the actions an object can perform.

© 2025 PotegaIT – Python for Beginners Course
