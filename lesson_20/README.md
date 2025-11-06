## 🇵🇱 Wersja polska

# 🧯 Lekcja 20: Obsługa wyjątków – try, except, finally

## 🎯 Cel lekcji
Nauczysz się, jak zabezpieczyć swój program przed niespodziewanymi błędami podczas działania. Poznasz trzy kluczowe elementy obsługi wyjątków w Pythonie:  
`try`, `except` i `finally`.

---

## 🗣️ Wprowadzenie

Każdy program może się „wysypać”, jeśli coś pójdzie nie tak – np. użytkownik wpisze błędne dane, plik się nie załaduje albo spróbujemy podzielić przez zero.  
W Pythonie nie musimy pozwalać, żeby błąd zakończył działanie programu. Zamiast tego możemy go **przechwycić, obsłużyć i bezpiecznie kontynuować**.

Tym właśnie zajmuje się **mechanizm obsługi wyjątków**.

---

## 🔍 1. Co to jest wyjątek?

**Wyjątek** to sytuacja, w której podczas działania programu pojawia się błąd — np. próba dzielenia przez zero lub błędne dane wejściowe.

Przykład:

```python
liczba = int(input("Podaj liczbę: "))
wynik = 10 / liczba
print("Wynik to:", wynik)
```

Jeśli użytkownik poda **0**, Python zgłosi błąd:

```python
ZeroDivisionError: division by zero
```

Właśnie taki komunikat to **wyjątek**.
Zamiast doprowadzać do awarii programu, możemy taki wyjątek przechwycić.

---

## 🧯 2. Podstawowa obsługa błędu (`try` - `except`)

Aby uniknąć zawieszenia programu, używamy bloku `try` i `except`.
W `try` umieszczamy kod, który może się nie udać.
W `except` – reakcję, jeśli coś pójdzie nie tak.

```python
try:
    liczba = int(input("Podaj liczbę: "))
    wynik = 10 / liczba
    print("Wynik to:", wynik)
except ZeroDivisionError:
    print("Nie można dzielić przez zero!")
```

Teraz, nawet jeśli użytkownik poda `0`, program się nie zawiesi — wyświetli komunikat i działa dalej.

---

## 🔄 3. Obsługa wielu błędów

Czasami może wystąpić więcej niż jeden typ błędu.
Możemy wtedy dodać kilka bloków `except` i każdy z nich obsłuży inny przypadek.

```python
try:
    liczba = int(input("Podaj liczbę: "))
    wynik = 10 / liczba
    print("Wynik to:", wynik)
except ZeroDivisionError:
    print("Nie dzielimy przez zero!")
except ValueError:
    print("Musisz podać poprawną liczbę!")
```

* Jeśli użytkownik wpisze **0**, uruchomi się `ZeroDivisionError`.
* Jeśli wpisze np. **abc**, uruchomi się `ValueError`.

Python sprawdza wyjątki **po kolei**, od góry do dołu.

---

## 🧹 4. Blok `finally`

Blok `finally` wykonuje się **zawsze** – niezależnie od tego, czy wystąpił błąd, czy nie.
Używamy go np. do „sprzątania” po operacjach: zamknięcia pliku, zwolnienia zasobów itp.

```python
try:
    plik = open("dane.txt", "r")
    zawartosc = plik.read()
    print(zawartosc)
except FileNotFoundError:
    print("Plik nie istnieje.")
finally:
    print("Koniec operacji na pliku.")
```

W tym przykładzie:

* Jeśli plik istnieje – program go odczyta i wyświetli.
* Jeśli nie – przechwyci błąd i poinformuje użytkownika.
* W obu przypadkach na końcu pojawi się komunikat z `finally`.

Dzięki temu masz **pełną kontrolę** nad tym, co się dzieje po każdej operacji.

---

## 🔧 5. Mini projekt – Kalkulator odporny na błędy

Stwórz prosty kalkulator, który:

* prosi użytkownika o dwie liczby,
* dzieli je przez siebie,
* obsługuje dwa typy błędów:
  * wpisanie tekstu zamiast liczby,
  * podanie zera jako dzielnika.

```python
try:
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    wynik = a / b
    print("Wynik dzielenia to:", wynik)
except ZeroDivisionError:
    print("Nie można dzielić przez zero!")
except ValueError:
    print("Wprowadź poprawne liczby!")
finally:
    print("Program zakończony.")
```

Ten prosty przykład pokazuje, jak stworzyć **bezpieczny program**, który nie wywala się z powodu błędnych danych.

---

## ✅ Podsumowanie

W tej lekcji nauczyłeś się jednej z najważniejszych zasad programowania:

> Dobry program nie przerywa działania z powodu błędu — przewiduje go i reaguje.

Dzięki użyciu:

* `try` – testujesz kod,
* `except` – przechwytujesz i obsługujesz błędy,
* `finally` – wykonujesz kod końcowy, niezależnie od wyniku.

Od teraz Twoje programy będą **stabilne, bezpieczne i profesjonalne**.
Już w następnych lekcjach zobaczysz, jak często ten mechanizm się przydaje — przy pracy z plikami, użytkownikiem czy siecią.

© 2025 PotęgaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version

# 🧯 Lesson 20: Exception Handling – try, except, finally

## 🎯 Lesson Objective
You will learn how to protect your program from unexpected runtime errors.  
We’ll explore three key elements of exception handling in Python:  
`try`, `except`, and `finally`.

---

## 🗣️ Introduction

Every program can “crash” if something goes wrong — for example, when a user enters invalid data, a file fails to load, or we try to divide by zero.  
In Python, we don’t have to let such errors stop our program.  
Instead, we can **catch them, handle them, and continue safely**.

This is exactly what the **exception handling mechanism** is for.

---

## 🔍 1. What Is an Exception?

An **exception** is an event that occurs when something goes wrong during the execution of a program — for example, dividing by zero or entering invalid input.

Example:

```python
number = int(input("Enter a number: "))
result = 10 / number
print("The result is:", result)
```

If the user enters **0**, Python will raise an error:

```python
ZeroDivisionError: division by zero
```

Such a message is an **exception**.
Instead of crashing the program, we can catch and handle this situation.

---

## 🧯 2. Basic Error Handling (`try` - `except`)

To prevent the program from crashing, we use the `try` and `except` blocks.
Inside `try`, we place the code that might fail.
Inside `except`, we define what should happen **if an error occurs**.

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("The result is:", result)
except ZeroDivisionError:
    print("You cannot divide by zero!")
```

Now, even if the user enters `0`, the program won’t crash — it will display a friendly message and keep running.

---

## 🔄 3. Handling Multiple Errors

Sometimes, more than one type of error may occur.
In that case, we can use multiple `except` blocks — one for each specific error.

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("The result is:", result)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("You must enter a valid number!")
```

* If the user enters **0**, `ZeroDivisionError` will be triggered.
* If they type something like **abc**, `ValueError` will occur.

Python checks exceptions **in order**, from top to bottom.

---

## 🧹 4. The `finally` Block

The `finally` block is **always executed** — no matter if an error occurred or not.
It’s used for “cleanup” operations like closing files or freeing resources.

```python
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("The file does not exist.")
finally:
    print("End of file operation.")
```

In this example:

* If the file exists, it’s read and printed.
* If it doesn’t, a clear error message is shown.
* In both cases, the code inside `finally` runs at the end.

This gives you **full control** over what happens after each operation.

---

## 🔧 5. Mini Project – Error-Resistant Calculator

Create a simple calculator that:

* asks the user for two numbers,
* divides them,
* handles two types of errors:
  * the user entered text instead of a number,
  * the user entered zero as the divisor.

```python
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = a / b
    print("The result is:", result)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Please enter valid numbers!")
finally:
    print("Program finished.")
```

This simple example shows how to build a **safe and stable** program that doesn’t crash due to invalid input.

---

## ✅ Summary

In this lesson, you learned one of the most important programming principles:

> A good program doesn’t stop because of an error — it predicts and handles it.

Using:

* try – you test the code,
* except – you catch and handle errors,
* finally – you run cleanup code regardless of the result.

From now on, your programs will be **stable, safe, and professional**.
In the next lessons, you’ll see how often this mechanism is useful — especially when working with files, user input, or network operations.

© 2025 PotegaIT – Python Course for Beginners
