## 🇵🇱 Wersja polska

# 🧩 Lekcja 23: Tworzenie własnego modułu

---

## 🎯 Cel lekcji

W tej lekcji nauczysz się, jak **tworzyć własne moduły w Pythonie** i jak **korzystać z nich w innych plikach**.  
Dzięki temu możesz:

- uporządkować kod,  
- łatwiej go testować,  
- wielokrotnie wykorzystywać funkcje w różnych projektach.  

Tworzenie własnych modułów to ważny krok w stronę bardziej profesjonalnego programowania.

---

## 📝 1. Co to jest moduł?

- Moduł w Pythonie to **zwykły plik `.py`**, w którym zapisujesz funkcje, zmienne lub klasy.  
- Możesz go później zaimportować w innym programie, tak jak wbudowane moduły `math` czy `random`.

Przykład struktury folderu:

```css
projekt/
├── moj_modul.py
└── main.py
```

---

## 📝 2. Tworzenie własnego modułu

Stwórz plik **moj_modul.py** i dodaj przykładowe funkcje:

```python
# moj_modul.py

def powiedz_czesc(imie):
    print(f"Cześć, {imie}!")

def dodaj(a, b):
    return a + b
```

* `powiedz_czesc(imie)` – wypisuje powitanie dla podanego imienia.
* `dodaj(a, b)` – zwraca sumę dwóch liczb.

---

## 📝 3. Korzystanie z modułu w innym pliku

Stwórz plik main.py w tym samym folderze:

```python
# main.py

import moj_modul

moj_modul.powiedz_czesc("Greg")   # Wywołanie funkcji powitanie
suma = moj_modul.dodaj(5, 7)      # Wywołanie funkcji dodawania
print("Suma:", suma)
```

* Użycie modułu polega na wpisaniu `import nazwa_modulu`.
* Następnie wywołujesz funkcje poprzez `nazwa_modulu.funkcja()`.

---

## 📝 4. Importowanie konkretnych funkcji

Jeśli nie chcesz pisać `moj_modul.` za każdym razem, możesz zaimportować funkcję bezpośrednio:

```python
from moj_modul import powiedz_czesc

powiedz_czesc("Julia")
```
> Uwaga: importowanie zbyt wielu funkcji w ten sposób może być nieczytelne. Często lepiej używać całej nazwy modułu.

---

## 📝 5. Mini projekt: własny moduł matematyczny

### Plik `matematyka.py`

```python
def kwadrat(x):
    return x ** 2

def srednia(lista):
    return sum(lista) / len(lista)

def czy_parzysta(x):
    return x % 2 == 0
```

* `kwadrat(x)` – zwraca kwadrat liczby
* `srednia(lista)` – zwraca średnią z listy liczb
* `czy_parzysta(x)` – zwraca True, jeśli liczba jest parzysta

### Plik `analiza.py`

```python
import matematyka

liczby = []

for i in range(5):
    n = int(input(f"Podaj liczbę {i + 1}: "))
    liczby.append(n)

print("Kwadraty liczb:")
for l in liczby:
    print(matematyka.kwadrat(l))

print("Średnia:", matematyka.srednia(liczby))

for l in liczby:
    if matematyka.czy_parzysta(l):
        print(f"{l} jest parzysta.")
    else:
        print(f"{l} jest nieparzysta.")
```

* Program prosi użytkownika o podanie 5 liczb.
* Następnie używa funkcji z modułu matematyka do obliczenia kwadratów, średniej i sprawdzenia parzystości.

---

## ✅ Podsumowanie

W tej lekcji dowiedziałeś się:

* Czym jest moduł w Pythonie.
* Jak tworzyć własny moduł `.py`.
* Jak korzystać z modułu w innych plikach poprzez `import`.
* Jak importować konkretne funkcje.
* Jak zorganizować prosty projekt z modułem matematycznym.

Tworzenie własnych modułów to pierwszy krok do bardziej profesjonalnego i uporządkowanego kodu.
Teraz możesz budować własne biblioteki i wykorzystywać je w wielu projektach – dokładnie tak jak robią zawodowi programiści.

© 2025 PotęgaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version
# 🧩 Lesson 23: Creating Your Own Module

---

## 🎯 Lesson Goal

In this lesson, you will learn how to **create your own Python modules** and how to **use them in other files**.  
This allows you to:

- organize your code,  
- make it easier to test,  
- reuse functions across different projects.  

Creating your own modules is an important step toward more professional programming.

---

## 📝 1. What is a module?

- A Python module is simply a **`.py` file** where you can store functions, variables, or classes.  
- You can later import it into another program, just like built-in modules such as `math` or `random`.

Example folder structure:

```css
project/
├── my_module.py
└── main.py
```
---

## 📝 2. Creating your own module

Create a file called **my_module.py** and add example functions:

```python
# my_module.py

def say_hello(name):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b
```

* `say_hello(name)` – prints a greeting for the given name.
* `add(a, b)` – returns the sum of two numbers.

---

## 📝 3. Using your module in another file

Create a file **main.py** in the same folder:

```python
# main.py

import my_module

my_module.say_hello("Greg")   # Call the greeting function
total = my_module.add(5, 7)   # Call the addition function
print("Total:", total)
```

* Use a module by writing `import module_name`.
* Then call functions with `module_name.function()`.

---

## 📝 4. Importing specific functions

If you don’t want to type `my_module.` every time, you can import a function directly:

```python
from my_module import say_hello

say_hello("Julia")
```

> Note: importing too many functions this way can get confusing. Often it’s better to use the full module name.

---

## 📝 5. Mini Project: Your Own Math Module

### File `math_module.py`

```python
def square(x):
    return x ** 2

def average(numbers):
    return sum(numbers) / len(numbers)

def is_even(x):
    return x % 2 == 0
```

* `square(x)` – returns the square of a number
* `average(numbers)` – returns the average of a list of numbers
* `is_even(x)` – returns True if the number is even

### File `analysis.py`

```python
import math_module

numbers = []

for i in range(5):
    n = int(input(f"Enter number {i + 1}: "))
    numbers.append(n)

print("Squares of the numbers:")
for num in numbers:
    print(math_module.square(num))

print("Average:", math_module.average(numbers))

for num in numbers:
    if math_module.is_even(num):
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
```

* The program asks the user to enter 5 numbers.
* Then it uses functions from the math module to calculate squares, the average, and check which numbers are even.

---

## ✅ Summary

In this lesson, you learned:

* What a Python module is.
* How to create your own `.py` module.
* How to use a module in other files via `import`.
* How to import specific functions.
* How to organize a simple project with a math module.

Creating your own modules is the first step toward more professional and organized code.
Now you can build your own libraries and reuse them in multiple projects – just like professional programmers do every day.

© 2025 PotegaIT – Python Course for Beginners

