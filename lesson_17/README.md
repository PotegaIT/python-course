## 🇵🇱 Wersja polska

# 🧠 Lekcja 17 – Debugowanie i czytanie błędów w Pythonie

---

## 🎯 Cel lekcji

W tej lekcji nauczysz się, jak rozpoznawać, czytać i obsługiwać błędy w Pythonie.
Dzięki temu:

* łatwiej zlokalizujesz problemy w kodzie,
* szybciej naprawisz błędy,
* poznasz techniki debugowania, takie jak print() oraz try/except,
* nauczysz się pisać bardziej odporne i stabilne programy.

Debugowanie jest fundamentem pracy każdego programisty – błędy zdarzają się każdemu, ale umiejętność ich rozwiązywania odróżnia dobrych programistów od początkujących.

---

## 📝 1. Rodzaje błędów

W Pythonie wyróżniamy dwa główne typy błędów:

* **Błędy składniowe (SyntaxError)** – błędy uniemożliwiające uruchomienie programu.
* **Błędy wykonania (RuntimeError, ValueError, ZeroDivisionError itd.)** – pojawiają się w trakcie działania programu.

### 🔧 Przykład 1 – Błąd składniowy

```python
print("Witaj"
```

💬 Python zgłosi `SyntaxError` – brak nawiasu zamykającego. Takie błędy trzeba poprawić przed uruchomieniem programu.

### 🔧 Przykład 2 – Błąd wykonania

```python
liczba = int("abc")
```

💬 Kod uruchamia się, ale w momencie próby konwersji `"abc"` na liczbę Python zgłosi `ValueError`.

---

## 📝 2. Jak czytać komunikaty o błędach (traceback)

Traceback to komunikat wyświetlany przez Pythona w momencie błędu. Zawiera:

* nazwę pliku,
* numer linii,
* nazwę funkcji (jeśli dotyczy),
* typ błędu (np. `TypeError`, `NameError`),
* krótki opis błędu.

### 🔧 Przykład 3 – NameError

```python
print(imie)
```

**📜 Traceback:**

```python
NameError: name 'imie' is not defined
```

💬 Python informuje, że zmienna `imie` nie została zdefiniowana.

### 🔧 Przykład 4 – IndexError

```python
lista = [1, 2, 3]
print(lista[5])
```

**📜 Traceback:**

```python
IndexError: list index out of range
```

💬 Próba odczytu elementu spoza zakresu listy.

---

## 📝 3. Technika print-debugging

Czasami najlepiej dodać **print()** w kluczowych miejscach kodu, aby sprawdzić wartości zmiennych i przebieg programu.

### 🔧 Przykład 5

```python
def dzielenie(a, b):
    print("a =", a)
    print("b =", b)
    wynik = a / b
    return wynik

dzielenie(10, 0)
```

**📜 Traceback:**

```python
ZeroDivisionError: division by zero
```

💬 Dzięki `print()` widzimy, że `b` = 0, co powoduje błąd dzielenia.

---

## 📝 4. Wstęp do try/except

Konstrukcja `try/except` pozwala obsłużyć **potencjalne błędy**, aby program nie zakończył się niekontrolowanie.

### 🔧 Przykład 6

```python
try:
    liczba = int(input("Podaj liczbę: "))
    print("Liczba x 2 =", liczba * 2)
except ValueError:
    print("To nie była liczba!")
```

💬 Jeśli użytkownik poda nieprawidłową wartość, program wyświetli komunikat, zamiast zgłosić błąd.

---

## 🧩 Mini-projekt: Kalkulator bez awarii

Stwórz prosty kalkulator, który:

* pyta użytkownika o dwie liczby,
* dzieli pierwszą przez drugą,
* obsługuje błędy wprowadzania danych i dzielenia przez zero.

```python
def kalkulator():
    try:
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        wynik = a / b
        print("Wynik dzielenia:", wynik)
    except ValueError:
        print("Wprowadź prawidłową liczbę!")
    except ZeroDivisionError:
        print("Nie dzielimy przez zero!")

kalkulator()
```

## 🎉 Podsumowanie lekcji 17

* Błędy zdarzają się każdemu – kluczowe jest umiejętne ich diagnozowanie.
* Nauczyłeś się rozpoznawać **błędy składniowe i wykonania**.
* Poznałeś sposób czytania komunikatów `traceback`.
* Wykorzystałeś `print()` jako narzędzie debugowania.
* Wstępnie zapoznałeś się z `try/except`, aby zabezpieczać program przed awariami.

Opanowanie tych umiejętności jest fundamentem pracy każdego programisty – nie chodzi o to, by całkowicie unikać błędów, lecz by umieć je diagnozować i skutecznie rozwiązywać.

© 2025 PotęgaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version

# 🧠 Lesson 17 – Debugging and Reading Errors in Python

---

## 🎯 Lesson Objective

In this lesson, you will learn how to identify, **read, and handle errors in Python**.
Thanks to this, you will be able to:

* locate problems in your code more easily,
* fix errors faster,
* learn debugging techniques such as `print()` and `try/except`,
* write more resilient and stable programs.

Debugging is a fundamental skill for every programmer – errors happen to everyone, but knowing how to handle them efficiently sets experienced developers apart from beginners.

---

## 📝 1. Types of Errors

In Python, there are two main types of errors:

* **Syntax errors (SyntaxError)** – prevent the program from running at all.
* **Runtime errors (RuntimeError, ValueError, ZeroDivisionError, etc.)** – occur during program execution.

### 🔧 Example 1 – Syntax Error

```python
print("Hello"
```

💬 Python will raise a `SyntaxError` – a missing closing parenthesis. These errors must be fixed before running the program.

### 🔧 Example 2 – Runtime Error

```python
number = int("abc")
```

💬 The code runs, but when Python tries to convert `"abc"` to a number, it raises a `ValueError`.

---

## 📝 2. How to Read Error Messages (Traceback)

A traceback is the message Python displays when an error occurs. It contains:

* the file name,
* the line number,
* the function name (if applicable),
* the error type (e.g., `TypeError`, `NameError`),
* a brief description of the error.

### 🔧 Example 3 – NameError

```python
print(name)
```

**📜 Traceback:**

```python
NameError: name 'name' is not defined
```

💬 Python informs you that the variable `name` was not defined.

### 🔧 Example 4 – IndexError

```python
my_list = [1, 2, 3]
print(my_list[5])
```

**📜 Traceback:**

```python
IndexError: list index out of range
```

💬 Attempting to access an element outside the list’s range.

---

## 📝 3. Print-Debugging Technique

Sometimes, the easiest way to understand what’s happening is to add **print()** statements at key points in your code to inspect variable values and program flow.

### 🔧 Example 5

```python
def divide(a, b):
    print("a =", a)
    print("b =", b)
    result = a / b
    return result

divide(10, 0)
```

**📜 Traceback:**

```python
ZeroDivisionError: division by zero
```

💬 The `print()` statements reveal that `b` = 0, which causes the division error.

---

## 📝 4. Introduction to try/except

The `try/except` construct allows you to **handle potential errors** so that the program does not crash unexpectedly.

### 🔧 Example 6

```python
try:
    number = int(input("Enter a number: "))
    print("Number x 2 =", number * 2)
except ValueError:
    print("That was not a number!")
```

💬 If the user enters invalid input, the program will display a message instead of raising an error.

---

## 🧩 Mini-Project: Crash-Proof Calculator

Create a simple calculator that:

* asks the user for two numbers,
* divides the first number by the second,
* handles invalid input and division by zero.

```python
def calculator():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        result = a / b
        print("Division result:", result)
    except ValueError:
        print("Please enter a valid number!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")

calculator()
```

---

## 🎉 Lesson 17 Summary

* Errors happen to everyone – the key is to diagnose them effectively.
* You learned to recognize syntax and runtime errors.
* You learned how to read `traceback` messages.
* You used `print()` as a debugging tool.
* You got an introduction to `try/except` to protect programs from crashing.

Mastering these skills is essential for any programmer – the goal is not to completely avoid errors, but to be able to diagnose and fix them efficiently.

© 2025 PotegaIT – Python for Beginners
