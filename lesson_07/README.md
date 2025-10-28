## 🇵🇱 Wersja polska

# Lekcja 7: f-stringi i input()

## Wprowadzenie
Dziś przechodzimy do bardzo praktycznych rzeczy. Poznamy funkcję `input()`, dzięki której program może rozmawiać z użytkownikiem – czyli pobierać dane wpisywane z klawiatury.  
Następnie wrócimy do **f-stringów**, które pojawiły się już w poprzedniej lekcji, ale teraz dokładniej wytłumaczymy, jak działają i dlaczego są takie wygodne.  
To bardzo przydatne narzędzia, dzięki którym zaczniesz tworzyć pierwsze, w pełni interaktywne programy.

---

## 1. Funkcja `input()`
Funkcja `input()` zatrzymuje działanie programu i czeka, aż użytkownik wpisze coś z klawiatury. Po wciśnięciu Enter program rusza dalej. Wszystko, co wpiszemy, jest traktowane jako tekst (`str`).  
Jeśli potrzebujemy liczbę, trzeba dodatkowo użyć funkcji `int()` lub `float()`.

### 📘 Przykład:

```python
name = input("Jak masz na imię? ")
print("Witaj,", name)

age = input("Ile masz lat? ")
print("Za rok będziesz miał", int(age) + 1, "lat.")
```
## 2. F-stringi

F-stringi (ang. *formatted string literals*) to nowoczesny i wygodny sposób łączenia tekstu z wartościami zmiennych w Pythonie. Są dostępne od wersji 3.6 i szybko stały się standardem, ponieważ są czytelniejsze i prostsze od starszych metod.

Działają w ten sposób, że przed cudzysłowem dodajemy literę `f`, a wewnątrz napisu możemy wpisywać zmienne w nawiasach klamrowych `{}`. Python automatycznie zamieni te nawiasy na wartości zmiennych.

### 📘 Przykład:

```python
name = "Ania"
age = 12

# Użycie f-stringa
print(f"Cześć, mam na imię {name} i mam {age} lat.")
```
### Wynik:
`Cześć, mam na imię Ania i mam 12 lat.`

Dla porównania, starsze metody:
```python
# Starszy styl z konkatenacją
print("Cześć, mam na imię " + name + " i mam " + str(age) + " lat.")

# Starszy styl z format()
print("Cześć, mam na imię {} i mam {} lat.".format(name, age))
```
F-stringi są znacznie bardziej czytelne – wystarczy wstawić zmienne dokładnie tam, gdzie mają się pojawić w tekście.
```python
name = "Greg"
age = 30
print(f"Cześć, {name}! Masz {age} lat.")
```
## 💡 3. Mini projekt – interaktywny program

Zróbmy teraz prosty program, który zapyta użytkownika o imię i wiek, a następnie wyświetli powitanie oraz poinformuje, ile lat osoba będzie miała za rok.
```python
# Pobieranie danych od użytkownika
name = input("Jak masz na imię? ")
age = input("Ile masz lat? ")

# Wyświetlenie powitania i obliczenie wieku za rok
print(f"Witaj, {name}! Za rok będziesz miał {int(age) + 1} lat.")
```
⚠️ **Ważne**: input() zawsze zwraca tekst, nawet jeśli wpiszesz liczbę. Dlatego używamy int() do konwersji wieku na liczbę, żeby móc dodać 1.

## ✅ Podsumowanie

To już kolejna lekcja, a Ty potrafisz tworzyć programy, które rozmawiają z użytkownikiem i reagują na dane wejściowe.
Znasz funkcję input() i potrafisz używać f-stringów, czyli wygodnego sposobu na łączenie tekstu i zmiennych.
Tworzysz teraz programy, które nie tylko „coś robią”, ale też wchodzą w interakcję z użytkownikiem. Brawo!

© 2025 PotegaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version

# Lesson 7: F-strings and input()

## Introduction
Today we are moving on to very practical topics. We will learn about the `input()` function, which allows a program to interact with the user – that is, to receive data typed from the keyboard.  
Then we will return to **f-strings**, which appeared briefly in the previous lesson, but this time we will explain in detail how they work and why they are so convenient.  
These are very useful tools that will help you create your first fully interactive programs.

---

## 1. The `input()` Function
The `input()` function pauses the program and waits for the user to type something on the keyboard. After pressing Enter, the program continues. Everything entered is treated as text (`str`).  
If you need a number, you must additionally use `int()` or `float()`.

### 📘 Example:

```python
name = input("What is your name? ")
print("Hello,", name)

age = input("How old are you? ")
print("Next year you will be", int(age) + 1, "years old.")
```
## 2. F-strings

F-strings (short for *formatted string literals*) are a modern and convenient way to combine text with variable values in Python. They are available from version 3.6 and quickly became standard because they are more readable and simpler than older methods.

They work by adding the letter `f` before the quotation marks. Inside the string, you can insert variables within curly braces `{}`. Python automatically replaces the braces with the variable values.

📘 **Example:**

```python
name = "Greg"
age = 25
print(f"My name is {name} and I am {age} years old.")
```
**Outout:
`Hi, my name is Anna and I am 12 years old.`

For comparison, older methods:
```python
# Older style with concatenation
print("Hi, my name is " + name + " and I am " + str(age) + " years old.")

# Older style with format()
print("Hi, my name is {} and I am {} years old.".format(name, age))
```
F-strings are much cleaner – just insert the variables exactly where you want them in the text.
```python
name = "Greg"
age = 30
print(f"Hi, {name}! You are {age} years old.")
```
## 💡 3. Mini Project – Interactive Program

Let's create a simple program that asks the user for their name and age, then prints a greeting and tells them how old they will be next year.
```python
# Getting data from the user
name = input("What is your name? ")
age = input("How old are you? ")

# Printing the greeting and calculating age next year
print(f"Hello, {name}! Next year you will be {int(age) + 1} years old.")
```
⚠️ **Important**: input() always returns text, even if you enter a number. That's why we use int() to convert the age to a number so we can add 1.

## ✅ Summary

This is another lesson, and now you can create programs that interact with the user and respond to input.
You know how to use input() and f-strings, a convenient way to combine text and variables.
You are now creating programs that not only "do something," but also interact with the user. Well done!

© 2025 PotegaIT – Python Course for Beginners

