## 🇵🇱 Wersja polska

# 🧠 Lekcja 13 – Sterowanie przebiegiem pętli: break i continue

---

## 🎯 Cel lekcji

W tej lekcji nauczysz się, jak dokładnie kontrolować działanie pętli.
Poznasz dwa bardzo przydatne słowa kluczowe w Pythonie – `break` i `continue`.

Dzięki nim możesz:

* przerwać pętlę w dowolnym momencie (`break`),
* pominąć jeden krok i przejść dalej (`continue`).

To potężne narzędzia, które dają Ci większą kontrolę nad przebiegiem programu.

---

## 📝 1. Instrukcja `break` – przerywanie pętli

Instrukcja `break` działa jak **przycisk awaryjny**.
Kiedy Python ją napotka, **natychmiast kończy działanie pętli**, nawet jeśli warunek pętli wciąż jest spełniony.
Używamy jej wtedy, gdy nie ma sensu kontynuować dalszego działania – np. gdy znaleźliśmy to, czego szukaliśmy.

```python
for liczba in range(10):
    if liczba == 5:
        print("Znaleziono 5! Kończę.")
        break
    print("Sprawdzam:", liczba)
```

### 🔍 Wyjaśnienie:

* Program sprawdza liczby od 0 do 9.
* Gdy napotka 5 – przerywa pętlę.
* Liczby po 5 nie zostaną już sprawdzone.

---

## 📝 2. Instrukcja `continue` – pomijanie jednej iteracji

Instrukcja `continue` działa odwrotnie niż `break`.
Nie kończy pętli, ale pomija tylko bieżący krok i przechodzi do następnego.

To tak, jakbyś powiedział:

> „Tego przypadku nie chcę – idź dalej!”

```python
liczby = [3, -1, 7, -4, 5]

for liczba in liczby:
    if liczba < 0:
        continue
    print("Pozytywna liczba:", liczba)
```

### 🔍 Wyjaśnienie:

* Program pomija liczby ujemne (`continue`).
* Dla dodatnich wykonuje `print()`.
* Dzięki temu pętla działa selektywnie – przetwarza tylko dane, które nas interesują.

---

## 🧮 3. break i continue w pętli while

Obie instrukcje działają również w pętli `while`.
To szczególnie przydatne, gdy pętla działa na podstawie danych użytkownika lub zmieniających się warunków.\

```python
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    if i == 7:
        break
    print(i)
```

### 🔍 Wyjaśnienie:

* Zmienna `i` zwiększa się od 1 do 10.
* Gdy osiągnie 3 – `continue` pomija drukowanie.
* Gdy osiągnie 7 – `break` kończy pętlę.
* Efekt: program drukuje 1, 2, 4, 5, 6.

---

## 🧩 4. Mini projekt – filtr liczb od użytkownika

> Stwórz program, który pobiera liczby od użytkownika i przetwarza je w zależności od wartości.

```python
while True:
    liczba = int(input("Podaj liczbę: "))

    if liczba == 0:
        print("Koniec – wpisałeś 0.")
        break

    if liczba == 100:
        print("Liczba specjalna 100 – kończę program.")
        break

    if liczba < 0:
        print("Liczba ujemna – pomijam.")
        continue

    print("Liczba:", liczba)
```

### 🔍 Wyjaśnienie:

* Pętla działa w nieskończoność (`while True`).
* `break` przerywa program dla 0 lub 100.
* `continue` pomija liczby ujemne.
* Tylko liczby dodatnie są drukowane.

### 💡 Rozbudowana wersja – licznik i suma liczb dodatnich

Dodajmy licznik i sumę liczb dodatnich, aby pod koniec wyświetlić podsumowanie:

```python
licznik = 0
suma = 0

while True:
    liczba = int(input("Podaj liczbę: "))

    if liczba == 0:
        print("Koniec – wpisałeś 0.")
        break

    if liczba == 100:
        print("Liczba specjalna 100 – kończę program.")
        break

    if liczba < 0:
        print("Liczba ujemna – pomijam.")
        continue

    licznik += 1
    suma += liczba
    print("Liczba:", liczba)

print(f"\nWprowadziłeś {licznik} liczb dodatnich. Suma to {suma}.")
```

### 🔍 Wyjaśnienie:

* `licznik` zlicza liczby dodatnie.
* `suma` dodaje ich wartości.
* `break` kończy działanie programu.
* `continue` pomija niechciane dane.

### 🧠 Wniosek

To już całkiem praktyczny program!  
Łączy w sobie:

* pętle `while`,
* instrukcje `break` i `continue`,
* obsługę danych użytkownika,
* warunki i operacje arytmetyczne.

To jedne z fundamentów programowania – dzięki nim Twoje programy stają się elastyczne i inteligentne.  

---

## 🎉 Podsumowanie lekcji 13

* `break` – przerywa pętlę w dowolnym momencie.
* `continue` – pomija jeden krok i przechodzi dalej.
* Obie instrukcje dają Ci większą kontrolę nad przebiegiem programu.

Dzięki nim możesz tworzyć bardziej precyzyjne i efektywne rozwiązania.

© 2025 PotęgaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version

# 🧠 Lesson 13 – Controlling Loops: break and continue

---

## 🎯 Lesson Goal

In this lesson, you will learn how to control the flow of loops more precisely.
You will get to know two very useful Python keywords – `brea`k and `continue`.

With them, you can:

* stop a loop at any point (`break`),
* skip one iteration and continue (`continue`).

These are powerful tools that give you greater control over your program’s execution.

## 📝 1. `break` – stopping a loop

The `break` statement acts like an **emergency stop button**.
When Python encounters it, the loop **immediately ends**, even if the loop condition is still true.
We use it when there’s **no reason to continue** – for example, when we found what we were looking for.

```python
for number in range(10):
    if number == 5:
        print("Found 5! Stopping.")
        break
    print("Checking:", number)
```

### 🔍 Explanation:

* The program checks numbers from 0 to 9.
* When it encounters 5 – the loop stops.
* Numbers after 5 are not processed.

---

## 📝 2. `continue` – skipping an iteration

The `continue` statement works differently from `break`.
It **does not stop the loop**, but **skips the current iteration** and moves to the next one.

It’s like saying:

> “I’m not interested in this one – move on!”

```python
numbers = [3, -1, 7, -4, 5]

for number in numbers:
    if number < 0:
        continue
    print("Positive number:", number)
```

### 🔍 Explanation:

* The program skips negative numbers (`continue`).
* For positive numbers, it executes `print()`.
* This makes the loop selective – it processes only the values we care about.

---

## 🧮 3. `break` and `continue` in `while` loops

Both statements also work in `while` loops.
This is especially useful when the loop depends on **user input** or **changing conditions**.

```python
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    if i == 7:
        break
    print(i)
```

### 🔍 Explanation:

* The variable `i` increases from 1 to 10.
* When it reaches 3 – `continue` skips printing.
* When it reaches 7 – `break` stops the loop.
* Result: prints 1, 2, 4, 5, 6.

---

## 🧩 4. Mini project – user number filter
> Create a program that reads numbers from the user and processes them depending on their value.

```python
while True:
    number = int(input("Enter a number: "))

    if number == 0:
        print("Finished – you entered 0.")
        break

    if number == 100:
        print("Special number 100 – stopping the program.")
        break

    if number < 0:
        print("Negative number – skipping.")
        continue

    print("Number:", number)
```

### 🔍 Explanation:

* The loop runs indefinitely ('while True').
* 'break' stops the program for 0 or 100.
* 'continue' skips negative numbers.
* Only positive numbers are printed.

## 💡 Extended version – counter and sum

We can also add a counter and sum of positive numbers to display a summary at the end:

```python
count = 0
total = 0

while True:
    number = int(input("Enter a number: "))

    if number == 0:
        print("Finished – you entered 0.")
        break

    if number == 100:
        print("Special number 100 – stopping the program.")
        break

    if number < 0:
        print("Negative number – skipping.")
        continue

    count += 1
    total += number
    print("Number:", number)

print(f"\nYou entered {count} positive numbers. Their sum is {total}.")
```

### 🔍 Explanation:

* `count` tracks the number of positive numbers.
* `total` sums their values.
* `break` ends the program.
* `continue` skips unwanted numbers.

### 🧠 Takeaway

This is already a **practical program**!  
It combines:

* `while` loops,
* `break` and `continue`,
* user input,
* conditions and arithmetic operations.

These are core programming foundations, making your programs flexible and intelligent.

---

## 🎉 Lesson 13 Summary

* `break` – stops a loop at any moment.
* `continue` – skips one iteration and continues.
* Both statements give you more control over program flow.

Using them, you can write more precise and efficient solutions.

© 2025 PotegaIT – Python for Beginners
