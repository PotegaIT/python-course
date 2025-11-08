## 🇵🇱 Wersja polska

# 🧮 Lekcja 24: Kalkulator tekstowy (CLI)

---

## 🎯 Cel lekcji

W tej lekcji stworzysz prosty kalkulator tekstowy działający w wierszu poleceń (CLI – Command Line Interface).

Dzięki temu nauczysz się:

* pobierać dane od użytkownika,
* wykonywać operacje matematyczne,
* obsługiwać błędy (np. dzielenie przez zero),
* stosować pętlę, aby program działał wielokrotnie bez ponownego uruchamiania.

To praktyczne ćwiczenie, które pozwoli Ci lepiej zrozumieć, jak tworzyć programy działające w terminalu.

---

## 📝 1. Projekt 1 – Kalkulator dodawania i odejmowania

Zaczniemy od najprostszego kalkulatora, który obsługuje **dodawanie** i **odejmowanie**.

### Kod:

```python
# Kalkulator tekstowy - dodawanie i odejmowanie

print("Witaj w kalkulatorze tekstowym!")
print("Wybierz operację: + (dodawanie), - (odejmowanie)")

# Pobieramy operację
operacja = input("Podaj operację: ")

# Pobieramy liczby
liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))

# Wykonujemy obliczenia na podstawie wybranej operacji
if operacja == "+":
    wynik = liczba1 + liczba2
    print("Wynik dodawania:", wynik)
elif operacja == "-":
    wynik = liczba1 - liczba2
    print("Wynik odejmowania:", wynik)
else:
    print("Nieznana operacja. Użyj + lub -.")
```

### 🗣️ Wyjaśnienie:

Program pyta użytkownika o rodzaj operacji oraz dwie liczby.
Na podstawie wybranego symbolu (`+` lub `-`) wykonuje odpowiednie działanie i wyświetla wynik.
Jeśli użytkownik wpisze inny symbol – program zwróci komunikat o błędzie.

---

## 📝 2. Projekt 2 – Dodanie mnożenia i dzielenia

Teraz rozszerzymy nasz kalkulator o mnożenie (`*`) i dzielenie (`/`).

### Kod

```python
# Kalkulator tekstowy - dodawanie, odejmowanie, mnożenie i dzielenie

print("Witaj w kalkulatorze tekstowym!")
print("Wybierz operację: + (dodawanie), - (odejmowanie), * (mnożenie), / (dzielenie)")

# Pobieramy operację
operacja = input("Podaj operację: ")

# Pobieramy liczby
liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))

# Wykonujemy obliczenia na podstawie wybranej operacji
if operacja == "+":
    wynik = liczba1 + liczba2
    print("Wynik dodawania:", wynik)
elif operacja == "-":
    wynik = liczba1 - liczba2
    print("Wynik odejmowania:", wynik)
elif operacja == "*":
    wynik = liczba1 * liczba2
    print("Wynik mnożenia:", wynik)
elif operacja == "/":
    if liczba2 != 0:
        wynik = liczba1 / liczba2
        print("Wynik dzielenia:", wynik)
    else:
        print("Błąd: nie można dzielić przez zero!")
else:
    print("Nieznana operacja. Użyj +, -, * lub /.")
```

### 🗣️ Wyjaśnienie:

Dodaliśmy dwie nowe operacje.
Zwróć uwagę na **sprawdzenie dzielenia przez zero** — to ważny element kontroli błędów, który chroni przed niepoprawnym działaniem programu.

---

## 📝 3. Projekt 3 – Kalkulator z pętlą (powtarzanie operacji)

Teraz sprawimy, by kalkulator działał w **pętli**, czyli by użytkownik mógł wykonywać kolejne obliczenia bez ponownego uruchamiania programu.

### Kod:

```python
# Kalkulator tekstowy z pętlą i możliwością powtarzania operacji

while True:
    print("\nWitaj w kalkulatorze tekstowym!")
    print("Wybierz operację: + (dodawanie), - (odejmowanie), * (mnożenie), / (dzielenie)")

    # Pobieramy operację
    operacja = input("Podaj operację: ")

    # Pobieramy liczby
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))

    # Wykonujemy obliczenia na podstawie wybranej operacji
    if operacja == "+":
        wynik = liczba1 + liczba2
        print("Wynik dodawania:", wynik)
    elif operacja == "-":
        wynik = liczba1 - liczba2
        print("Wynik odejmowania:", wynik)
    elif operacja == "*":
        wynik = liczba1 * liczba2
        print("Wynik mnożenia:", wynik)
    elif operacja == "/":
        if liczba2 != 0:
            wynik = liczba1 / liczba2
            print("Wynik dzielenia:", wynik)
        else:
            print("Błąd: nie można dzielić przez zero!")
    else:
        print("Nieznana operacja. Użyj +, -, * lub /.")

    # Pytamy, czy użytkownik chce kontynuować
    kontynuować = input("Czy chcesz wykonać kolejną operację? (tak/nie): ").lower()
    if kontynuować != "tak":
        print("Dziękujemy za korzystanie z kalkulatora!")
        break
```

### 🗣️ Wyjaśnienie:

Program działa w nieskończonej pętli `while True`.
Po każdej operacji użytkownik decyduje, czy chce kontynuować.
Jeśli wpisze coś innego niż „tak”, pętla się kończy i program wyświetla pożegnalny komunikat.

### 🧠 Zadanie domowe

Stwórz kalkulator, który umożliwia wykonanie kilku operacji po kolei na jednym wyniku.

Na przykład:

```python
Wynik: 5
Wybierz kolejną operację (*, /, +, -): *
Podaj kolejną liczbę: 3
Nowy wynik: 15
```

Wykorzystaj pętlę i odpowiednią logikę, aby program działał płynnie.

---

## ✅ Podsumowanie

W tej lekcji nauczyłeś się:

* pobierać dane z klawiatury przy użyciu `input()`,
* konwertować dane na liczby (`float()`),
* stosować instrukcje warunkowe `if`, `elif`, `else`,
* obsługiwać błędy logiczne (np. dzielenie przez zero),
* tworzyć program działający w pętli.

To jedno z najważniejszych ćwiczeń praktycznych — pokazuje, jak połączyć wiele podstawowych elementów Pythona w jeden działający program.
Taki kalkulator to klasyczny przykład aplikacji CLI, czyli programu, z którym użytkownik wchodzi w interakcję za pomocą tekstu.

© 2025 PotegaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version

🧮 Lesson 24: Text-Based Calculator (CLI)

---

## 🎯 Lesson Goal

In this lesson, you’ll create a simple text-based calculator that runs in the **command line (CLI – Command Line Interface)**.

By the end, you’ll learn how to:

* get input from the user,
* perform basic mathematical operations,
* handle errors (like division by zero),
* use loops to keep your program running without restarting it.

This is a practical project that shows how to make simple interactive programs directly in the terminal.

---

## 📝 1. Project 1 – Addition and Subtraction Calculator

We’ll start with a simple calculator that supports **addition** and **subtraction**.

### Code:

```python
# Text Calculator - Addition and Subtraction

print("Welcome to the text calculator!")
print("Choose an operation: + (addition), - (subtraction)")

# Get operation from the user
operation = input("Enter operation: ")

# Get numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Perform calculation based on the chosen operation
if operation == "+":
    result = number1 + number2
    print("Addition result:", result)
elif operation == "-":
    result = number1 - number2
    print("Subtraction result:", result)
else:
    print("Unknown operation. Use + or -.")
# Text Calculator - Addition and Subtraction

print("Welcome to the text calculator!")
print("Choose an operation: + (addition), - (subtraction)")

# Get operation from the user
operation = input("Enter operation: ")

# Get numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Perform calculation based on the chosen operation
if operation == "+":
    result = number1 + number2
    print("Addition result:", result)
elif operation == "-":
    result = number1 - number2
    print("Subtraction result:", result)
else:
    print("Unknown operation. Use + or -.")```
