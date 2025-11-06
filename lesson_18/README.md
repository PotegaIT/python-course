## 🇵🇱 Wersja polska

# 🧠 Lekcja 18 – Odczyt i zapis do plików tekstowych

---

## 🎯 Cel lekcji

W tej lekcji nauczysz się, jak **czytać, zapisywać i dopisywać dane** w plikach tekstowych.  
Dzięki temu Twoje programy będą mogły **przechowywać dane na dysku**, zamiast tracić je po każdym uruchomieniu.

Po tej lekcji będziesz potrafić:
- odczytywać zawartość plików tekstowych,
- zapisywać dane do nowych plików,
- dopisywać nowe informacje do już istniejących,
- korzystać z konstrukcji `with`, która bezpiecznie zarządza plikami.

To bardzo praktyczna umiejętność, która pozwoli Twoim programom „żyć” dłużej niż jedno uruchomienie.

---

## 📝 1. Otwieranie i czytanie plików

W Pythonie do pracy z plikami służy funkcja **`open()`**.  
Aby odczytać plik, otwieramy go w **trybie odczytu** (`"r"` – jak *read*).

### 🔧 Przykład:

```python
dokument = open("plik.txt", "r")
zawartosc = dokument.read()
print(zawartosc)
dokument.close()
```

💬 Tutaj:

* otwieramy plik `plik.txt` w trybie odczytu,
* metoda `.read()` wczytuje jego całą zawartość,
* po zakończeniu pracy koniecznie zamykamy plik przez `close()`.

❗ Jeśli plik nie istnieje, Python zgłosi błąd **FileNotFoundError** – to naturalne i później nauczysz się to obsługiwać.

---

## 🧱 2. Bezpieczne otwieranie plików – `with`

Zamiast pamiętać o zamykaniu pliku, Python pozwala użyć konstrukcji `with`, która robi to automatycznie – nawet w przypadku błędu.

### 🔧 Przykład:

```python
with open("plik.txt", "r") as dokument:
    zawartosc = dokument.read()
    print(zawartosc)
```

💬 Gdy kod w bloku `with` się zakończy, plik automatycznie zostanie zamknięty.
To **najlepsza praktyka** – warto korzystać z niej zawsze.

---

## ✏️ 3. Zapisywanie danych do pliku

Aby zapisać dane, otwieramy plik w trybie zapisu (`"w"` – jak write).
Jeśli plik istnieje, zostanie nadpisany – a jeśli nie istnieje, Python utworzy go automatycznie.

### 🔧 Przykład:

```python
with open("nowy_plik.txt", "w") as dokument:
    dokument.write("Witaj w nowym pliku!\n")
    dokument.write("To druga linia tekstu.\n")
```

💬 Znak `\n` oznacza nową linię.
Po uruchomieniu kodu możesz otworzyć `nowy_plik.txt` w edytorze i zobaczyć efekt.

### 💡 Dodatkowa wskazówka

Nie musisz wcześniej ręcznie tworzyć pliku – Python zrobi to za Ciebie:

```python
with open("utworzony_plik.txt", "w") as dokument:
    dokument.write("Ten plik został utworzony przez program!\n")
```

💬 Jeśli plik nie istniał – zostanie utworzony.
Jeśli już istniał – zostanie nadpisany, dlatego warto uważać, aby nie stracić ważnych danych.

---

## ➕ 4. Dopisywanie danych do istniejącego pliku (`"a"` – append)

Jeśli chcesz dodać nowe dane na końcu pliku, użyj trybu `"a"`.
Dzięki temu poprzednia zawartość zostanie zachowana.

### 🔧 Przykład:

```python
with open("nowy_plik.txt", "a") as dokument:
    dokument.write("Dopisujemy nowy wiersz.\n")
```

💬 W trybie `"a"` dane są automatycznie dopisywane na końcu pliku.
To przydatne np. przy tworzeniu logów, zapisywaniu historii lub wyników programu.

---

## 🧩 5. Mini-projekt: zapisujemy zdania użytkownika

Napisz program, który poprosi użytkownika o 3 zdania i zapisze je w osobnym pliku.

### 🔧 Przykład:

```python
with open("moje_zdania.txt", "w") as plik:
    for i in range(3):
        zdanie = input(f"Podaj zdanie nr {i + 1}: ")
        plik.write(zdanie + "\n")

print("Zdania zostały zapisane!")
```

💬 Program uruchomi pętlę 3 razy, za każdym razem prosząc o zdanie.
Każdy wiersz zostanie zapisany osobno w pliku `moje_zdania.txt`.

💡 Wskazówka: po uruchomieniu programu sprawdź w folderze, czy plik został utworzony i co zawiera.

---

## 🎉 Podsumowanie lekcji 18

W tej lekcji nauczyłeś się:

* czytać dane z pliku (`open("plik.txt", "r")`)
* zapisywać dane do pliku (`open("plik.txt", "w")`)
* dopisywać dane do istniejących plików (`open("plik.txt", "a")`)
* używać konstrukcji `with` dla bezpiecznej pracy z plikami

Teraz potrafisz tworzyć programy, które przechowują dane między uruchomieniami —
czyli notatniki, rejestry, logi, a nawet proste bazy danych tekstowych.

© 2025 PotęgaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version

# 🧠 Lesson 18 – Reading and Writing Text Files

---

## 🎯 Lesson Goal

In this lesson, you’ll learn how to **read, write, and append data** in text files.
This allows your programs to **store information on disk**, instead of losing it every time you close them.

After completing this lesson, you’ll be able to:

* read the contents of text files,
* write data into new files,
* append information to existing files,
* use the `with` statement for safe file handling.

This is a very practical skill — it lets your programs “live” longer than a single execution.

---

## 📝 1. Opening and Reading Files

In Python, the function `open()` is used for working with files.
To read a file, we open it in read mode (`"r"` – as in *read*).

### 🔧 Example:

```python
document = open("file.txt", "r")
content = document.read()
print(content)
document.close()
```

💬 Here:

* we open the file `file.txt` in read mode,
* the `.read()` method loads its entire content,
* after finishing, we must close the file with `close()`.

❗ If the file doesn’t exist, Python will raise a **FileNotFoundError** – that’s normal, and you’ll learn how to handle it later.

---

## 🧱 2. Safe File Opening – `with`

Instead of remembering to close files manually, Python provides the `with` statement,
which automatically closes the file, even if an error occurs.

### 🔧 Example:

```python
with open("file.txt", "r") as document:
    content = document.read()
    print(content)
```

💬 When the code inside the `with` block finishes, the file is automatically closed.
This is the best **practice** – you should always use `with` for file operations.

---

## ✏️ 3. Writing Data to a File

To save data, open the file in write mode (`"w"` – as in *write*).
If the file already exists, it will be overwritten.
If it doesn’t exist, Python will create it automatically.

### 🔧 Example:

```python
with open("new_file.txt", "w") as document:
    document.write("Welcome to the new file!\n")
    document.write("This is the second line of text.\n")
```

💬 The `\n` character means a new line.
After running this code, you can open `new_file.txt` in any text editor to see the result.

### 💡 Additional Tip

You don’t need to manually create the file first – Python will do it for you:

```python
with open("created_file.txt", "w") as document:
    document.write("This file was created by the program!\n")
```

💬 If the file didn’t exist – it will be created.
If it already existed – it will be overwritten.
Be careful not to lose important data!

---

## ➕ 4. Appending Data to an Existing File (`"a"` – append)

If you want to **add new data at the end of a file**, use **append mode** (`"a"`).
This way, the previous content remains unchanged.

### 🔧 Example:

```python
with open("new_file.txt", "a") as document:
    document.write("Adding a new line.\n")
```

💬 In `"a"` mode, data is automatically written at the end of the file.
This is useful for logs, history files, or saving results over time.

---

## 🧩 5. Mini Project: Save User Sentences

Write a program that asks the user for 3 sentences and saves them in a file.

### 🔧 Example:

```python
with open("my_sentences.txt", "w") as file:
    for i in range(3):
        sentence = input(f"Enter sentence #{i + 1}: ")
        file.write(sentence + "\n")

print("Your sentences have been saved!")
```

💬 The program runs a loop 3 times, asking for a sentence each time.
Each one is written on a separate line in `my_sentences.txt`.

💡 Tip: After running the program, check the folder to see the new file and its contents.

---

## 🎉 Summary of Lesson 18

In this lesson, you learned how to:

* read data from a file (`open("file.txt", "r")`)
* write data to a file (`open("file.txt", "w")`)
* append data to existing files (`open("file.txt", "a")`)
* use the `with` statement for safe file operations

Now you can create programs that **store data between runs** —
such as notes, logs, records, or even simple text-based databases.

© 2025 PotegaIT – Python Course for Beginners
