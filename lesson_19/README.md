## 🇵🇱 Wersja polska

# 🧠 Lekcja 19 – Praca z katalogami i systemem plików (`os`, `pathlib`)

---

## 🎯 Cel lekcji

W tej lekcji nauczysz się, jak **pracować z plikami i katalogami na dysku** — czyli jak tworzyć foldery, usuwać je, sprawdzać ich zawartość i rodzaj (plik lub katalog).  
Dzięki temu będziesz mógł **automatyzować zadania**, takie jak porządkowanie danych, generowanie raportów czy analiza zawartości folderów.

Poznasz dwie biblioteki:

- **`os`** – starsza, klasyczna, bardzo stabilna,
- **`pathlib`** – nowsza, bardziej czytelna i obiektowa.

W praktyce często będziesz używać `pathlib`, ponieważ kod z jej użyciem jest prostszy i bardziej „pythoniczny”.

---

## 📝 1. Sprawdzanie aktualnego katalogu roboczego

Każdy program działa w tzw. **katalogu roboczym** – to folder, z którego został uruchomiony.  
Aby sprawdzić, gdzie aktualnie jesteś, możesz użyć jednej z poniższych metod:

### 🔧 Przykład z `os`:

```python
import os

print(os.getcwd())  # get current working directory
```

### 🔧 Przykład z `pathlib`:

```python
from pathlib import Path

print(Path.cwd())
```

💬 Obie wersje zwracają tę samą ścieżkę – katalog, w którym działa Twój program.
To istotne, ponieważ jeśli otwierasz plik bez podania pełnej ścieżki, Python będzie go szukał właśnie w tym miejscu.

---

## 📁 2. Tworzenie nowego folderu

Czasami program musi utworzyć nowy katalog – np. na raporty lub zapisane wyniki.

### 🔧 Przykład z `os`:

```python
import os

os.mkdir("nowy_folder")
```

### 🔧 Przykład z `pathlib`:

```python
from pathlib import Path

Path("nowy_folder1").mkdir()
```

💬 Jeśli folder o tej nazwie już istnieje, Python zgłosi błąd.
Dlatego warto wcześniej sprawdzić, czy taki katalog już jest – zobaczysz to w mini-projekcie poniżej.

---

## 📄 3. Wyświetlanie zawartości folderu

Jeśli chcesz zobaczyć, co znajduje się w katalogu (np. wypisać listę plików), możesz to zrobić na dwa sposoby:

### 🔧 Przykład z `os`:

```python
import os

zawartosc = os.listdir(".")  # "." oznacza bieżący folder
print(zawartosc)
```

### 🔧 Przykład z `pathlib`:

```python
from pathlib import Path

zawartosc = Path(".").iterdir()
for element in zawartosc:
    print(element)
```

💬 `os.listdir()` zwraca listę nazw (napisów),
a `pathlib.iterdir()` zwraca obiekty typu `Path`, które dają więcej możliwości — np. sprawdzenie, czy element to plik lub katalog.

---

## 🔍 4. Sprawdzanie, czy coś jest plikiem czy katalogiem

Jeśli przeglądasz zawartość folderu, dobrze wiedzieć, które elementy są plikami, a które katalogami.

### 🔧 Przykład z `pathlib`:

```python
from pathlib import Path

sciezka = Path("plik.txt")
print(sciezka.is_file())   # True jeśli to plik
print(sciezka.is_dir())    # True jeśli to katalog
```

💬 Dzięki temu możesz np. filtrować tylko pliki `.txt`, pominąć katalogi albo znaleźć podfoldery tematyczne.

---

## 🗑️ 5. Usuwanie plików i katalogów

Czasami chcesz coś usunąć — ale pamiętaj: **Python nie pyta o potwierdzenie!**
Usuniętych plików nie da się łatwo odzyskać.

### 🔧 Przykład z `os`:

```python
import os

os.remove("plik.txt")        # usuwa plik
os.rmdir("pusty_folder")     # usuwa pusty katalog
```

### 🔧 Przykład z `pathlib`:

```python
from pathlib import Path

Path("plik.txt").unlink()     # usuwa plik
Path("pusty_folder").rmdir()  # usuwa pusty folder
```

💬 Funkcje `rmdir()` i `os.rmdir()` działają tylko dla pustych katalogów.
Jeśli chcesz usunąć folder z zawartością, możesz użyć `shutil.rmtree()`, ale to temat dla bardziej zaawansowanych.

---

## 🧩 6. Mini-projekt: katalog „raporty”

Zróbmy mały program, który:

1. sprawdzi, czy istnieje katalog `raporty`,
2. jeśli nie – utworzy go,
3. a następnie wypisze jego zawartość.

### 🔧 Kod:

```python
from pathlib import Path

katalog = Path("raporty")

if not katalog.exists():
    katalog.mkdir()

print("Zawartość katalogu 'raporty':")
for element in katalog.iterdir():
    print("-", element)
```

💬 Dzięki temu programowi możesz łatwo sprawdzić, czy katalog istnieje, utworzyć go, a następnie przejrzeć jego zawartość.
To świetna baza pod tworzenie automatycznych systemów raportujących, archiwizujących lub porządkujących dane.

---

## 🎉 Podsumowanie lekcji 19

W tej lekcji nauczyłeś się:

* sprawdzać, w jakim katalogu działa Twój program (`os.getcwd()` / `Path.cwd()`),
* tworzyć nowe foldery (`os.mkdir()` / `Path.mkdir()`),
* przeglądać zawartość katalogu (`os.listdir()` / `Path.iterdir()`),
* rozróżniać pliki i katalogi (`is_file()` / `is_dir()`),
* usuwać niepotrzebne pliki i foldery.

Poznałeś dwie biblioteki – klasyczną os i nowoczesną **pathlib**.
Od teraz możesz tworzyć programy, które **zarządzają plikami i strukturą katalogów** – to pierwszy krok w kierunku automatyzacji zadań i tworzenia prawdziwych narzędzi programistycznych.

© 2025 PotęgaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version

# 🧠 Lesson 19 – Working with Directories and the File System (`os`, `pathlib`)

---

## 🎯 Lesson Objective

In this lesson, you’ll learn how to **work with files and directories on your computer** — how to create folders, delete them, check their contents, and determine whether something is a file or a directory.
This knowledge allows you to **automate everyday tasks** such as organizing data, generating reports, or analyzing the contents of folders.

You’ll get to know two Python libraries:

`os` – older, classic, and very stable,

`pathlib` – newer, more readable, and object-oriented.

In modern Python code, we often use `pathlib`, because it makes your code cleaner and more “Pythonic”.

---

## 📝 1. Checking the Current Working Directory

Every Python program runs in a **working directory** — the folder where the script is executed.
To check your current location, use one of the following methods:

### 🔧 Example with `os`:

```python
import os

print(os.getcwd())  # get current working directory
```

### 🔧 Example with `pathlib`:

```python
from pathlib import Path

print(Path.cwd())
```

💬 Both methods return the same result — the path to the folder where your program is running.
This is important because if you open a file without specifying the full path, Python will look for it in this exact directory.

---

## 📁 2. Creating a New Folder

Sometimes you’ll want your program to create a new directory — for example, to store reports or generated files.

### 🔧 Example with `os`:

```python
import os

os.mkdir("new_folder")
```

### 🔧 Example with `pathlib`:

```python
from pathlib import Path

Path("new_folder1").mkdir()
```

💬 If a folder with the same name already exists, Python will raise an error.
That’s why it’s a good idea to check if the directory exists before creating it — you’ll see how in the mini project below.

---

## 📄 3. Listing the Contents of a Folder

If you want to see what’s inside a folder — for example, to list all files or filter out specific types — you can do it like this:

### 🔧 Example with `os`:

```python
import os

contents = os.listdir(".")  # "." means current directory
print(contents)
```

🔧 Example with `pathlib`:

```python
from pathlib import Path

contents = Path(".").iterdir()
for element in contents:
    print(element)
```

💬 The difference is that`os.listdir()` returns a list of strings,
while `pathlib.iterdir()` returns **Path objects**, which give you more control and extra methods (for example, checking if it’s a file or a directory).

---

## 🔍 4. Checking If It’s a File or a Directory

When you list folder contents, it’s useful to know whether each item is a file or a directory.

### 🔧 Example with `pathlib`:

```python
from pathlib import Path

path = Path("file.txt")
print(path.is_file())   # True if it's a file
print(path.is_dir())    # True if it's a directory
```

💬 This feature allows you to, for instance, process only `.txt` files, skip folders, or search for specific directories.

## 🗑️ 5. Deleting Files and Folders

Sometimes you’ll need to delete files or folders — but remember: **Python won’t ask for confirmation!**
Once deleted, files are gone permanently.

### 🔧 Example with `os`:

```python
import os

os.remove("file.txt")        # delete a file
os.rmdir("empty_folder")     # delete an empty directory
```

### 🔧 Example with `pathlib`:

```python
from pathlib import Path

Path("file.txt").unlink()     # delete a file
Path("empty_folder").rmdir()  # delete an empty folder
```

💬 Both `rmdir()` and `os.rmdir()` only work on empty directories.
If you need to delete directories with content, you can use `shutil.rmtree()` — but that’s a topic for more advanced lessons.

---

## 🧩 6. Mini Project: The “Reports” Folder

Let’s create a small program that will:

1. Check if a folder named `reports` exists,
2. Create it if it doesn’t,
3. And then list its contents.

### 🔧 Example Code:

```python
from pathlib import Path

folder = Path("reports")

if not folder.exists():
    folder.mkdir()

print("Contents of 'reports' folder:")
for element in folder.iterdir():
    print("-", element)
```

💬 This program checks for the folder’s existence, creates it if necessary, and lists its contents.
It’s a great foundation for creating automated **reporting or data-archiving tools**.

---

## 🎉 Lesson 19 Summary

In this lesson, you learned how to:

* check the current working directory (`os.getcwd()` / `Path.cwd()`),
* create new folders (`os.mkdir()` / `Path.mkdir()`),
* list folder contents (`os.listdir()` / `Path.iterdir()`),
* distinguish between files and folders (`is_file()` / `is_dir()`),
* and safely delete unnecessary files or directories.

You’ve also discovered two key libraries — the classic os and the modern **pathlib**.
From now on, you can write programs that **manage files and directory structures** — a key skill for automation, data management, and professional-level development.

© 2025 PotegaIT – Python Course for Beginners
