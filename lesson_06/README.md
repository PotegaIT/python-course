## 🇵🇱 Wersja polska

# 🧮 Lekcja 6: Operatory arytmetyczne i logiczne

W tej lekcji poznasz coś, bez czego żaden język programowania się nie obejdzie – **operatory**.  
To dzięki nim program potrafi **liczyć, porównywać i podejmować decyzje**.  
Dowiesz się:
- jak w Pythonie działa dodawanie, odejmowanie, mnożenie czy dzielenie,  
- jak sprawdzać warunki (np. czy coś jest większe od czegoś),  
- oraz jak łączyć różne warunki za pomocą operatorów logicznych.

---

## 🔹 1. Operatory arytmetyczne

Operatory arytmetyczne służą do wykonywania **podstawowych działań matematycznych**.  
Działają na liczbach (`int` i `float`), a wynik również jest liczbą.

| Operator | Opis | Przykład | Wynik |
|-----------|------|-----------|-------|
| `+` | dodawanie | `10 + 3` | `13` |
| `-` | odejmowanie | `10 - 3` | `7` |
| `*` | mnożenie | `10 * 3` | `30` |
| `/` | dzielenie (zawsze float) | `10 / 3` | `3.333...` |
| `//` | dzielenie całkowite | `10 // 3` | `3` |
| `%` | reszta z dzielenia | `10 % 3` | `1` |
| `**` | potęgowanie | `10 ** 3` | `1000` |

### 📘 Przykład:
```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

## 2. Operatory porównań i logiczne

### 🔸 Operatory porównań

Pozwalają sprawdzić, czy dwie wartości są **równe, różne, większe lub mniejsze**.  
Zwracają wartość logiczną (`True` lub `False`).

| Operator | Opis | Przykład | Wynik |
|-----------|------|-----------|-------|
| `==` | równość | `5 == 5` | `True` |
| `!=` | nierówność | `5 != 3` | `True` |
| `>` | większe niż | `5 > 3` | `True` |
| `<` | mniejsze niż | `5 < 3` | `False` |
| `>=` | większe lub równe | `5 >= 5` | `True` |
| `<=` | mniejsze lub równe | `3 <= 5` | `True` |

### 📘 Przykład:
```python
x = 5
y = 10

print(x == y)      # False
print(x < y)       # True
print(x != y)      # True
```
### 🔸 Operatory logiczne

Pozwalają łączyć różne warunki w jedną całość.
Używamy ich np. przy sprawdzaniu, czy dwa warunki są prawdziwe jednocześnie.

| Operator | Opis                                       | Przykład             | Wynik   |
| -------- | ------------------------------------------ | -------------------- | ------- |
| `and`    | oba warunki muszą być prawdziwe            | `(x < 10 and y > 5)` | `True`  |
| `or`     | wystarczy, że jeden warunek jest prawdziwy | `(x > 10 or y > 5)`  | `True`  |
| `not`    | odwraca wartość logiczną                   | `not x > 3`          | `False` |

### 📘 Przykład:
```python
x = 5
y = 10

print(x < 10 and y > 5)   # True
print(x > 10 or y > 5)    # True
print(not x > 3)          # False
```

## 💡 3. Mini projekt – Prosty kalkulator i warunki

Zróbmy coś praktycznego — mały kalkulator, który wykona kilka działań i sprawdzi warunki logiczne.
```python
a = 8
b = 4

print(f"Suma: {a + b}")
print(f"Różnica: {a - b}")
print(f"Iloczyn: {a * b}")
print(f"Iloraz: {a / b}")

print(f"Czy a większe od b? {a > b}")
print(f"Czy a jest podzielne przez b? {a % b == 0}")
```
### 🔍 Co tu się dzieje?

* a - b → różnica,

* a * b → iloczyn,

* a / b → iloraz (wynik zawsze float),

* operator % sprawdza resztę z dzielenia. Jeśli reszta to 0, liczba jest podzielna przez drugą.

## 🧠 4. Operatory logiczne – w praktyce

Przyjrzyjmy się dokładniej operatorom and, or, not:
```python
a = 8
b = 4

print(a > 5 and b < 20)
print(a > 10 and b < 20)

print(a < 5 or b > 2)
print(a > 10 or b < 3)

print(not a > 5)
print(not b < 3)
```
#### Wyjaśnienie krok po kroku:

| Kod                 | Wynik   | Dlaczego                                    |
| ------------------- | ------- | ------------------------------------------- |
| `a > 5 and b < 20`  | `True`  | oba warunki prawdziwe                       |
| `a > 10 and b < 20` | `False` | pierwszy fałszywy                           |
| `a < 5 or b > 2`    | `True`  | drugi warunek prawdziwy                     |
| `a > 10 or b < 3`   | `False` | oba fałszywe                                |
| `not a > 5`         | `False` | `a > 5` to `True`, więc `not True → False`  |
| `not b < 3`         | `True`  | `b < 3` to `False`, więc `not False → True` |

## ✅ Podsumowanie

Dziś nauczyłeś się:

* korzystać z operatorów arytmetycznych,

* wykonywać podstawowe działania matematyczne,

* raz używać operatorów logicznych, które pozwalają łączyć warunki.

To fundament każdego programu — dzięki temu komputer potrafi analizować dane i podejmować decyzje.

© 2025 PotęgaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version

# 🧮 Lesson 6: Arithmetic and Logical Operators

In this lesson, you’ll learn something essential — **operators**.  
They allow a program to **calculate, compare, and make decisions**.  
You will discover:
- how addition, subtraction, multiplication, and division work in Python,  
- how to check conditions (e.g., if something is greater than something else),  
- and how to combine different conditions using logical operators.

---

## 🔹 1. Arithmetic Operators

Arithmetic operators are used to perform **basic mathematical operations**.  
They work on numbers (`int` and `float`), and the result is also a number.

| Operator | Description | Example | Result |
|-----------|-------------|----------|---------|
| `+` | addition | `10 + 3` | `13` |
| `-` | subtraction | `10 - 3` | `7` |
| `*` | multiplication | `10 * 3` | `30` |
| `/` | division (always returns float) | `10 / 3` | `3.333...` |
| `//` | integer (floor) division | `10 // 3` | `3` |
| `%` | modulus (remainder) | `10 % 3` | `1` |
| `**` | exponentiation | `10 ** 3` | `1000` |

### 📘 Example:
```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

## 2. Comparison and Logical Operators

### 🔸 Comparison Operators

They allow you to check whether two values are **equal, different, greater, or smaller**.  
They return a logical value (`True` or `False`).

| Operator | Description | Example | Result |
|-----------|--------------|----------|---------|
| `==` | equality | `5 == 5` | `True` |
| `!=` | inequality | `5 != 3` | `True` |
| `>` | greater than | `5 > 3` | `True` |
| `<` | less than | `5 < 3` | `False` |
| `>=` | greater than or equal to | `5 >= 5` | `True` |
| `<=` | less than or equal to | `3 <= 5` | `True` |

### 📘 Example:

```python
x = 5
y = 10

print(x == y)      # False
print(x < y)       # True
print(x != y)      # True
```
### 🔸 Logical Operators

Logical operators allow you to **combine multiple conditions** into one expression.  
They are often used to check whether two or more conditions are true at the same time.

| Operator | Description | Example | Result |
|-----------|-------------|----------|---------|
| `and` | both conditions must be true | `(x < 10 and y > 5)` | `True` |
| `or` | at least one condition must be true | `(x > 10 or y > 5)` | `True` |
| `not` | reverses the logical value | `not x > 3` | `False` |

### 📘 Example:
```python
x = 5
y = 10

print(x < 10 and y > 5)   # True
print(x > 10 or y > 5)    # True
print(not x > 3)          # False
```
## 💡 3. Mini Project – Simple Calculator and Conditions

Let’s do something practical — a small calculator that performs a few operations and checks logical conditions.
```python
a = 8
b = 4

print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
print(f"Quotient: {a / b}")

print(f"Is 'a' greater than 'b'? {a > b}")
print(f"Is 'a' divisible by 'b'? {a % b == 0}")
```
### 🔍 What’s happening here?

* `a - b` → difference  
* `a * b` → product  
* `a / b` → quotient (the result is always a float)  
* The `%` operator checks the **remainder of the division**.  
  If the remainder is `0`, it means the number is **divisible** by the other.

## 🧠 4. Logical operators — in practice

Let's take a closer look at the `and`, `or`, `not` operators:

```python
a = 8
b = 4

print(a > 5 and b < 20)
print(a > 10 and b < 20)

print(a < 5 or b > 2)
print(a > 10 or b < 3)

print(not a > 5)
print(not b < 3)
```
#### Step-by-step explanation:

| Code                | Result  | Why (explanation)                                 |
|---------------------|---------|---------------------------------------------------|
| `a > 5 and b < 20`  | `True`  | both conditions are true                          |
| `a > 10 and b < 20` | `False` | the first condition is false                      |
| `a < 5 or b > 2`    | `True`  | the second condition is true                      |
| `a > 10 or b < 3`   | `False` | both conditions are false                         |
| `not a > 5`         | `False` | `a > 5` is `True`, so `not True` → `False`        |
| `not b < 3`         | `True`  | `b < 3` is `False`, so `not False` → `True`       |

## ✅ Summary

Today you learned how to:

* use arithmetic operators,  
* perform basic mathematical operations,  
* and use logical operators, which allow you to combine conditions.

This is the foundation of every program — it enables the computer to **analyze data and make decisions**.

© 2025 PotegaIT – Python Course for Beginners
