## 🇵🇱 Wersja polska

# 🧠 Lekcja 11 – Iterowanie po strukturach danych: pętle for i while

---

## 🎯 Cel lekcji
W tej lekcji nauczysz się, jak **iterować po danych**, czyli wykonywać czynność wielokrotnie dla każdego elementu.  
To bardzo ważna umiejętność – pozwala np. wypisać wszystkie elementy listy albo sprawdzić, które spełniają określony warunek.  
Poznasz dwa podstawowe rodzaje pętli: **for** i **while**.

---

## 📝 1. Pętla for – gdy znamy dane

### Co to jest pętla for?
* Służy do przechodzenia przez każdy element struktury danych (lista, krotka, zbiór, słownik).  
* Używamy jej, gdy znamy dane lub liczbę elementów.  
* Działa jak: *dla każdego elementu w kolekcji – wykonaj coś*.  
* Bardzo czytelna i często używana w Pythonie.

### 📌 Przykłady

```python
# Iterowanie po liście
owoce = ["jabłko", "banan", "gruszka"]

for owoc in owoce:
    print("Owoc:", owoc)
```
```python
# Iterowanie po krotce
osoba = ("Anna", "Nowak", 28)

for element in osoba:
    print("Element krotki:", element)
```
```python
# Iterowanie po zbiorze
kolory = {"czerwony", "zielony", "niebieski"}

for kolor in kolory:
    print("Kolor:", kolor)
```
```python
# Iterowanie po kluczach słownika
osoba = {"imie": "Anna", "nazwisko": "Nowak", "wiek": 28}

for klucz in osoba:
    print("Klucz:", klucz)
```
```python
# Iterowanie po parach klucz-wartość
for klucz, wartosc in osoba.items():
    print(f"{klucz}: {wartosc}")
```

### 🧭 Podsumowanie:

* **for** działa na każdej kolekcji, po której można przechodzić krok po kroku.
* Używamy, gdy znamy dane lub chcemy przetworzyć wszystkie elementy.
* Prosta, czytelna i bardzo często używana.

---

## 📝 2. for z range() – gdy potrzebujemy liczb

* Czasem chcemy powtórzyć czynność określoną liczbę razy.
* `range()` tworzy ciąg liczb.

```python
# Powtarzamy 5 razy (0 do 4)
for i in range(5):
    print("Liczba:", i)

# Możemy zacząć od innej liczby
for i in range(2, 6):
    print(i)  # 2, 3, 4, 5
```

---

## 📝 3. Pętla while – gdy nie wiemy ile razy

### Co to jest pętla while?

* Wykonuje się dopóki warunek jest prawdziwy.
* Przydatna, gdy nie wiemy z góry, ile powtórzeń jest potrzebnych.
* Idealna np. do oczekiwania na poprawną odpowiedź użytkownika.
* Bardziej elastyczna niż for, ale trzeba uważać na pętle nieskończone.

### 📌 Przykłady

```python
# Liczenie od 0 do 2
liczba = 0

while liczba < 3:
    print("Liczba:", liczba)
    liczba += 1
```
```python
# Prosty sprawdzacz hasła
haslo = ""

while haslo != "python":
    haslo = input("Podaj hasło: ")

print("Dostęp przyznany!")
```
### ⚠️ Uwaga na pętle nieskończone

```python
licznik = 0

while licznik < 3:
    print("Nigdy się nie kończę!")
    # brak licznik += 1
```

### 🧭 Podsumowanie:

* Używamy while, gdy nie znamy z góry liczby powtórzeń.
* Pętla działa dopóki warunek jest prawdziwy.
* Musimy sami zadbać, aby warunek kiedyś przestał być spełniony.
* Przydatna w dynamicznych sytuacjach, np. oczekiwanie na dane od użytkownika.

---

## 🧩 4. Mini projekt

> Program pyta użytkownika o 3 ulubione potrawy i wypisuje je kolejno, korzystając z **for** i **range()**.

```python
potrawy = []

for i in range(3):
    potrawa = input(f"Podaj potrawę nr {i + 1}: ")
    potrawy.append(potrawa)

print("Twoje ulubione potrawy:")
for potrawa in potrawy:
    print("-", potrawa)
```

## 🎉 Podsumowanie lekcji 11

* Pętle to jedno z najważniejszych narzędzi w programowaniu.
* Pozwalają powtarzać operacje na listach, liczbach czy danych wejściowych.
* **for**: gdy znamy dane lub chcemy przejść przez całą kolekcję.
* **while**: gdy powtarzamy czynność dopóki spełniony jest warunek.
* Teraz potrafisz tworzyć dynamiczne i interaktywne programy reagujące na dane użytkownika lub przetwarzające wiele elementów automatycznie.

© 2025 PotęgaIT – Python dla początkujących

---

## 🇬🇧 English Version

# 🧠 Lesson 11 – Iterating over Data Structures: for and while Loops

---

## 🎯 Lesson Goal
In this lesson, you will learn how to **iterate over data**, which means performing an action repeatedly for each element.  
This is a very important skill – it allows you to, for example, print all elements of a list or check which ones meet a certain condition.  
You will learn two basic types of loops: **for** and **while**.

---

## 📝 1. for Loop – when we know the data

### What is a for loop?
* Used to go through each element of a data structure (list, tuple, set, dictionary).  
* We use it when we know the data or roughly how many elements there are.  
* Works like: *for each element in the collection – do something*.  
* Very readable and widely used in Python.

### 📌 Examples

```python
# Iterating over a list
fruits = ["apple", "banana", "pear"]

for fruit in fruits:
    print("Fruit:", fruit)
```
```python
# Iterating over a tuple
person = ("Anna", "Nowak", 28)

for element in person:
    print("Tuple element:", element)
```
```python
# Iterating over a set
colors = {"red", "green", "blue"}

for color in colors:
    print("Color:", color)
```
```python
# Iterating over dictionary keys
person = {"first_name": "Anna", "last_name": "Nowak", "age": 28}

for key in person:
    print("Key:", key)
```
```python
# Iterating over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
```

### 🧭 Summary

* **for** works on any collection you can iterate step by step.
* Use it when you know the data or want to process all elements.
* Simple, readable, and very common in Python.

---

## 📝 2. for with range() – when we need numbers

* Sometimes we want a loop to repeat a specific number of times.
* `range()` creates a sequence of numbers.

```python
# Repeat 5 times (0 to 4)
for i in range(5):
    print("Number:", i)

# Start from a different number
for i in range(2, 6):
    print(i)  # 2, 3, 4, 5
```

---

## 📝 3. while Loop – when we don't know how many times

### What is a while loop?

* Executes as long as a condition is true.
* Useful when we don’t know in advance how many repetitions are needed.
* Ideal, for example, for waiting for correct user input.
* More flexible than for, but watch out for infinite loops.

### 📌 Examples

```python
# Counting from 0 to 2
number = 0

while number < 3:
    print("Number:", number)
    number += 1
```
```python
# Simple password checker
password = ""

while password != "python":
    password = input("Enter password: ")

print("Access granted!")
```

### ⚠️ Watch out for infinite loops

```python
counter = 0

while counter < 3:
    print("I never end!")
    # missing counter += 1
```

### 🧭 Summary

* Use while when you don’t know how many times to repeat.
* The loop runs as long as the condition is true.
* You must ensure the condition eventually becomes false.
* Useful in dynamic situations, e.g., waiting for user input.

---

## 🧩 4. Mini Project

> The program asks the user for 3 favorite dishes and prints them one by one using for and range().

```python
dishes = []

for i in range(3):
    dish = input(f"Enter dish #{i + 1}: ")
    dishes.append(dish)

print("Your favorite dishes:")
for dish in dishes:
    print("-", dish)
```

---

## 🎉 Lesson 11 Summary

* Loops are one of the most important tools in programming.
* They allow repeating actions on lists, numbers, or user input.
* **for**: when we know the data or want to iterate over the entire collection.
* **while**: when an action should repeat as long as a condition is true.
* You can now create dynamic and interactive programs that react to user input or process many elements automatically.

© 2025 PotegaIT – Python for Beginners
