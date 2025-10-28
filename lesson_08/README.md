## 🇵🇱 Wersja polska

# 🧠 Lekcja 8 – Komentarze i dobre praktyki

---

## 🎯 Cel lekcji
W tej lekcji poznasz **komentarze** w Pythonie oraz **dobre praktyki programistyczne**, które sprawiają, że kod jest bardziej czytelny i zrozumiały.  
Dowiesz się, jak pisać kod nie tylko działający, ale także uporządkowany i przyjazny dla innych programistów.

---

## 🗣️ Wprowadzenie

> W tej części skupimy się na tym, co sprawia, że kod staje się czytelny i zrozumiały.  
> Komputer może wykonać wszystko, ale to ludzie piszą i czytają kod.  
> Dlatego ważne są komentarze oraz dobre praktyki programistyczne.

---

## 📝 1. Komentarze

Komentarze to fragmenty tekstu w kodzie, których Python **nie wykonuje**.  
Służą do opisywania działania programu w sposób zrozumiały dla człowieka.  
Dzięki nim łatwiej zrozumieć, co robi dany fragment kodu — zwłaszcza po czasie.

### 📌 Przykład

```python
# To jest komentarz liniowy
print("Cześć")  # komentarz obok kodu

"""
To jest dłuższy komentarz
na kilka linii.
"""
```

### 💡 Wskazówki:

* Komentarze zaczynamy od znaku `#`

* Dłuższe opisy można umieszczać w potrójnych cudzysłowach `(""" ... """)`

* Komentarze nie wpływają na działanie programu

---

## 💡 2. Dobre praktyki

Kod może działać, ale być napisany w sposób trudny do czytania.
Dlatego warto dbać o czytelność, nazewnictwo zmiennych i formatowanie.

Pisz kod tak, jakbyś pisał go dla przyszłego siebie lub innej osoby, która będzie go czytać za jakiś czas.

### 📌 Przykład

```python
# Zły styl
x=input("name?");print("Hi "+x)

# Dobry styl
name = input("Jak masz na imię? ")
print(f"Cześć, {name}!")
```

### 🧭 Zasady dobrego stylu:

* 🟢 Używaj czytelnych nazw zmiennych (np. user_name, user_age)

* 🟢 Oddzielaj sekcje kodu pustymi liniami

* 🟢 Nie pisz zbyt długich linii (maks. ok. 80 znaków)

* 🟢 Używaj komentarzy tam, gdzie kod może być nieoczywisty

* 🟢 Formatuj kod zgodnie z zasadami PEP 8 (np. spacje po przecinkach, wokół operatorów)

## 🧩 3. Mini zadanie

> Popraw poniższy kod tak, aby był czytelny, dobrze nazwany i skomentowany.

```python
x=input("wiek?");print("Masz "+x+" lat")
```

## 🧭 4. Podsumowanie

> To już kolejny krok w Twojej programistycznej przygodzie.
> Dziś nauczyłeś się, jak pisać kod, który nie tylko działa, ale też jest czytelny i zrozumiały.
> Poznałeś komentarze – czyli sposób, by tłumaczyć, co robi kod – oraz dobre praktyki, które sprawiają, że program wygląda profesjonalnie.
> Pamiętaj: dobry kod to taki, który łatwo się czyta, nie tylko taki, który działa.
> Dzięki temu inni (albo Ty sam za jakiś czas) będą mogli go szybko zrozumieć.

© 2025 PotęgaIT – Kurs Python dla początkujących

---

  
## 🇬🇧 English Version

# 🧠 Lesson 8 – Comments and Good Practices

---

## 🎯 Lesson Goal
In this lesson, you will learn about **comments** in Python and **good programming practices** that make your code more readable and understandable.  
You’ll discover how to write code that not only works, but is also clean, organized, and friendly to other programmers.

---

## 🗣️ Introduction

> In this part, we’ll focus on what makes code readable and clear.  
> The computer can execute anything, but it’s humans who write and read code.  
> That’s why comments and good programming practices are so important.

---

## 📝 1. Comments

Comments are pieces of text in your code that Python **does not execute**.  
They are used to describe what the program does in a way that is easy for humans to understand.  
Thanks to comments, it’s much easier to figure out what a piece of code does — especially after some time.

### 📌 Example

```python
# This is a single-line comment
print("Hello")  # comment next to code

"""
This is a longer comment
that spans multiple lines.
"""
```

### 💡 Tips:

* Comments start with the `#` symbol

* Longer descriptions can be written using triple quotes `(""" ... """)`

* Comments do not affect how the program works

## 💡 2. Good Practices

Your code might work, but still be written in a way that’s hard to read.
That’s why you should care about readability, variable naming, and formatting.

Write code as if you were writing it for your future self or someone else who will read it later.

### 📌 Example

```python
# Bad style
x=input("name?");print("Hi "+x)

# Good style
name = input("What is your name? ")
print(f"Hello, {name}!")
```

### 🧭 Good Style Guidelines:

* 🟢 Use clear variable names (e.g., user_name, user_age)

* 🟢 Separate sections of code with blank lines

* 🟢 Avoid overly long lines (max about 80 characters)

* 🟢 Add comments where the code might be unclear

* 🟢 Format your code according to PEP 8 (e.g., spaces after commas and around operators)

## 🧩 3. Mini Challenge

> Improve the code below so that it is readable, well-named, and properly commented.

## 🧭 4. Summary

> This is another step in your programming journey.
> Today, you learned how to write code that not only works but is also clear and easy to read.
> You discovered comments — a way to explain what your code does — and good practices that make your programs look professional.
> Remember: good code is not just code that works, but code that is easy to read.
> This way, others (or even you in the future) will be able to understand it quickly.

© 2025 PotegaIT – Python Course for Beginners

