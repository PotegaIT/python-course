## 🇵🇱 Wersja polska

# Lekcja 4 – Jak działają terminal, interpretery i IDE – praktyczne wprowadzenie

W tej lekcji poznasz podstawowe narzędzia używane przez programistów: terminal, interpreter Pythona i środowiska IDE. Zrozumienie ich działania pozwoli Ci lepiej kontrolować swój kod i wiedzieć, co dzieje się „pod maską” programu.

## Terminal

Terminal to narzędzie umożliwiające komunikację z komputerem za pomocą tekstu. Zamiast klikać w ikony, wpisujesz polecenia, np. aby wyświetlić pliki w folderze, wejść do innego katalogu czy utworzyć nowy dokument. Terminal pozwala sterować systemem operacyjnym w precyzyjny sposób i działa na Linuxie, macOS i Windowsie (PowerShell lub CMD). Programiści cenią terminal, ponieważ daje większą kontrolę, umożliwia automatyzację zadań i często jest szybszy niż klikanie po folderach.

### Przykładowe polecenia:

#### Linux/macOS:

* **pwd** – pokaż bieżący katalog
* **ls** – pokaż pliki w katalogu
* **cd folder** – wejdź do folderu

#### Windows (PowerShell/CMD):

* cd folder
* dir

## Interpreter Pythona

Interpreter to program, który czyta kod źródłowy linijka po linijce i natychmiast go wykonuje. 
Python jest językiem interpretowanym, więc nie wymaga wcześniejszej kompilacji. 
Jeśli w pliku napiszesz `print("Hello")`, interpreter od razu wykona tę linijkę.

### Jak działa interpreter:

* Piszesz kod w pliku .py, np. `hello.py`.

* Interpreter Pythona analizuje każdą linijkę od góry.

* Wykonuje kod po kolei, linia po linii.

* Jeśli napotka błąd, zatrzymuje wykonanie i pokazuje komunikat o błędzie.

Przykład pliku **hello.py**:
```python
print("Linia 1")
print("Linia 2")
print("Linia 3")
```

### Uruchomienie w terminalu:
```python
python hello.py
```
Interpreter przeczyta i wykona każdą linijkę po kolei.
Jeśli w środku znajdzie błąd, np. brak cudzysłowu w `print(Linia 2)`, Python zatrzyma się i pokaże komunikat błędu.

## IDE i edytory kodu

IDE (Integrated Development Environment) to zintegrowane środowisko programistyczne, które łączy w jednym miejscu edytor kodu, podpowiedzi,
podświetlanie składni, terminal i narzędzia do debugowania. 
Popularne IDE to [PyCharm](https://www.jetbrains.com/pycharm/), [VS Code](https://code.visualstudio.com/), [Thonny](https://thonny.org/), [IDLE](https://docs.python.org/3/library/idle.html).
Możesz też używać prostych edytorów tekstu (np. [Notepad++](https://notepad-plus-plus.org/)) i uruchamiać programy przez terminal.

### Warto poznać:

* jak wygląda plik **.py** w IDE

* gdzie znajduje się terminal w IDE

* jak zapisać i uruchomić kod bez wychodzenia z edytora

## Podsumowanie

Teraz wiesz, jak działa interpreter Pythona, potrafisz uruchamiać programy w terminalu i korzystać z profesjonalnego środowiska IDE.
To podstawowe umiejętności, które pozwalają rozwijać projekty i świadomie korzystać z narzędzi programistycznych.

© 2025 PotęgaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version

# Lesson 4 – How the Terminal, Interpreters, and IDEs Work – A Practical Introduction

In this lesson, you will learn about the basic tools used by programmers: the terminal, the Python interpreter, and IDEs.
Understanding how they work will help you better control your code and know what happens "under the hood" of your program.

## Terminal

The terminal is a tool that allows you to communicate with the computer using text. 
Instead of clicking icons, you type commands, for example, to list files in a folder, navigate to another directory, or create a new document. 
The terminal allows precise control over the operating system and works on Linux, macOS, and Windows (PowerShell or CMD). 
Programmers value the terminal because it gives more control, enables task automation, and is often faster than navigating folders by clicking.

### Example commands:

#### Linux/macOS:

* **pwd** – show the current directory
* **ls** – list files in the directory
* **cd folder** – go into a folder

#### Windows (PowerShell/CMD):

* cd folder
* dir

## Python Interpreter

An interpreter is a program that reads source code line by line and executes it immediately.
Python is an interpreted language, so it does not require prior compilation.
If you write `print("Hello")` in a file, the interpreter executes that line right away.

### How the interpreter works:

* You write code in a .py file, e.g., hello.py
* The Python interpreter analyzes each line from top to bottom
* It executes the code line by line
* If it encounters an error, it stops execution and shows an error message

Example **hello.py** file:
```python
print("Line 1")
print("Line 2")
print("Line 3")
```
### Running in the terminal:
```python
python hello.py
```
The interpreter reads and executes each line in order.
If there is an error, e.g., missing quotes in `print(Line 2)`, Python will stop immediately and display an error message.

## IDEs and Code Editors

An IDE (Integrated Development Environment) is an integrated programming environment that combines in one place: a code editor, suggestions, syntax highlighting, terminal, and debugging tools.
Popular IDEs include [PyCharm](https://www.jetbrains.com/pycharm/), [VS Code](https://code.visualstudio.com/), [Thonny](https://thonny.org/), [IDLE](https://docs.python.org/3/library/idle.html).
You can also use simple text editors [Notepad++](https://notepad-plus-plus.org/)) and run programs via the terminal.

### What to explore:

* How a .py file looks in an IDE
* Where the terminal is located in an IDE
* How to save and run code without leaving the editor

## Summary

Now you know how the Python interpreter works, how to run programs in the terminal, and how to use a professional IDE.
These are essential skills that allow you to develop projects and use programming tools effectively.

© 2025 PotegaIT – Python Course for Beginners
