## 🇵🇱 Wersja polska

# 🧾 Lekcja 30: Mini-aplikacja konsolowa z klasami – Menedżer budżetu domowego

---

## 🎬 Wprowadzenie

> Witaj w **ostatniej lekcji** naszego kursu **Pythona od podstaw!** 🎉

Dziś stworzymy coś wyjątkowego – **miniaplikację konsolową**, która pokaże, że naprawdę potrafisz już programować w Pythonie.

Zaprojektujemy **Menedżer budżetu domowego**, czyli prosty system do zarządzania wydatkami.  
Nasz program pozwoli:

- dodawać wydatki,  
- przeglądać listę wydatków,  
- usuwać je po numerze,  
- oraz obliczać **łączną sumę wydatków**.

To doskonałe podsumowanie wszystkiego, czego się nauczyłeś – wykorzystamy **klasy, metody, listy, pętle i obsługę błędów**. 

Gotowy? Zaczynajmy! 🚀

---

## 📋 1. Plan programu

Zanim napiszemy kod, spójrzmy, jak będzie działał nasz system:

Stworzymy **jedną główną klasę – `Budzet`**, która będzie:

- przechowywać listę wydatków,  
- umożliwiać ich dodawanie,  
- wyświetlać je w czytelnej formie,  
- usuwać po numerze,  
- oraz liczyć sumę wszystkich wydatków.

Każdy wydatek będzie zapisywany jako **słownik (`dict`)** z kluczami:

```python
{"opis": "np. Zakupy spożywcze", "kwota": 150.0}
```

Takie podejście jest proste i przejrzyste – idealne do pracy z danymi finansowymi.

---

## 🧱 2. Klasa Budzet

```python
class Budzet:
    def __init__(self):
        self.wydatki = []

    def dodaj_wydatek(self, opis, kwota):
        self.wydatki.append({"opis": opis, "kwota": kwota})

    def wyswietl_wydatki(self):
        if not self.wydatki:
            print("Brak wydatków.")
            return
        print("--- Lista wydatków ---")
        for idx, wydatek in enumerate(self.wydatki, 1):
            print(f"{idx}. {wydatek['opis']}: {wydatek['kwota']} zł")

    def usun_wydatek(self, numer):
        if 0 < numer <= len(self.wydatki):
            usuniety = self.wydatki.pop(numer - 1)
            print(f"Usunięto: {usuniety['opis']} za {usuniety['kwota']} zł")
        else:
            print("Nieprawidłowy numer wydatku.")

    def suma_wydatkow(self):
        suma = sum(w["kwota"] for w in self.wydatki)
        print(f"Łączna suma wydatków: {suma} zł")
```

### 🗣️ Omówienie

* `__init__` – konstruktor, który tworzy pustą listę `wydatki`.
* `dodaj_wydatek()` – dodaje nowy wydatek jako słownik z opisem i kwotą.
* `wyswietl_wydatki()` – wypisuje wszystkie wydatki w formie listy z numeracją.
  * Używamy funkcji `enumerate()`, by łatwo dodać numer przy każdym wpisie.
* `usun_wydatek()` – usuwa wydatek na podstawie numeru (użytkownik wybiera 1, 2, 3...).
* `suma_wydatkow()` – sumuje wszystkie kwoty i pokazuje łączną wartość wydatków.

To świetny przykład klasy, która łączy logikę i dane w jednym miejscu.   
Każda metoda ma swoją odpowiedzialność – czysto i przejrzyście.

---

## 🔁 3. Pętla główna – interakcja z użytkownikiem

```python
budzet = Budzet()

while True:
    print("\nWybierz opcję:")
    print("1. Dodaj wydatek")
    print("2. Pokaż wydatki")
    print("3. Usuń wydatek")
    print("4. Pokaż sumę wydatków")
    print("5. Zakończ")

    wybor = input("Twój wybór: ")

    if wybor == "1":
        opis = input("Podaj opis wydatku: ")
        try:
            kwota = float(input("Podaj kwotę: "))
            budzet.dodaj_wydatek(opis, kwota)
        except ValueError:
            print("Błąd: kwota musi być liczbą.")

    elif wybor == "2":
        budzet.wyswietl_wydatki()

    elif wybor == "3":
        try:
            numer = int(input("Podaj numer wydatku do usunięcia: "))
            budzet.usun_wydatek(numer)
        except ValueError:
            print("Błąd: musisz podać numer.")

    elif wybor == "4":
        budzet.suma_wydatkow()

    elif wybor == "5":
        print("Zamykam program. Do zobaczenia!")
        break

    else:
        print("Niepoprawny wybór. Spróbuj jeszcze raz.")
```

### 🗣️ Wyjaśnienie działania

* Tworzymy obiekt klasy `Budzet`.
* W nieskończonej pętli `while True` program pokazuje menu.
* Użytkownik wybiera akcję wpisując numer (1–5).
* Każda opcja uruchamia odpowiednią metodę klasy.
* Dzięki `try-except` obsługujemy błędy – np. gdy ktoś wpisze tekst zamiast liczby.
* Opcja „5” przerywa pętlę i kończy program.

To już w pełni funkcjonalna aplikacja konsolowa!   
Jest prosta, ale pokazuje wszystkie najważniejsze elementy programowania obiektowego w praktyce.

---

## 🧩 4. Przykładowe działanie programu

```markdown
Wybierz opcję:
1. Dodaj wydatek
2. Pokaż wydatki
3. Usuń wydatek
4. Pokaż sumę wydatków
5. Zakończ
Twój wybór: 1
Podaj opis wydatku: Zakupy spożywcze
Podaj kwotę: 120

Wybierz opcję:
1. Dodaj wydatek
2. Pokaż wydatki
...
Twój wybór: 2
--- Lista wydatków ---
1. Zakupy spożywcze: 120.0 zł
```

---

## 🏠 5. Zadanie domowe

Spróbuj rozbudować aplikację o nowe funkcje:

* 💾 **Zapis i odczyt wydatków z pliku tekstowego**
* 🏷️ **Dodanie kategorii** (np. „Jedzenie”, „Transport”, „Rachunki”)
* 📊 **Podsumowanie według kategorii**
* ✏️ **Możliwość edycji wydatku**

To świetne ćwiczenie, które pozwoli Ci dalej rozwijać umiejętności pracy z danymi, klasami i plikami.

---

## 🎓 6. Podsumowanie całego kursu

Gratulacje! 🥳
Ukończyłeś pełny kurs **Pythona dla początkujących** — od pierwszej linijki kodu aż po własne mini-aplikacje!

W trakcie kursu nauczyłeś się:

* pracować ze **zmiennymi, typami danych, pętlami i instrukcjami warunkowymi**,
* tworzyć **funkcje i moduły**,
* używać **plików i katalogów**,
* korzystać z **klas, obiektów i metod**,
* oraz pisać **praktyczne programy** krok po kroku.

Twoje umiejętności są już solidne – potrafisz samodzielnie analizować problem, zaplanować rozwiązanie i napisać działający kod. To właśnie fundament każdego dobrego programisty.

---

## 🚀 Co dalej?

To dopiero początek Twojej przygody z Pythonem!

W kolejnych kursach zajmiemy się m.in.:

* 🌐 tworzeniem aplikacji webowych w Flasku i Django,
* 🕹️ tworzeniem gier w Pygame,
* 📈 analizą danych z Pandas i Matplotlib,
* ⚙️ automatyzacją codziennych zadań w systemie,
* 🤖 oraz wykorzystaniem sztucznej inteligencji w Pythonie.

Dziękuję Ci za wspólną naukę i gratuluję wytrwałości! 💪   
Do zobaczenia w kolejnych kursach z serii **Python – krok dalej**.

Powodzenia, przyszły programisto! 👨‍💻🚀

© 2025 PotęgaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version

# 🧾 Lesson 30: Console Mini-App with Classes – Home Budget Manager

---

## 🎬 Introduction

> Welcome to the **final lesson** of our **Python from Scratch course!** 🎉

Today, we’ll create something special – a **console mini-application** that proves you can really program in Python now.

We’ll design a **Home Budget Manager**, a simple system for managing expenses.  
Our program will allow you to:

- add expenses,  
- view the list of expenses,  
- delete them by number,  
- and calculate the **total sum of expenses**.

This is a perfect summary of everything you’ve learned – we’ll use **classes, methods, lists, loops, and error handling**.

Ready? Let’s go! 🚀

---

## 📋 1. Program Plan

Before we start coding, let’s see how our system will work:

We’ll create **one main class – `Budget`**, which will:

- store a list of expenses,  
- allow adding new ones,  
- display them in a readable format,  
- delete them by number,  
- and calculate the total of all expenses.

Each expense will be stored as a **dictionary (`dict`)** with keys:

```python
{"description": "e.g. Groceries", "amount": 150.0}
```

This approach is simple and clear – perfect for working with financial data.

## 🧱 2. Budget Class

```python
class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount):
        self.expenses.append({"description": description, "amount": amount})

    def show_expenses(self):
        if not self.expenses:
            print("No expenses.")
            return
        print("--- Expense List ---")
        for idx, expense in enumerate(self.expenses, 1):
            print(f"{idx}. {expense['description']}: {expense['amount']} PLN")

    def remove_expense(self, number):
        if 0 < number <= len(self.expenses):
            removed = self.expenses.pop(number - 1)
            print(f"Removed: {removed['description']} for {removed['amount']} PLN")
        else:
            print("Invalid expense number.")

    def total_expenses(self):
        total = sum(e["amount"] for e in self.expenses)
        print(f"Total expenses: {total} PLN")
```

### 🗣️ Explanation

* `__init__` – constructor that creates an empty `expenses` list.
* `add_expense()` – adds a new expense as a dictionary with a description and amount.
* `show_expenses()` – prints all expenses in a numbered list.
  * We use the `enumerate()` function to easily add numbers to each entry.
* `remove_expense()` – removes an expense based on its number (user chooses 1, 2, 3...).
* `total_expenses()` – sums all amounts and displays the total value of expenses.

This is a great example of a class that combines logic and data in one place.   
Each method has a clear responsibility – clean and organized.

---

## 🔁 3. Main Loop – User Interaction

```python
budget = Budget()

while True:
    print("\nChoose an option:")
    print("1. Add expense")
    print("2. Show expenses")
    print("3. Remove expense")
    print("4. Show total expenses")
    print("5. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        description = input("Enter expense description: ")
        try:
            amount = float(input("Enter amount: "))
            budget.add_expense(description, amount)
        except ValueError:
            print("Error: amount must be a number.")

    elif choice == "2":
        budget.show_expenses()

    elif choice == "3":
        try:
            number = int(input("Enter the number of the expense to remove: "))
            budget.remove_expense(number)
        except ValueError:
            print("Error: you must enter a number.")

    elif choice == "4":
        budget.total_expenses()

    elif choice == "5":
        print("Closing the program. See you next time!")
        break

    else:
        print("Invalid choice. Please try again.")
```

### 🗣️ How It Works

* We create an object of the `Budget` class.
* In an infinite `while True` loop, the program shows a menu.
* The user selects an action by entering a number (1–5).
* Each option runs the corresponding class method.
* With `try-except`, we handle errors – for example, when someone enters text instead of a number.
* Option “5” breaks the loop and ends the program.

This is already a fully functional console application!   
It’s simple but demonstrates all key elements of object-oriented programming in practice.

---

## 🧩 4. Example Program Output

```markdown
Choose an option:
1. Add expense
2. Show expenses
3. Remove expense
4. Show total expenses
5. Exit
Your choice: 1
Enter expense description: Groceries
Enter amount: 120

Choose an option:
1. Add expense
2. Show expenses
...
Your choice: 2
--- Expense List ---
1. Groceries: 120.0 PLN
```

---

## 🏠 5. Homework

Try expanding the application with new features:

* 💾 **Save and load expenses from a text file**
* 🏷️ **Add categories** (e.g., “Food”, “Transport”, “Bills”)
* 📊 **Summary by category**
* ✏️ **Edit existing expenses**

This is a great exercise to help you develop your skills in working with data, classes, and files.

---

## 🎓 6. Course Summary

Congratulations! 🥳
You’ve completed the full **Python for Beginners course** — from your first line of code to creating your own mini-applications!

Throughout the course, you learned how to:

* work with **variables, data types, loops, and conditionals**,
* create **functions and modules**,
* use **files and directories**,
* work with **classes, objects, and methods**,
* and write **practical programs** step by step.

Your skills are now solid – you can analyze problems, plan solutions, and write working code.
That’s the foundation of every good programmer.

---

## 🚀 What’s Next?

This is just the beginning of your Python journey!

In upcoming courses, we’ll cover:

* 🌐 building web applications with Flask and Django,
* 🕹️ creating games with Pygame,
* 📈 data analysis with Pandas and Matplotlib,
* ⚙️ automating everyday system tasks,
* 🤖 and using artificial intelligence with Python.

Thank you for learning with me and congratulations on your persistence! 💪   
See you in the next courses in the **Python – Next Step** series.

Good luck, future programmer! 👨‍💻🚀

© 2025 PotegaIT – Python Course for Beginners
