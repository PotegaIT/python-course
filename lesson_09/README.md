## 🇵🇱 Wersja polska

# 🧠 Lekcja 9 – Listy i operacje na listach

---

## 🎯 Cel lekcji
W tej lekcji poznasz jedno z najważniejszych narzędzi w Pythonie – **listy**.  
Listy to zbiory danych, które możemy modyfikować, przeglądać i analizować.  
Nauczysz się tworzyć listy, dodawać i usuwać elementy, a także korzystać z przydatnych funkcji.

---

## 🗣️ Wprowadzenie

> Listy w Pythonie to uporządkowane zbiory elementów, które można łatwo modyfikować.  
> Pozwalają przechowywać liczby, teksty, a nawet inne listy.  
> Dzięki nim programy stają się bardziej dynamiczne i elastyczne.

---

## 📝 1. Co to jest lista?

Lista to uporządkowany zbiór elementów. Możesz do niej wrzucić liczby, teksty, a nawet inne listy.  
W Pythonie listy zapisujemy w nawiasach kwadratowych `[]`.

### 📌 Przykład

```python
owoce = ["jabłko", "banan", "gruszka"]
print(owoce)

# Możemy też mieć pustą listę
pusta_lista = []

# Możemy też mieć pustą listę
pusta_lista = []
```

## 💡 2. Dodawanie i usuwanie elementów

Lista w Pythonie jest dynamiczna – możemy ją modyfikować w trakcie działania programu.

* Dodawać nowe elementy → `append()`
* Usuwać elementy → `remove()` lub `pop()`
* Zmieniać kolejność elementów

### 📌 Przykłady

```python
# Dodawanie elementu na końcu listy
owoce = ["jabłko", "banan", "gruszka"]
owoce.append("śliwka")
print(owoce)  # ['jabłko', 'banan', 'gruszka', 'śliwka']

# Usuwanie elementu po nazwie
owoce.remove("banan")
print(owoce)  # ['jabłko', 'gruszka', 'śliwka']

# Usuwanie ostatniego elementu i zapisanie go do zmiennej
ostatni = owoce.pop()
print("Usunięto:", ostatni)
print(owoce)  # ['jabłko', 'gruszka']

# Usuwanie elementu po indeksie
pierwszy = owoce.pop(0)
print("Usunięto pierwszy element:", pierwszy)
print(owoce)  # ['gruszka']
```

## 🧩 3. Dostęp do elementów listy

Każdy element w liście ma swój numer (indeks) – w Pythonie indeksowanie zaczyna się od zera.

### 📌 Przykłady

```python
owoce = ["jabłko", "banan", "gruszka"]

# Pobranie elementu po indeksie
pierwszy = owoce[0]
print("Pierwszy owoc to:", pierwszy)

# Zmiana wartości elementu
owoce[1] = "kiwi"
print(owoce)  # ['jabłko', 'kiwi', 'gruszka']

# Indeksy ujemne – liczenie od końca
ostatni = owoce[-1]
print("Ostatni owoc to:", ostatni)

# Błąd przy zbyt dużym indeksie
# print(owoce[10])  # IndexError
```

## 🧭 4. Długość listy

Aby sprawdzić, ile elementów zawiera lista, używamy funkcji `len()`

```python
print("Liczba owoców:", len(owoce))
```

## 🧩 5. Mini projekt

> Stwórzmy program, który pyta użytkownika o 3 ulubione potrawy i zapisuje je do listy.
> Potem wypiszemy listę i jej długość.

```python
potrawy = []

potrawy.append(input("Podaj 1. potrawę: "))
potrawy.append(input("Podaj 2. potrawę: "))
potrawy.append(input("Podaj 3. potrawę: "))

print("Twoje ulubione potrawy:", potrawy)
print("Liczba potraw:", len(potrawy))
```

## 🎉 Podsumowanie

Świetna robota! W tej lekcji poznaliśmy bardzo ważną strukturę danych w Pythonie – listy.

Nauczyłeś się:

* Czym jest lista i jak ją tworzyć, także pustą
* Jak dodawać elementy (`append()`)
* Jak usuwać elementy (`remove()` i `pop()`)
* Jak odwoływać się do elementów po indeksach dodatnich i ujemnych
* Co się dzieje przy błędzie `IndexError`
* Jak zmieniać wartości elementów listy
* Jak sprawdzać długość listy (`len()`)

Dodatkowo stworzyliśmy **mini-projekt** z ulubionymi potrawami, łączący wszystkie poznane umiejętności.
Listy są fundamentem wielu programów – od prostych po bardzo zaawansowane, dlatego warto je dobrze poznać.

© 2025 PotęgaIT – Kurs Python dla początkujących

---

# 🧠 Lesson 9 – Lists and List Operations

---

## 🎯 Lesson Goal
In this lesson, you will learn one of the most important tools in Python – **lists**.  
Lists are collections of data that we can modify, iterate over, and analyze.  
You will learn how to create lists, add and remove elements, and use useful functions.

---

## 🗣️ Introduction

> Lists in Python are ordered collections of elements that can be easily modified.  
> They can store numbers, text, and even other lists.  
> Thanks to lists, programs become more dynamic and flexible.

---

## 📝 1. What is a list?

A list is an **ordered collection of elements**. You can store numbers, text, and even other lists in it.  
In Python, lists are written using square brackets `[]`.

### 📌 Example

```python
fruits = ["apple", "banana", "pear"]
print(fruits)

# We can also have an empty list
empty_list = []
```

## 💡 2. Adding and Removing Elements

Lists in Python are dynamic – we can modify them while the program is running.

* Add new elements → `append()`
* Remove elements → `remove()` or `pop()`
* Change the order of elements

### 📌 Examples

```python
# Adding an element to the end of the list
fruits = ["apple", "banana", "pear"]
fruits.append("plum")
print(fruits)  # ['apple', 'banana', 'pear', 'plum']

# Removing an element by value
fruits.remove("banana")
print(fruits)  # ['apple', 'pear', 'plum']

# Removing the last element and storing it in a variable
last = fruits.pop()
print("Removed:", last)
print(fruits)  # ['apple', 'pear']

# Removing an element by index
first = fruits.pop(0)
print("Removed first element:", first)
print(fruits)  # ['pear']
```

## 🧩 3. Accessing List Elements

Each element in a list has a number (index) – in Python, indexing starts at zero.

### 📌 Examples

```python
fruits = ["apple", "banana", "pear"]

# Access element by index
first = fruits[0]
print("First fruit is:", first)

# Changing the value of an element
fruits[1] = "kiwi"
print(fruits)  # ['apple', 'kiwi', 'pear']

# Negative indices – counting from the end
last = fruits[-1]
print("Last fruit is:", last)

# Error when using an index that is too large
# print(fruits[10])  # IndexError
```

## 🧭 4. Length of a List

To check how many elements are in a list, use the `len()` function.

```python
print("Number of fruits:", len(fruits))
```

## 🧩 5. Mini Project

> Let's create a program that asks the user for 3 favorite dishes and stores them in a list.
> Then we will print the list and its length.

```python
dishes = []

dishes.append(input("Enter dish 1: "))
dishes.append(input("Enter dish 2: "))
dishes.append(input("Enter dish 3: "))

print("Your favorite dishes:", dishes)
print("Number of dishes:", len(dishes))
```

## 🎉 Summary

Great job! In this lesson, we learned a very important Python data structure – lists.

You learned:

* What a list is and how to create it, including empty lists
* How to add elements (append())
* How to remove elements (remove() and pop())
* How to access elements using positive and negative indices
* What happens when an IndexError occurs
* How to change the values of elements
* How to check the length of a list (len())

We also created a mini-project with favorite dishes, combining all the skills we learned.
Lists are a foundation for many programs – from simple to advanced – so it’s important to know them well.

© 2025 PotęgaIT – Python Course for Beginners
