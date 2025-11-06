## 🇵🇱 Wersja polska

# 🧠 Lekcja 14 – List Comprehensions

---

## 🎯 Cel lekcji

W tej lekcji poznasz **list comprehensions** — zwięzły sposób tworzenia nowych list w Pythonie.  
Dzięki nim możesz w jednej linijce kodu:

* generować nowe listy,
* modyfikować istniejące elementy,
* filtrować dane według określonego warunku.

To jedno z najbardziej eleganckich i efektywnych narzędzi w Pythonie, które znacząco poprawia czytelność kodu.

---

## 📝 1. Co to jest List Comprehension?

List comprehension to **krótka forma zapisu pętli for**, dzięki której możemy tworzyć listy w prostszy sposób.  
Zamiast kilku linii kodu z `for` i `append()`, możemy wszystko zapisać w jednej linijce.

```python
liczby = [1, 2, 3, 4, 5]
kwadraty = [x * x for x in liczby]
print(kwadraty)
```

### 🔍 Wyjaśnienie:

* `for x in liczby` – przechodzi po wszystkich elementach listy `liczby`.
* `x * x` – określa, co ma się znaleźć w nowej liście.
* Wynik: `[1, 4, 9, 16, 25]`.

💡 Zapis `[x * x for x in liczby]` można czytać jako:

> „Weź każdą liczbę x z listy liczby i zapisz jej kwadrat w nowej liście.”

---

## 🧩 2. List Comprehension z warunkiem (if)

List comprehensions można rozszerzyć o warunek, aby filtrować dane.
Dzięki temu w nowej liście znajdą się tylko te elementy, które spełniają określony warunek.

```python
liczby = [1, 2, 3, 4, 5, 6]
parzyste = [x for x in liczby if x % 2 == 0]
print(parzyste)
```

### 🔍 Wyjaśnienie:

* Warunek `if x % 2 == 0` przepuszcza tylko liczby parzyste.
* Wynik: `[2, 4, 6]`.

### 💡 Uwaga:

Warunek `if` w list comprehension jest opcjonalny, ale bardzo przydatny.
Pozwala filtrować dane bez użycia dodatkowych pętli lub instrukcji `if`.

---

## 🧮 3. List Comprehension z tekstem

List comprehensions działają nie tylko na liczbach — również na tekstach!
To świetny sposób na szybkie przetwarzanie list napisów.

```python
owoce = ["jabłko", "banan", "gruszka"]
duze_litery = [owoc.upper() for owoc in owoce]
print(duze_litery)
```

### 🔍 Wyjaśnienie:

* `owoc.upper()` zamienia każdy napis na wielkie litery.
* Wynik: `['JABŁKO', 'BANAN', 'GRUSZKA']`.

💬 Możesz również używać metod takich jak `lower()`, `replace()` czy `strip()` — wszystko w jednej linijce!

---

## 🧩 4. Mini projekt – filtrowanie liczb od użytkownika

> Stwórz program, który pobiera 5 liczb od użytkownika, a następnie wybiera tylko te większe niż 10.

```python
liczby = []

# Pobieranie danych od użytkownika
for i in range(5):
    liczba = int(input(f"Podaj liczbę nr {i+1}: "))
    liczby.append(liczba)

# Tworzenie listy z liczbami większymi niż 10
wieksze_niz_10 = [x for x in liczby if x > 10]

# Wyświetlenie wyniku
print("Liczby większe niż 10:")
print(wieksze_niz_10)
```

### 🔍 Wyjaśnienie:

* Pętla `for` zbiera dane od użytkownika.
* List comprehension filtruje liczby większe niż 10.
* Wynik to nowa lista z wybranymi wartościami.

💡 To doskonały przykład połączenia pętli, warunków, konwersji typów i list comprehension w jednym programie!

---

## 🧠 5. Wskazówki i dobre praktyki

* List comprehensions są świetne, gdy kod pozostaje czytelny.
Jeśli konstrukcja staje się zbyt długa lub złożona — lepiej użyć klasycznej pętli `for`.
* Możesz tworzyć również zagnieżdżone comprehensions, np. listy w listach — ale to temat na później.
* Zawsze zwracaj uwagę, aby Twoje comprehensions były zrozumiałe także dla innych programistów.

---

## 🎉 Podsumowanie lekcji 14

* Poznałeś pojęcie **list comprehension**.
* Nauczyłeś się tworzyć nowe listy w jednej linijce kodu.
* Wiesz, jak dodawać **warunki (if)**, by filtrować dane.
* Potrafisz przetwarzać **listy tekstów i liczb** w sposób prosty i czytelny.

List comprehensions to potężne narzędzie, które sprawia, że Twój kod jest krótszy, bardziej elegancki i profesjonalny.

© 2025 PotęgaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version

# 🧠 Lesson 14 – List Comprehensions

---

## 🎯 Lesson Goal

In this lesson, you will learn about **list comprehensions** — a concise way to create new lists in Python.  
With them, you can, in a single line of code:

* generate new lists,
* modify existing elements,
* filter data based on specific conditions.

This is one of the most elegant and efficient tools in Python, which significantly improves code readability.

---

## 📝 1. What is a List Comprehension?

A list comprehension is a **short form of a for loop** that allows us to create lists in a simpler way.  
Instead of writing multiple lines with `for` and `append()`, we can do it all in a single line.

```python
numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]
print(squares)
```

### 🔍 Explanation:

* `for x in numbers` — iterates through all elements in the list `numbers`.
* `x * x` — defines what will be included in the new list.
* Result: `[1, 4, 9, 16, 25]`.

💡 You can read `[x * x for x in numbers]` as:

> “Take each number x from the list numbers and store its square in a new list.”

---

🧩 2. List Comprehension with a Condition (`if`)

You can add a condition to a list comprehension to filter elements.
This way, only elements that meet a specific condition will appear in the new list.

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
```

### 🔍 Explanation:

* The condition `if x % 2 == 0` allows only even numbers.
* Result: `[2, 4, 6]`.

### 💡 Note:

The `if` condition in a list comprehension is optional but very useful.
It allows filtering data without additional loops or `if` statements.

---

## 🧮 3. List Comprehension with Text

List comprehensions work not only with numbers but also with strings!
This is a great way to quickly process lists of text.

```python
fruits = ["apple", "banana", "pear"]
uppercase_fruits = [fruit.upper() for fruit in fruits]
print(uppercase_fruits)
```

### 🔍 Explanation:

* `fruit.upper()` converts each string to uppercase.
* Result: `['APPLE', 'BANANA', 'PEAR']`.

💬 You can also use methods like `lower()`, `replace()`, or `strip()` — all in one line!

---


## 🧩 4. Mini Project – Filtering User Input

> Create a program that takes 5 numbers from the user and selects only those greater than 10.

```python
numbers = []

# Collecting data from the user
for i in range(5):
    number = int(input(f"Enter number #{i+1}: "))
    numbers.append(number)

# Creating a list with numbers greater than 10
greater_than_10 = [x for x in numbers if x > 10]

# Displaying the result
print("Numbers greater than 10:")
print(greater_than_10)
```

### 🔍 Explanation:

* The `for` loop collects input from the user.
* The list comprehension filters numbers greater than 10.
* The result is a new list containing only the selected values.

💡 This is an excellent example of combining loops, conditions, type conversion, and list comprehension in a single program!

---

## 🧠 5. Tips and Best Practices

* List comprehensions are great when code remains **readable**.
If a comprehension becomes too long or complex, use a classic `for` loop instead.

* You can also create **nested comprehensions**, e.g., lists within lists — but that is a more advanced topic.
* Always make sure your comprehensions are **understandable** for others who may read your code.

---

## 🎉 Lesson 14 Summary

* You learned about **list comprehensions**.
* You can now create new lists in a single line of code.
* You know how to add **conditions** (`if`) to filter data.
* You can process **lists of numbers and strings** in a simple and readable way.

List comprehensions are a powerful tool that makes your code shorter, cleaner, and more professional.

© 2025 PotegaIT – Python for Beginners
