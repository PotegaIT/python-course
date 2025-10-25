## 🇵🇱 Wersja polska

# Lekcja 5 – Zmienne i typy danych (string, int, float, bool)

W tej lekcji poznasz podstawy zmiennych w Pythonie oraz cztery najważniejsze typy danych: **string**, **int**, **float** i **bool**. Zmienna to nazwa, pod którą przechowujemy jakąś wartość – tekst, liczbę lub wartość logiczną. Dzięki zmiennym możemy przechowywać dane i wykorzystywać je w różnych miejscach programu.

## Co to są zmienne?

Zmienna to nazwa, pod którą przechowywana jest wartość. Nadajemy jej nazwę, używamy znaku **równości =** i przypisujemy wartość. Typ danych określa rodzaj wartości przechowywanej w zmiennej.

#### Przykłady:
```sh
name = "Greg" # string – tekst
age = 30 # int – liczba całkowita
height = 1.75 # float – liczba zmiennoprzecinkowa
is_student = True # bool – wartość logiczna
```

## Typy danych – string, int, float, bool

Każda zmienna w Pythonie ma typ danych, który mówi, jakiego rodzaju dane są w niej przechowywane i jak Python ma je traktować.
Poznanie typów danych jest podstawą nauki programowania.

**string (str)** – tekst, ciąg znaków w pojedynczych lub podwójnych cudzysłowach.  
Przykłady: `"Python"`, `"123"`, `'Hello world'`

**int** – liczby całkowite.  
Przykłady: `5`, `-100`, `2025`

**float** – liczby zmiennoprzecinkowe, z częścią dziesiętną (używamy kropki).  
Przykłady: `3.14`, `0.5`, `-2.0`

**bool** – wartości logiczne `True` lub `False`.  
Stosowane do sprawdzania warunków.

## Funkcja type()

Python posiada wbudowaną funkcję **type()**, która pozwala sprawdzić typ zmiennej. 

#### Przykład:
```sh
city = "Oslo"
year = 2025
temperature = 4.5
is_raining = False

print(type(city)) # <class 'str'>
print(type(year)) # <class 'int'>
print(type(temperature)) # <class 'float'>
print(type(is_raining)) # <class 'bool'>
```
Dzięki **type()** można sprawdzić, jakiego typu jest dana zmienna i unikać błędów, np. przy próbie dodania tekstu do liczby.

## Mini projekt

Przykładowy program tworzący zmienne różnych typów i wyświetlający je:

```sh
name = "Anna"
age = 25
height = 1.68
is_logged_in = True

print(f"Użytkownik {name}, wiek: {age}, wzrost: {height} m")
print(f"Czy zalogowany? {is_logged_in}")
```

## Podsumowanie

Dzisiaj nauczyłeś się, czym są zmienne i jak przechowywać w nich różne typy danych. 
Poznałeś cztery podstawowe typy w Pythonie: 

* string,
* int,
* float
* bool.

Dzięki nim możesz przechowywać tekst, liczby i informacje logiczne. 
Te umiejętności są fundamentem każdego programu i będą wykorzystywane w kolejnych lekcjach.
Podsumowanie

---

## 🇬🇧 English Version

# Lesson 5 – Variables and Data Types (string, int, float, bool)

In this lesson, you’ll learn the basics of variables in Python and the four most important data types: **string**, **int**, **float**, and **bool**.  
A variable is a name under which we store a certain value – text, a number, or a logical (boolean) value. Variables allow us to store data and use it in different parts of the program.

## What are variables?

A variable is a name that holds a value. We assign it a name, use the **equals sign (=)**, and give it a value. The data type defines what kind of value the variable stores.

#### Examples:
```python
name = "Greg"      # string – text
age = 30           # int – integer number
height = 1.75      # float – floating-point number
is_student = True  # bool – logical (boolean) value
```
## Data Types – string, int, float, bool

Every variable in Python has a data type that defines what kind of data it stores and how Python should interpret it.  
Understanding data types is a fundamental part of learning programming.

**string (str)** – text, a sequence of characters enclosed in single or double quotes.  
Examples: `"Python"`, `"123"`, `'Hello world'`

**int** – integer numbers.  
Examples: `5`, `-100`, `2025`

**float** – floating-point numbers with a decimal part (use a dot).  
Examples: `3.14`, `0.5`, `-2.0`

**bool** – logical values `True` or `False`.  
Used for condition checking.

## The type() Function

Python has a built-in **type()** function that allows you to check the data type of a variable.

#### Example:
```python
city = "Oslo"
year = 2025
temperature = 4.5
is_raining = False

print(type(city))        # <class 'str'>
print(type(year))        # <class 'int'>
print(type(temperature)) # <class 'float'>
print(type(is_raining))  # <class 'bool'>
```
Thanks to **type()**, you can check what type a variable is and avoid errors — for example, when trying to add text to a number.

## Mini Project

An example program that creates variables of different data types and displays them:

```python
name = "Anna"
age = 25
height = 1.68
is_logged_in = True

print(f"User {name}, age: {age}, height: {height} m")
print(f"Is logged in? {is_logged_in}")
```
## Summary

Today you learned what variables are and how to store different data types in them.  
You got to know the four basic types in Python:

* string  
* int  
* float  
* bool  

With these, you can store text, numbers, and logical information.  
These skills form the foundation of every program and will be used in the upcoming lessons.

