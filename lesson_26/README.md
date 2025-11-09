## 🇵🇱 Wersja polska

# 📝 Lekcja 26 — Prosty program do zarządzania zadaniami (TODO CLI)

---

## 🎯 Cel lekcji

W tej lekcji zbudujemy kolejny praktyczny projekt — **tekstowy menedżer zadań (TODO listę)** działający w terminalu.  
Będzie to mały, ale bardzo użyteczny program, który pozwoli nam połączyć wiele umiejętności poznanych wcześniej.

Nauczysz się:

* organizować kod w **funkcje**,  
* przechowywać dane w **listach**,  
* tworzyć **interaktywne menu** w terminalu,  
* **zapisywać** i **odczytywać** dane z pliku,  
* oraz kontrolować działanie programu przy pomocy **pętli głównej**.

To praktyczne ćwiczenie, które pokazuje, jak z podstaw Pythona można stworzyć prostą, codzienną aplikację.

---

## 1. Co chcemy osiągnąć?

Zbudujemy prosty program do zarządzania zadaniami — tzw. **TODO listę**.

Nasz program pozwoli użytkownikowi:

* ➕ dodać nowe zadanie,  
* 📋 wyświetlić wszystkie zadania,  
* ❌ usunąć wybrane zadanie,  
* 💾 zapisać listę do pliku, aby nie zniknęła po zamknięciu programu.

Przykładowe menu programu:

--- MENU ---
1. Pokaż zadania
2. Dodaj zadanie
3. Usuń zadanie
4. Zapisz i zakończ

---

## 2. Struktura danych – jak przechowywać zadania

Zadania będziemy przechowywać w **liście** Pythona.  
Każde zadanie będzie po prostu tekstem (napisem typu `str`).

Przykład:

```python
zadania = ["Posprzątać pokój", "Napisać projekt", "Zrobić zakupy"]
```

Taka lista jest łatwa do modyfikacji, iteracji oraz późniejszego zapisu do pliku.

## 3. Funkcja dodająca zadanie

Zacznijmy od funkcji, która doda nowe zadanie do listy:

```python
def dodaj_zadanie(zadania, nowe_zadanie):
    zadania.append(nowe_zadanie)
```

### 🗣️ Wyjaśnienie:

* `append()` dodaje element na końcu listy.
* Funkcja nie zwraca wartości — modyfikuje listę bezpośrednio.

---

## 4. Funkcja wyświetlająca zadania

Teraz napiszemy funkcję, która ładnie wypisze wszystkie zadania użytkownika:

```python
def pokaz_zadania(zadania):
    if not zadania:
        print("Brak zadań na liście.")
    else:
        print("Lista zadań:")
        for idx, zadanie in enumerate(zadania, start=1):
            print(f"{idx}. {zadanie}")
```

### 🗣️ Wyjaśnienie:

* `enumerate()` pozwala numerować elementy listy.
* Jeśli lista jest pusta, informujemy użytkownika odpowiednim komunikatem.

---

## 5. Funkcja usuwająca zadanie

Kolejnym krokiem jest możliwość usunięcia zadania na podstawie jego numeru.

```python
def usun_zadanie(zadania, numer):
    if 0 < numer <= len(zadania):
        zadania.pop(numer - 1)
        print("Zadanie zostało usunięte.")
    else:
        print("Niepoprawny numer zadania.")
```

### 🗣️ Wyjaśnienie:

* `pop()` usuwa element z listy po jego indeksie.
* Od numeru użytkownika odejmujemy 1, ponieważ listy w Pythonie zaczynają się od indeksu `0`.
* Dodatkowo sprawdzamy poprawność numeru, by uniknąć błędu.

---

## 6. Zapis i odczyt z pliku

Chcemy, aby lista zadań była zapamiętana po zamknięciu programu.
W tym celu zapiszemy ją do pliku tekstowego.

### Funkcja zapisu:

```python
def zapisz_zadania(zadania, sciezka):
    with open(sciezka, 'w', encoding='utf-8') as plik:
        for zadanie in zadania:
            plik.write(zadanie + '\n')
```

### Funkcja odczytu:

```python
def wczytaj_zadania(sciezka):
    try:
        with open(sciezka, 'r', encoding='utf-8') as plik:
            return [linia.strip() for linia in plik]
    except FileNotFoundError:
        return []
```

### 🗣️ Wyjaśnienie:

* Każde zadanie zapisujemy w osobnej linii.
* `strip()` usuwa znak nowej linii `\n`.
* Jeśli plik nie istnieje, funkcja zwraca pustą listę, zamiast generować błąd.

---

## 7. Główna pętla programu

Teraz połączymy wszystkie funkcje w jeden działający program.

```python
def main():
    sciezka = "zadania.txt"
    zadania = wczytaj_zadania(sciezka)

    while True:
        print("\n--- MENU ---")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Usuń zadanie")
        print("4. Zapisz i zakończ")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            pokaz_zadania(zadania)
        elif wybor == "2":
            nowe = input("Podaj treść nowego zadania: ")
            dodaj_zadanie(zadania, nowe)
        elif wybor == "3":
            pokaz_zadania(zadania)
            try:
                numer = int(input("Podaj numer zadania do usunięcia: "))
                usun_zadanie(zadania, numer)
            except ValueError:
                print("Musisz podać numer.")
        elif wybor == "4":
            zapisz_zadania(zadania, sciezka)
            print("Zadania zapisane. Do zobaczenia!")
            break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
```

A na końcu:

```python
if __name__ == "__main__":
    main()
```

---

## 8. Co oznacza `__name__ == "__main__"`?

Każdy plik `.py` ma wbudowaną zmienną `__name__`.

* Jeśli plik jest uruchamiany bezpośrednio (np. `python todo.py)`, → wtedy `__name__` przyjmuje wartość `"__main__"`.
* Jeśli plik jest importowany jako moduł (np. `import todo`), → wtedy `__name__` ma wartość `"todo"` (czyli nazwę pliku bez `.py`).

Dlatego stosujemy:

```python
if __name__ == "__main__":
    main()
```

### 🧠 Dlaczego to robimy?

Dzięki temu:

* Funkcja `main()` uruchamia się tylko wtedy, gdy plik jest wykonywany bezpośrednio.
* Możemy zaimportować ten plik jako moduł w innym projekcie — bez ryzyka, że program wystartuje automatycznie.

---

## 9. Struktura projektu

```arduino
todo_cli/
├── todo.py           # główny skrypt programu (funkcje + pętla główna)
├── zadania.txt       # plik z zapisanymi zadaniami
└── README.md         # dokumentacja (ten plik)
```

---

## 10. Przykładowe działanie programu

```markdown
--- MENU ---
1. Pokaż zadania
2. Dodaj zadanie
3. Usuń zadanie
4. Zapisz i zakończ

Wybierz opcję: 2
Podaj treść nowego zadania: Nagrać lekcję 26
Zadanie dodane!

--- MENU ---
1. Pokaż zadania
2. Dodaj zadanie
3. Usuń zadanie
4. Zapisz i zakończ
```

---

## 11. Testowanie i obsługa błędów

### ✅ Jak testować:

* Dodaj kilka zadań, a następnie wyświetl listę.
* Spróbuj usunąć zadanie, podając poprawny i błędny numer.
* Zakończ program, uruchom go ponownie i sprawdź, czy lista została zapisana.

### ⚠️ Typowe błędy:

* Niepodanie liczby przy usuwaniu (`ValueError`).
* Próba usunięcia zadania o nieistniejącym numerze.
* Brak pliku `zadania.txt` przy pierwszym uruchomieniu (rozwiązane przez `try/except`).

---

## 12. Pomysły na rozwój projektu

Spróbuj rozszerzyć swój program o dodatkowe możliwości:

1. **✏️ Edycja zadań** — możliwość zmiany treści zadania.
2. **✅ Oznaczanie jako** wykonane — dodanie statusu zadania.
3. **🔍 Filtrowanie** — wyświetlanie tylko zadań zakończonych lub aktywnych.
4. **📅 Dodanie daty** — przypisanie terminu wykonania.
5. **🔄 Sortowanie** — np. alfabetycznie lub według terminu.
6. **💻 Interfejs CLI** — obsługa argumentów wiersza poleceń (moduł `argparse`).
7. **💾 Format JSON** — zapisywanie danych w pliku `.json` zamiast `.txt`.

Każde z tych rozszerzeń to świetne ćwiczenie, które rozwija umiejętność tworzenia realnych aplikacji w Pythonie.

---

## ✅ Podsumowanie

Stworzyłeś działający program **TODO CLI** — prosty, ale praktyczny menedżer zadań.

Dzięki tej lekcji:

* nauczyłeś się organizować kod przy pomocy **funkcji**,
* poznałeś zasady **zachowywania danych** w plikach,
* przećwiczyłeś **obsługę błędów** użytkownika,
* i stworzyłeś **tekstowy interfejs użytkownika**, działający jak mała aplikacja.

To już pełnoprawny projekt, który możesz rozwijać dalej!
Dodaj nowe funkcje, eksperymentuj z formatami danych i baw się w tworzenie własnych narzędzi programistycznych.

© 2025 PotęgaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version

# 📝 Lesson 26 — Simple Task Manager (TODO CLI)

---

## 🎯 Lesson Goal

In this lesson, we’ll build another practical project — a **text-based task manager (TODO list)** that runs in the terminal.  
It will be a small but very useful program that combines many skills you’ve already learned.

You will learn how to:

* organize your code using **functions**,  
* store data in **lists**,  
* create an **interactive menu** in the terminal,  
* **save** and **load** data from a file,  
* and control the flow of your program using a **main loop**.

This is a hands-on exercise showing how Python basics can be used to create a simple, everyday application.

---

## 1. What we want to achieve

We’ll build a simple program for managing tasks — a **TODO list**.

Our program will allow the user to:

* ➕ add a new task,  
* 📋 display all tasks,  
* ❌ delete a selected task,  
* 💾 save the list to a file so it’s not lost after exiting.

Example program menu:

--- MENU ---   
1. Show tasks
2. Add a task
3. Delete a task
4. Save and exit


---

## 2. Data structure – how we store tasks

We’ll store all tasks in a Python **list**.  
Each task will simply be a string.

Example:

```python
tasks = ["Clean the room", "Write a project", "Do the shopping"]
```

A list is easy to modify, iterate through, and save to a file later.

---

## 3. Function to add a task

Let’s start with a simple function that adds a new task to the list:

```python
def add_task(tasks, new_task):
    tasks.append(new_task)
```

### 🗣️ Explanation:

* `append()` adds an element to the end of the list.
* The function doesn’t return anything — it modifies the list directly.

---

## 4. Function to display tasks

Now let’s create a function that nicely prints all the user’s tasks:

```python
def show_tasks(tasks):
    if not tasks:
        print("No tasks on the list.")
    else:
        print("Your tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
```

### 🗣️ Explanation:

* `enumerate()` allows us to number the elements in the list.
* If the list is empty, we display an appropriate message.

---

## 5. Function to delete a task

Next, we’ll add the ability to delete a task by its number.

```python
def delete_task(tasks, number):
    if 0 < number <= len(tasks):
        tasks.pop(number - 1)
        print("Task has been deleted.")
    else:
        print("Invalid task number.")
```

### 🗣️ Explanation:

* `pop()` removes an element from the list by its index.
* We subtract 1 from the user’s number because Python lists start at index `0`.
* We also validate the number to prevent errors.

---

## 6. Saving and loading from a file

We want the task list to be preserved after closing the program.
To do that, we’ll save it to a text file.

### Save function:

```python
def save_tasks(tasks, path):
    with open(path, 'w', encoding='utf-8') as file:
        for task in tasks:
            file.write(task + '\n')
```

### Load function:

```python
def load_tasks(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []
```

### 🗣️ Explanation:

* Each task is written on a separate line.
* `strip()` removes the newline character `\n`.
* If the file doesn’t exist, the function returns an empty list instead of throwing an error.

---

## 7. Main program loop

Now we’ll combine everything into one working program.

```python
def main():
    path = "tasks.txt"
    tasks = load_tasks(path)

    while True:
        print("\n--- MENU ---")
        print("1. Show tasks")
        print("2. Add a task")
        print("3. Delete a task")
        print("4. Save and exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            new = input("Enter a new task: ")
            add_task(tasks, new)
        elif choice == "3":
            show_tasks(tasks)
            try:
                number = int(input("Enter the task number to delete: "))
                delete_task(tasks, number)
            except ValueError:
                print("You must enter a number.")
        elif choice == "4":
            save_tasks(tasks, path)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
```

And finally:

```python
if __name__ == "__main__":
    main()
```

---

## 8. What does `__name__ == "__main__" mean`?

Every `.py` file has a built-in variable called `__name__`.

If the file is run directly (e.g. `python todo.py`), → then `__name__` equals `"__main__"`.

If the file is imported as a module (e.g. `import todo`), → then `__name__` equals `"todo"` (the filename without `.py`).

That’s why we use:

```python
if __name__ == "__main__":
    main()
```

### 🧠 Why we do this:

* The `main()` function only runs when the file is executed directly.
* If we import the file into another project, it won’t automatically start running.

---

## 9. Project structure

```arduino
todo_cli/
├── todo.py           # main program script (functions + main loop)
├── tasks.txt         # file with saved tasks
└── README_EN.md      # documentation (this file)
```

---

## 10. Example program run

```markdown
--- MENU ---
1. Show tasks
2. Add a task
3. Delete a task
4. Save and exit

Choose an option: 2
Enter a new task: Record lesson 26
Task added!

--- MENU ---
1. Show tasks
2. Add a task
3. Delete a task
4. Save and exit
```

---

## 11. Testing and error handling

### ✅ How to test:

* Add a few tasks, then display the list.
* Try deleting a task using both valid and invalid numbers.
* Exit the program, run it again, and check if your list was saved.

### ⚠️ Common issues:

* Entering something other than a number when deleting (`ValueError`).
* Trying to delete a task with a non-existent number.
* Missing `tasks.txt` file on first run (handled with `try/except`).

---

## 12. Ideas for improving the project

Try extending your program with extra features:

1. **✏️ Edit tasks** — ability to modify a task’s text.
2. **✅ Mark as done** — add a “completed” status.
3. **🔍 Filtering** — show only completed or active tasks.
4. **📅 Add due dates** — assign a deadline to each task.
5. **🔄 Sorting** — sort tasks alphabetically or by date.
6. **💻 Command-line interface** — use the `argparse` module for arguments.
7. **💾 JSON format** — store data in a `.json` file instead of `.txt`.

Each of these improvements is a great exercise that brings you closer to building real-world Python applications.

---

## ✅ Summary

You’ve built a working **TODO CLI** — a simple but practical task manager.

Through this lesson, you’ve learned how to:

* organize your code with **functions**,
* handle **data storage** using files,
* practice **user error handling**,
* and create a **text-based user interface** that behaves like a real program.

This is already a complete mini-project you can expand further.   
Add new features, experiment with data formats, and enjoy creating your own programming tools!

© 2025 PotegaIT – Python Course for Beginners

