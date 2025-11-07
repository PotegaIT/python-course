## 🇵🇱 Wersja polska

# 🧮 Lekcja 21: Wbudowane moduły – `math`, `random`, `datetime`

---

## 🎯 Cel lekcji

W tej lekcji poznasz **trzy wbudowane moduły Pythona**:

- `math` – funkcje matematyczne, pierwiastki, potęgi, wartości bezwzględne, liczba Pi,  
- `random` – losowe liczby i wybór elementów z kolekcji,  
- `datetime` – praca z datą i czasem, porównywanie dat, mierzenie różnic czasowych.

Dzięki tym modułom możesz realizować bardziej zaawansowane obliczenia, tworzyć gry, aplikacje i programy wymagające losowości czy pomiaru czasu.

---

## 📝 1. Moduł `math`

### Przykłady użycia:

```python
import math

print("Pierwiastek z 16:", math.sqrt(16))          # √16 = 4.0
print("2 do potęgi 3:", math.pow(2, 3))            # 2^3 = 8.0
print("Wartość bezwzględna z -5:", math.fabs(-5))  # 5.0
print("Liczba Pi:", math.pi)                        # 3.1415926535...
```

### 🗣️ Wyjaśnienie:

* `math.sqrt(x)` – pierwiastek kwadratowy liczby `x`, zawsze float.
* `math.pow(a, b)` – potęgowanie `a` do `b`, zawsze float.
* `math.fabs(x)` – wartość bezwzględna liczby `x`, zawsze float.
* `math.pi` – stała Pi, przydatna w obliczeniach geometrycznych.

---

## 📝 2. Moduł `random`

### Przykłady użycia:

```python
import random

print("Losowa liczba od 1 do 10:", random.randint(1, 10))
print("Losowy wybór z listy:", random.choice(["kot", "pies", "mysz"]))
```

### 🗣️ Wyjaśnienie:

* `random.randint(a, b)` – losowa liczba całkowita z przedziału `[a, b]`.
* `random.choice(lista)` – losowy wybór elementu z listy.
* Przydatne w grach, quizach, symulacjach i losowaniach.

---

## 📝 3. Moduł `datetime`

### Przykłady użycia:

```python
import datetime

teraz = datetime.datetime.now()
print("Aktualna data i godzina:", teraz)

konkretna_data = datetime.datetime(2023, 12, 31)
print("Sylwester:", konkretna_data)
```

### 🗣️ Wyjaśnienie:

* `datetime.datetime.now()` – pobiera aktualną datę i czas.
* `datetime.datetime(rok, miesiac, dzien)` – tworzy konkretną datę.
* Moduł umożliwia porównywanie dat, liczenie różnic czasowych i odliczanie.

---

## 🛠️ 4. Mini projekt – Gra w zgadywanie liczby z pomiarem czasu

### Kod:

```python
import random
import datetime
import math

liczba = random.randint(1, 100)
start = datetime.datetime.now()
proby = 0

while True:
    strzal = int(input("Zgadnij liczbę od 1 do 100: "))
    proby += 1

    if strzal == liczba:
        break
    elif strzal < liczba:
        print("Za mało!")
    else:
        print("Za dużo!")

koniec = datetime.datetime.now()
czas = koniec - start

bazowa_wartosc = max(1, 10 - proby)
punkty = math.pow(bazowa_wartosc, 2) * 10

print(f"Twój wynik punktowy: {int(punkty)} punktów!")
print("Zajęło Ci to:", czas)

optymalna_liczba_prob = math.ceil(math.log2(100))
print("🔍 Teoretycznie, przy metodzie 'połówek', można było zgadnąć w maksymalnie", optymalna_liczba_prob, "próbach.")
```

### 🗣️ Wyjaśnienie:

* `random` – losowanie liczby do zgadnięcia.
* `datetime` – mierzenie czasu od startu do trafienia liczby.
* `math.pow` – wyliczanie punktów na podstawie liczby prób.
* Gra kończy się po trafieniu liczby, pokazuje czas i wynik punktowy.
* `math.log2(100)` – szacowanie optymalnej liczby prób przy metodzie „połówek”.

---

## ✅ Podsumowanie

W tej lekcji nauczyłeś się używać wbudowanych modułów:

* `math` – matematyka i funkcje numeryczne,
* `random` – losowość i wybory z kolekcji,
* `datetime` – data, czas i różnice czasowe.

Pozwalają one tworzyć bardziej zaawansowane programy, zarówno do prostych obliczeń, jak i do interaktywnych gier czy aplikacji z pomiarem czasu.
Opanowanie tych modułów jest fundamentem dalszych projektów programistycznych.

© 2025 PotęgaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version

# 🧮 Lesson 21: Built-in Modules – `math`, `random`, `datetime`

---

## 🎯 Lesson Goal

In this lesson, you will learn about **three built-in Python modules**:

- `math` – mathematical functions, square roots, powers, absolute values, Pi,  
- `random` – random numbers and selecting elements from a collection,  
- `datetime` – working with date and time, comparing dates, calculating time differences.

These modules allow you to perform more advanced calculations, create games, applications, and programs requiring randomness or time measurement.

---

## 📝 1. The `math` Module

### Example Usage:

```python
import math

print("Square root of 16:", math.sqrt(16))         # √16 = 4.0
print("2 to the power of 3:", math.pow(2, 3))      # 2^3 = 8.0
print("Absolute value of -5:", math.fabs(-5))      # 5.0
print("Value of Pi:", math.pi)                     # 3.1415926535...
```

### 🗣️ Explanation:

* `math.sqrt(x)` – square root of `x`, always returns a float.
* `math.pow(a, b)` – raises `a` to the power of `b`, always returns a float.
* `math.fabs(x)` – absolute value of `x`, always returns a float.
* `math.pi` – the constant Pi, useful for geometric calculations.

---

## 📝 2. The `random` Module

### Example Usage:

```python
import random

print("Random number from 1 to 10:", random.randint(1, 10))
print("Random choice from a list:", random.choice(["cat", "dog", "mouse"]))
```

### 🗣️ Explanation:

* `random.randint(a, b)` – a random integer between `[a, b]`.
* `random.choice(list)` – randomly selects an element from the list.
* Useful for games, quizzes, simulations, and lotteries.

---

## 📝 3. The `datetime` Module

### Example Usage:

```python
import datetime

now = datetime.datetime.now()
print("Current date and time:", now)

specific_date = datetime.datetime(2023, 12, 31)
print("New Year's Eve:", specific_date)
```

### 🗣️ Explanation:

* `datetime.datetime.now()` – gets the current date and time.
* `datetime.datetime(year, month, day)` – creates a specific date.
* The module allows comparing dates, calculating time differences, and countdowns.

---

## 🛠️ 4. Mini Project – Number Guessing Game with Time Measurement

### Code:

```python
import random
import datetime
import math

number = random.randint(1, 100)
start = datetime.datetime.now()
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess == number:
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

end = datetime.datetime.now()
duration = end - start

base_score = max(1, 10 - attempts)
points = math.pow(base_score, 2) * 10

print(f"Your score: {int(points)} points!")
print("It took you:", duration)

optimal_attempts = math.ceil(math.log2(100))
print("🔍 Theoretically, using the 'halving method', the number could be guessed in a maximum of", optimal_attempts, "attempts.")

```

### 🗣️ Explanation:

* `random` – selects the number to guess.
* `datetime` – measures time from start to correct guess.
* `math.pow` – calculates points based on attempts.
* The game ends when the number is guessed, showing the time taken and score.
* `math.log2(100)` – estimates the optimal number of guesses using the halving method.

---

## ✅ Summary

In this lesson, you learned how to use built-in Python modules:

* `math` – mathematics and numeric functions,
* `random` – randomness and selections from collections,
* `datetime` – date, time, and time differences.

They allow you to create more advanced programs, from simple calculations to interactive games and applications with time tracking.
Mastering these modules forms a solid foundation for future programming projects.

© 2025 PotegaIT – Python Course for Beginners
