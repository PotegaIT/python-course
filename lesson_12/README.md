## 🇵🇱 Wersja polska

# 🧠 Lekcja 12 – if, elif, else: logika decyzji

---

## 🎯 Cel lekcji
W tej lekcji nauczysz się, jak podejmować decyzje w programie.  
W Pythonie służą do tego **instrukcje warunkowe**: `if`, `elif`, `else`.  
Dzięki nim Twój program może działać inaczej w zależności od sytuacji – np. reagować na różne wartości danych lub wybierać odpowiednią ścieżkę działania.

To jeden z kluczowych elementów każdego języka programowania – **logika decyzji**.

---

## 📝 1. Instrukcja `if` – podstawowy warunek

Instrukcja `if` pozwala sprawdzić, **czy warunek jest prawdziwy**.  
Jeśli tak – wykona kod w swoim bloku.  
Jeśli nie – po prostu przejdzie dalej.

```python
temperatura = 30

if temperatura > 25:
    print("Jest gorąco!")
```

#### 🗣️ Co warto zapamiętać:

* **if** oznacza „jeśli”.
* Sprawdzamy warunek (np. `temperatura > 25`).
* Jeśli warunek jest prawdziwy, kod się wykona.
* Jeśli nie – nic się nie dzieje.

To warunek jednokierunkowy – reaguje tylko, gdy coś jest prawdą.

---

## 📝 2. Instrukcja `if...else` – dwie ścieżki

Czasem chcemy, by program zawsze wykonał coś –
jedno, jeśli warunek jest prawdziwy, lub inne, jeśli nie.

Wtedy używamy `else`, czyli „w przeciwnym razie”.

```python
temperatura = 15

if temperatura > 20:
    print("Ciepło")
else:
    print("Zimno")
```

#### 🗣️ Co warto zapamiętać:

* Jeśli warunek (`temperatura > 20`) jest fałszywy – Python wykona blok `else`.

Program zawsze wybierze jedną z dwóch dróg.

---

## 📝 3. Instrukcja `elif` – więcej możliwości

Co, jeśli mamy więcej niż dwa przypadki?

Używamy `elif` – czyli _else if_ – aby dodać kolejne warunki.

```python
temperatura = 10

if temperatura > 25:
    print("Gorąco")
elif temperatura > 15:
    print("W sam raz")
else:
    print("Zimno")
```

#### 🗣️ Co warto zapamiętać:

* Python sprawdza warunki po kolei.
* Jeśli pierwszy (`> 25`) nie jest spełniony, sprawdza kolejny (`> 15`).
* Gdy żaden nie jest prawdziwy – wykona się blok `else`.
* Można mieć wiele `elif`, ale tylko jedno if na początku i maksymalnie jedno else na końcu.

### 💡 Wskazówka praktyczna

Bloki `if`, `elif`, `else` muszą mieć wcięcia – Python rozpoznaje, które linie należą do którego warunku.
Zwykle używamy **4 spacji** lub jednego **tabulatora**.

---

## ⚙️ 4. Operatory porównań

Do tworzenia warunków używamy operatorów porównań:

| Operator | Znaczenie          | Przykład |
| -------- | ------------------ | -------- |
| `==`     | równe              | `a == b` |
| `!=`     | różne              | `a != b` |
| `>`      | większe niż        | `a > b`  |
| `<`      | mniejsze niż       | `a < b`  |
| `>=`     | większe lub równe  | `a >= b` |
| `<=`     | mniejsze lub równe | `a <= b` |

---

## 🧩 5. Mini projekt – decyzja na podstawie wieku

> Program, który zapyta użytkownika o wiek i powie, czy może prowadzić samochód.

```python
wiek = int(input("Ile masz lat? "))

if wiek >= 18:
    print("Możesz prowadzić samochód!")
    if wiek >= 70:
        print("Pamiętaj o badaniach lekarskich – mogą być wymagane.")
elif wiek >= 16:
    print("Jeszcze trochę poczekaj. Ale możesz już zacząć uczyć się teorii!")
else:
    print("Na razie jesteś za młody, ale wszystko przed Tobą!")
```

#### 🗣️ Wyjaśnienie:

* Używamy `if`, `elif` i `else` – każda ścieżka daje inny komunikat.
* W środku if zastosowano zagnieżdżony if (`if wiek >= 70`).
* Dzięki temu program reaguje różnie dla różnych grup wiekowych – jak prawdziwa aplikacja!

---

## 🎉 Podsumowanie lekcji 12

* Nauczyłeś się podejmować decyzje w programie.
* Poznałeś instrukcje: `if`, `elif`, `else`.
* Wiesz, jak porównywać wartości i kontrolować przepływ programu.
* Twoje programy potrafią teraz reagować na sytuację – czyli stały się naprawdę inteligentne!

© 2025 PotęgaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version

# 🧠 Lesson 12 – if, elif, else: decision logic

---

## 🎯 Lesson goal

In this lesson, you’ll learn how to make decisions in your program.
In Python, this is done using **conditional statements**: `if`, `elif`, and `else`.
They let your program behave differently depending on the situation — for example, react to different data values or choose the right course of action.

This is one of the key elements of any programming language — **decision logic**.

---

## 📝 1. The `if` statement – the basic condition

The `if` statement checks whether a condition is true.
If it is — the code inside its block will execute.
If not — Python will simply move on.

```python
temperature = 30

if temperature > 25:
    print("It's hot!")
```

#### 🗣️ Remember:

* if means “if” (as in “if something is true”).
* You check a condition (e.g., `temperature > 25`).
* If the condition is true, the code runs.
* If not – nothing happens.

It’s a one-way condition – it reacts only when something is true.

---

## 📝 2. The `if...else` statement – two paths

Sometimes you want your program to always do something –
one thing if the condition is true, another if it’s false.

That’s what `else` (“otherwise”) is for.

```python
temperature = 15

if temperature > 20:
    print("Warm")
else:
    print("Cold")
```

#### 🗣️ Remember:

* If the condition (`temperature > 20`) is false – Python runs the `else` block.

The program will always take one of the two paths.

---

## 📝 3. The `elif` statement – more options

What if you have more than two cases?

Use `elif` — short for _else if_ — to add more conditions.

```python
temperature = 10

if temperature > 25:
    print("Hot")
elif temperature > 15:
    print("Just right")
else:
    print("Cold")
```

#### 🗣️ Remember:

* Python checks the conditions in order.
* If the first (`> 25`) isn’t true, it checks the next (`> 15`).
* If none are true, the `else` block executes.
* You can have multiple `elif` blocks, but only one `if` at the start and one `else` at the end.

### 💡 Practical tip

The blocks inside `if`, `elif`, and `else` must be indented –
Python uses indentation to know which lines belong to which condition.
Use **4 spaces** or one **tab** per indentation level.

---

## ⚙️ 4. Comparison operators

To create conditions, we use comparison operators:

| Operator | Meaning             | Example  |
| -------- | ------------------- | -------- |
| `==`     | equal to            | `a == b` |
| `!=`     | not equal to        | `a != b` |
| `>`      | greater than        | `a > b`  |
| `<`      | less than           | `a < b`  |
| `>=`     | greater or equal to | `a >= b` |
| `<=`     | less or equal to    | `a <= b` |

---

## 🧩 5. Mini project – decision based on age

> A program that asks the user for their age and tells them if they can drive a car.

```python
age = int(input("How old are you? "))

if age >= 18:
    print("You can drive a car!")
    if age >= 70:
        print("Remember to get regular medical checkups – they might be required.")
elif age >= 16:
    print("Almost there! You can start learning the theory.")
else:
    print("You're too young for now, but your time will come!")
```

#### 🗣️ Explanation:

* We use `if`, `elif`, and `else` – each path gives a different message.
* Inside the first `if`, we use a nested `if` (`if age >= 70`).
* This way, the program reacts differently for different age groups – just like a real-world app!

---

## 🎉 Summary – Lesson 12

* You learned how to make decisions in your program.
* You now understand how to use `if`, `elif`, and `else`.
* You know how to compare values and control program flow.
* Your programs can now react to situations – they’ve become truly smart!

© 2025 PotegaIT – Python Course for Beginners
