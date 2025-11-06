## 🇵🇱 Wersja polska

# 🧠 Lekcja 15 – Tworzenie i wywoływanie funkcji

---

## 🎯 Cel lekcji

W tej lekcji nauczysz się, jak **tworzyć i wywoływać funkcje w Pythonie**.  
Funkcje pozwalają na:

* organizowanie kodu w mniejsze, logiczne bloki,
* wielokrotne wykonywanie tego samego fragmentu kodu,
* operowanie na różnych danych wejściowych i zwracanie wyników.

Dzięki funkcjom Twój kod stanie się bardziej przejrzysty, elastyczny i łatwiejszy do utrzymania.

---

## 📝 1. Co to jest funkcja?

Funkcja to **blok kodu, który wykonuje określone zadanie**.  
Możemy nadać jej nazwę i wywoływać ją w dowolnym miejscu programu, a także przekazywać do niej dane (parametry).

```python
def przywitaj():
    print("Cześć! Miło Cię widzieć!")

# wywołanie funkcji
przywitaj()
```

### 🔍 Wyjaśnienie:

* `def przywitaj()`: – definiujemy funkcję o nazwie `przywitaj`.
* Funkcja wykonuje kod w swoim bloku, czyli wypisuje komunikat.
* Wywołanie `przywitaj()` uruchamia funkcję w wybranym miejscu programu.

---

## 📝 2. Funkcja z parametrem

Funkcje mogą przyjmować parametry, czyli dane wejściowe, na których mogą operować.

```python
def przywitaj(imie):
    print("Cześć", imie + "!")

przywitaj("Ania")
przywitaj("Tomek")
```

### 🔍 Wyjaśnienie:

* `imie` to parametr funkcji – zmienna, która przyjmuje wartość podczas wywołania.
* Funkcja wykonuje te same instrukcje, ale z różnymi danymi wejściowymi.
* Dzięki parametrom funkcja jest uniwersalna i bardziej elastyczna.

---

## 📝 3. Funkcja zwracająca wartość

Funkcja może zwracać wartość, używając słowa kluczowego `return`.

```python
def dodaj(a, b):
    suma = a + b
    return suma

wynik = dodaj(3, 5)
print("Wynik dodawania:", wynik)
```

### 🔍 Wyjaśnienie:

* `return suma` – funkcja zwraca wynik działania.
* Wartość zwrócona może zostać przypisana do zmiennej (`wynik`) i używana dalej.
* Funkcja kończy swoje działanie po napotkaniu `return`.

---

## 📝 4. Funkcja z wieloma parametrami

Funkcja może przyjmować **więcej niż jeden parametr**, co pozwala na bardziej złożone operacje.

```python
def mnoz(a, b, c):
    return a * b * c

wynik = mnoz(2, 3, 4)
print("Wynik mnożenia:", wynik)
```

### 🔍 Wyjaśnienie:

* Funkcja mnoz przyjmuje trzy argumenty i zwraca ich iloczyn.
* Liczba parametrów w definicji musi odpowiadać liczbie argumentów podczas wywołania.

---

## 📝 5. Funkcja bez parametrów, zwracająca różne typy danych

Funkcja nie zawsze musi przyjmować parametry. Może też zwracać różne typy danych.

```python
def powitanie():
    return "Witaj w programowaniu!"

tekst = powitanie()
print(tekst)
```

### 🔍 Wyjaśnienie:

* Funkcja `powitanie` nie przyjmuje danych wejściowych.
* Zwraca tekst, który możemy przypisać do zmiennej i wykorzystać dalej.

---

## 🎉 Podsumowanie lekcji 15

* Funkcja to blok kodu, który wykonuje określone zadanie.
* Funkcje mogą przyjmować parametry i zwracać wartości.
* Pozwalają organizować kod, powtarzać operacje i zwiększać jego czytelność.
* Dzięki funkcjom Twój kod staje się bardziej elastyczny i łatwiejszy do utrzymania.

© 2025 PotęgaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version

# 🧠 Lesson 15 – Creating and Calling Functions

---

## 🎯 Lesson Goal

In this lesson, you will learn how to **create and call functions in Python**.  
Functions allow you to:

* organize code into smaller, logical blocks,
* reuse the same code multiple times,
* work with different input data and return results.

Using functions makes your code more readable, flexible, and easier to maintain.

---

## 📝 1. What is a function?

A function is a **block of code that performs a specific task**.  
We can give it a name and call it anywhere in our program, and we can also pass data to it (parameters).

```python
def greet():
    print("Hello! Nice to see you!")

# calling the function
greet()
```

### 🔍 Explanation:

* `def greet()`: – defines a function named `greet`.
* The function executes the code in its block, printing a message.
* Calling `greet()` runs the function at the desired place in the program.

---

## 📝 2. Function with a parameter

Functions can accept **parameters**, which are input data that the function can use.

```python
def greet(name):
    print("Hello", name + "!")

greet("Ania")
greet("Tomek")
```

### 🔍 Explanation:

* `name` is a function parameter – a variable that receives a value when the function is called.
* The function executes the same instructions but with different input data.
* Parameters make the function reusable and more flexible.

---

## 📝 3. Function returning a value

A function can return a value using the `return` keyword.

```python
def add(a, b):
    sum = a + b
    return sum

result = add(3, 5)
print("Addition result:", result)
```

### 🔍 Explanation:

* `return sum` – the function returns the result of its operation.
* The returned value can be assigned to a variable (`result`) and used later.
* The function ends immediately after encountering `return`.

---

## 📝 4. Function with multiple parameters

A function can accept **more than one parameter**, allowing more complex operations.

```python
def multiply(a, b, c):
    return a * b * c

result = multiply(2, 3, 4)
print("Multiplication result:", result)
```

### 🔍 Explanation:

* The multiply function takes three arguments and returns their product.
* The number of parameters in the definition must match the number of arguments when calling the function.

---

## 📝 5. Function without parameters, returning different data types

A function does not always need parameters. It can also return different types of data.

```python
def welcome():
    return "Welcome to programming!"

text = welcome()
print(text)
```

### 🔍 Explanation:

* The `welcome` function takes no input.
* It returns a string that can be assigned to a variable and used later.

---

## 🎉 Lesson 15 Summary

* A function is a block of code that performs a specific task.
* Functions can accept parameters and return values.
* They allow you to organize code, repeat operations, and improve readability.
* Using functions makes your code more flexible and easier to maintain.

© 2025 PotegaIT – Python for Beginners

---
