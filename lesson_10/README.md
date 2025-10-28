## 🇵🇱 Wersja polska

# 🧠 Lekcja 10 – Krotki, Słowniki i Zbiory (Tuples, Dictionaries, Sets)

---

## 🎯 Cel lekcji
W tej lekcji poznasz trzy ważne typy danych w Pythonie:

* **krotki (tuples)**
* **słowniki (dict)**
* **zbiory (set)**

Dzięki nim możesz przechowywać i organizować dane w różny sposób, w zależności od potrzeb programu.  
Dowiesz się, czym się różnią i kiedy najlepiej z nich korzystać.

---

## 📝 1. Krotki (Tuples)

### Co to jest krotka?
* Uporządkowany, ale **niezmienny** zbiór danych.  
* Elementy mają ustaloną kolejność, ale nie można ich zmieniać, dodawać ani usuwać po utworzeniu.

### Kiedy używać?
* Dane, które nie powinny się zmieniać:
  - współrzędne GPS
  - dane osobowe
  - kolory w formacie RGB

### 📌 Przykłady w Pythonie

```python
# Tworzenie krotki
osoba = ("Anna", "Nowak", 28)
print(osoba)  # ('Anna', 'Nowak', 28)

# Dostęp do elementów przez indeks
print("Imię:", osoba[0])  # Imię

# Rozpakowywanie krotki 
imie, nazwisko, wiek = osoba
print(imie, wiek)  # Anna 28

# Krotki są niezmienne 
# osoba[1] = "Kowalska"  # Błąd!
```

### 🧭 Podsumowanie:

* Krotki są uporządkowane i niezmienne.
* Tworzymy je nawiasami `()`.
* Możemy odwoływać się do elementów przez indeks.
* Możemy je rozpakować na zmienne.
* Nie można ich modyfikować po utworzeniu – to zaleta w niektórych przypadkach.

  ---

## 📝 2. Słowniki (Dictionaries)

### Co to jest słownik?

* Przechowuje dane w parach klucz : wartość (key : value).
* Klucze mówią, co oznacza dana wartość – kod staje się bardziej czytelny.

### 📌 Przykłady w Pythonie

```python
# Tworzenie słownika 
osoba = {
    "imie": "Anna",
    "nazwisko": "Nowak",
    "wiek": 28
}
print(osoba)

# Dostęp do wartości przez klucz 
print("Imię:", osoba["imie"])

# Dodawanie nowego klucza lub zmiana wartości
osoba["miasto"] = "Kraków"
osoba["wiek"] = 29

# Usuwanie elementu 
del osoba["nazwisko"]
```

### 🧭 Podsumowanie:

* Słowniki przechowują dane w parach klucz : wartość.
* Klucze dają czytelność kodu.
* Tworzymy je nawiasami `{}`.
* Można dodawać, zmieniać i usuwać dane.

  ---

## 📝 3. Zbiory (Sets)

### Co to jest zbiór?

Kolekcja unikalnych elementów.

Nie ma duplikatów i nie mają indeksów (nieuporządkowane).

Idealne do: listy tagów, unikalnych użytkowników, technologii.

### 📌 Przykłady w Pythonie

```python
# Tworzenie zbioru /
kolory = {"czerwony", "zielony", "niebieski", "zielony"}
print(kolory)  # Zielony wystąpi tylko raz 

# Dodawanie i usuwanie elementów 
kolory.add("żółty")
kolory.remove("czerwony")

# Sprawdzanie przynależności 
print("zielony" in kolory)  # True lub False
```

### 🧭 Podsumowanie:

* Zbiór przechowuje unikalne elementy.
* Tworzymy go nawiasami `{}`.
* Nie ma kolejności, brak indeksów.
* Możemy dodawać i usuwać elementy.
* Świetny do filtrowania duplikatów i sprawdzania przynależności.

---

## 🧭 4. Kiedy czego używać?

| Typ danych      | Zastosowanie                       |
| --------------- | ---------------------------------- |
| Krotki (tuple)  | Dane niezmienne i uporządkowane    |
| Słowniki (dict) | Dane opisane kluczami, czytelność  |
| Zbiory (set)    | Unikalne elementy, brak duplikatów |

---

## 🧩 5. Mini projekt

> Program pyta użytkownika o dane 3 osób i zapisuje każdą jako krotkę w słowniku.
> Na końcu tworzy zbiór unikalnych imion.

```python
osoby = {}
for i in range(3):
    imie = input("Podaj imię: ")
    nazwisko = input("Podaj nazwisko: ")
    wiek = int(input("Podaj wiek: "))
    osoby[i] = (imie, nazwisko, wiek)

imiona = {osoba[0] for osoba in osoby.values()}
print("Unikalne imiona:", imiona)
```

### Wyjaśnienie krok po kroku:

1. Tworzymy pusty słownik `osoby = {}`.
2. Pętla `for i in range(3)` pozwala powtórzyć wprowadzanie danych 3 razy.
3. Pobieramy dane od użytkownika `(input)` i zamieniamy wiek na liczbę (`int()`).
4. Zapisujemy dane jako krotkę `(imie, nazwisko, wiek)` w słowniku.
5. Tworzymy zbiór unikalnych imion za pomocą `set comprehension`.
6. Wyświetlamy wynik.

---

## 🎉 Podsumowanie lekcji 10

* Krotki: uporządkowane i niezmienne.
* Słowniki: pary klucz : wartość, mutowalne, czytelne.
* Zbiory: unikalne elementy, brak indeksów, szybkie sprawdzanie przynależności.
* Poznaliśmy również set comprehension i użyliśmy pętli for z range() w praktyce.
* Dzięki temu możemy tworzyć programy, które przechowują dane w przemyślany sposób i wyciągają z nich konkretne informacje.
* To fundament kolejnych lekcji z pętlami, warunkami i bardziej złożonymi strukturami danych.

© 2025 PotęgaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version

# 🧠 Lesson 10 – Tuples, Dictionaries, Sets

---

## 🎯 Lesson Goal
In this lesson, you will learn three important Python data types:

* **tuples**
* **dictionaries (dict)**
* **sets**

They allow you to store and organize data in different ways, depending on the needs of your program.  
You will learn the differences between them and when to use each type.

---

## 📝 1. Tuples

### What is a tuple?
* An **ordered but immutable** collection of data.  
* Elements have a fixed order but cannot be changed, added, or removed after creation.

### When to use?
* For data that should not change:
  - GPS coordinates
  - Personal data
  - RGB colors

### 📌 Python examples

```python
# Creating a tuple
person = ("Anna", "Nowak", 28)
print(person)  # ('Anna', 'Nowak', 28)

# Accessing elements by index
print("First name:", person[0])  # First name

# Tuple unpacking
first_name, last_name, age = person
print(first_name, age)  # Anna 28

# Tuples are immutable
# person[1] = "Kowalska"  # Error!
```

### 🧭 Summary:

* Tuples are ordered and immutable.
* We create them with parentheses `()`.
* We can access elements by index.
* We can unpack them into variables.
* We cannot modify them after creation – which is sometimes an advantage.

---

## 📝 2. Dictionaries

### What is a dictionary?

* Stores data in key : value pairs.
* Keys describe what the value represents – making the code more readable.

### 📌 Python examples

```python
# Creating a dictionary
person = {
    "first_name": "Anna",
    "last_name": "Nowak",
    "age": 28
}
print(person)

# Access value by key
print("First name:", person["first_name"])

# Add a new key or change value
person["city"] = "Kraków"
person["age"] = 29

# Remove an element
del person["last_name"]
```

### 🧭 Summary:

* Dictionaries store data in key : value pairs.
* Keys make code more readable.
* We create them with curly braces `{}`.
* Data can be added, changed, or removed.

---

## 📝 3. Sets

### What is a set?

* A collection of unique elements.
* No duplicates and no indexes (unordered).
* Ideal for: tags, unique users, technologies.

### 📌 Python examples

```python
# Creating a set
colors = {"red", "green", "blue", "green"}
print(colors)  # "green" appears only once

# Adding and removing elements
colors.add("yellow")
colors.remove("red")

# Checking membership
print("green" in colors)  # True or False
```

### 🧭 Summary:

* Sets store unique elements.
* We create them with `{}`.
* No order, no indexes.
* Elements can be added or removed.
* Great for filtering duplicates and checking membership.

---

### 🧭 4. When to use which?

| Data type  | Use case                                  |
| ---------- | ----------------------------------------- |
| Tuple      | Immutable and ordered data                |
| Dictionary | Descriptive data with keys, readable code |
| Set        | Unique elements, no duplicates            |

---

## 🧩 5. Mini project

> The program asks the user for data of 3 people and stores each as a tuple in a dictionary.
> At the end, it creates a set of unique first names.

```python
people = {}
for i in range(3):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = int(input("Enter age: "))
    people[i] = (first_name, last_name, age)

first_names = {person[0] for person in people.values()}
print("Unique first names:", first_names)
```

### Step-by-step explanation:

1. Create an empty dictionary `people = {}`.
2. The loop `for i in range(3)` repeats data entry 3 times.
3. We get user input with `input()` and convert age to an integer (`int()`).
4. Store the data as a tuple `(first_name, last_name, age)` in the dictionary.
5. Create a set of unique first names using set comprehension.
6. Print the result.

---

## 🎉 Lesson 10 Summary

* Tuples: ordered and immutable.
* Dictionaries: key : value pairs, mutable, readable.
* Sets: unique elements, no indexes, fast membership check.
* Learned set comprehension and used for loop with range() in practice.
* Now you can write programs that store data in a structured way and extract specific information.
* This lays the foundation for upcoming lessons on loops, conditions, and more complex data structures.

© 2025 PotegaIT – Python for Beginners
