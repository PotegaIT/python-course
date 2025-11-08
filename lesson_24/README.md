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

```yaml
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

© 2025 PotęgaIT – Kurs Python dla początkujących

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
```

### 🗣️ Explanation:

The program asks the user which operation to perform and then requests two numbers.
Depending on whether the user chose `+` or `-`, the program performs the calculation and displays the result.
If the user enters any other symbol, it shows an error message.

---

## 📝 2. Project 2 – Adding Multiplication and Division

Now, we’ll extend our calculator to also handle multiplication (`*`) and division (`/`).

### Code:

```python
# Text Calculator - Addition, Subtraction, Multiplication, and Division

print("Welcome to the text calculator!")
print("Choose an operation: + (addition), - (subtraction), * (multiplication), / (division)")

# Get operation from the user
operation = input("Enter operation: ")

# Get numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Perform calculation
if operation == "+":
    result = number1 + number2
    print("Addition result:", result)
elif operation == "-":
    result = number1 - number2
    print("Subtraction result:", result)
elif operation == "*":
    result = number1 * number2
    print("Multiplication result:", result)
elif operation == "/":
    if number2 != 0:
        result = number1 / number2
        print("Division result:", result)
    else:
        print("Error: cannot divide by zero!")
else:
    print("Unknown operation. Use +, -, * or /.")
```

### 🗣️ Explanation:

We added two new operations.
Notice the **division by zero check** — this prevents the program from crashing and ensures correct behavior.

### Code:

```python
# Text Calculator with Loop and Repeated Operations

while True:
    print("\nWelcome to the text calculator!")
    print("Choose an operation: + (addition), - (subtraction), * (multiplication), / (division)")

    # Get operation
    operation = input("Enter operation: ")

    # Get numbers
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    # Perform calculation
    if operation == "+":
        result = number1 + number2
        print("Addition result:", result)
    elif operation == "-":
        result = number1 - number2
        print("Subtraction result:", result)
    elif operation == "*":
        result = number1 * number2
        print("Multiplication result:", result)
    elif operation == "/":
        if number2 != 0:
            result = number1 / number2
            print("Division result:", result)
        else:
            print("Error: cannot divide by zero!")
    else:
        print("Unknown operation. Use +, -, * or /.")

    # Ask if user wants to continue
    continue_calc = input("Do you want to perform another operation? (yes/no): ").lower()
    if continue_calc != "yes":
        print("Thank you for using the calculator!")
        break
```

### 🗣️ Explanation:

The program now runs in an infinite `while True` loop.
After each operation, the user can decide whether to continue.
If they type anything other than “yes”, the program displays a goodbye message and exits.

### 🧠 Homework

Create a calculator that allows chaining multiple operations on one result.

Example:

```yaml
Result: 5
Choose next operation (*, /, +, -): *
Enter next number: 3
New result: 15
```

Use a loop and appropriate logic to make the program flow naturally.

---

## ✅ Summary

In this lesson, you learned how to:

* get user input with `input()`,
* convert data to numbers using `float()`,
* use conditional statements `if`, `elif`, `else`,
* handle logic errors like division by zero,
* build a loop-based interactive program.

This is one of the most valuable exercises in your learning journey — it shows how to combine Python basics into a real, working program.
A calculator like this is a classic example of a **CLI application**, where the user interacts with the program through text input and output.

© 2025 PotegaIT – Python Course for Beginners
