## 🇵🇱 Wersja polska

# 🔐 Lekcja 25 — Szyfrator plików (projekt)

---

## 🎯 Cel lekcji

Celem lekcji jest zbudowanie prostego, samodzielnego projektu w Pythonie — szyfratora plików.

Nauczysz się, jak:

* czytać i zapisywać pliki tekstowe (z obsługą `utf-8`),
* napisać funkcję szyfrującą (prosty szyfr Cezara),
* komponować program z mniejszych funkcji (modularność),
* przemyśleć ograniczenia prostego szyfrowania i możliwe ulepszenia.

To praktyczny projekt, który łączy umiejętności pracy z plikami, operacji na znakach i organizacji kodu.

---

## 1. Krótkie wprowadzenie do szyfrowania

Szyfrowanie to przekształcenie czytelnej treści (plaintext) w postać nieczytelną (ciphertext), tak aby osoby bez klucza nie mogły jej zrozumieć.
W tym projekcie użyjemy najprostszej metody — **szyfru Cezara** — polegającego na przesunięciu kodów znaków o stałą wartość:

Przykład: przy przesunięciu = `3`   
`A → D`, `B → E`, `C → F` itd.

> Uwaga: nasz przykład jest edukacyjny.   
> Szyfr Cezara jest łatwy do złamania i nie nadaje się do ochrony wrażliwych danych.   
> Służy tu do zrozumienia mechaniki szyfrowania.

---

## 2. Plan działania programu

Projekt zrealizujemy w kilku przejrzystych krokach:

1. Odczytamy zawartość pliku wejściowego (tekst).
2. Zastosujemy funkcję szyfrującą do całego tekstu (przesunięcie znaków).
3. Zapiszemy zaszyfrowany tekst do pliku wyjściowego.
4. _(Opcjonalnie)_ udostępnimy funkcję odszyfrowującą — ta sama logika z odwrotnym przesunięciem.

---

## 3. Funkcja szyfrująca (szyfr Cezara)

Prosta funkcja przyjmująca tekst i wartość przesunięcia:

```python
def szyfruj_tekst(tekst, przesuniecie):
    zaszyfrowany = ""
    for znak in tekst:
        zaszyfrowany += chr(ord(znak) + przesuniecie)
    return zaszyfrowany
```

### 🗣️ Wyjaśnienie:

* `ord(znak)` — zwraca kod liczbowy znaku (np. `'A'` → 65).
* `chr(kod)` — zwraca znak odpowiadający kodowi.
* Dodajemy **przesuniecie** do kodu znaku, co daje nowy znak.

#### ⚠️ Ważna uwaga:    
powyższa implementacja przesuwa wszystkie znaki (litery, cyfry, spacje, znaki diakrytyczne).

Można ją rozbudować, aby:

* przesuwać tylko alfabety ASCII,
* zachowywać wielkość liter,
* obsługiwać polskie znaki poprawnie (wymaga to bardziej zaawansowanej logiki lub normalizacji).

---

## 4. Odczyt pliku (bezpiecznie)

Używamy `with open(..., encoding='utf-8')`, aby zapewnić poprawne czytanie plików z polskimi znakami:

```python
def wczytaj_plik(sciezka):
    with open(sciezka, 'r', encoding='utf-8') as plik:
        zawartosc = plik.read()
    return zawartosc
```

### 🗣️ Wyjaśnienie:

* `with` automatycznie zamyka plik nawet w przypadku błędu.
* `encoding='utf-8'` jest zalecany przy pracy z tekstami zawierającymi znaki narodowe.

---

## 5. Zapis pliku

Zapisujemy wynik do nowego pliku (nadpisuje istniejący):

```python
def zapisz_plik(sciezka, tekst):
    with open(sciezka, 'w', encoding='utf-8') as plik:
        plik.write(tekst)
```

### 🗣️ Wyjaśnienie:

* Tryb `'w'` tworzy plik, jeśli go nie ma, lub nadpisuje istniejący.
* ⚠️ Pamiętaj: nadpisanie jest nieodwracalne — zadbaj o testy na kopii plików.

---

## 6. Funkcja łącząca wszystko: `szyfruj_plik`

Kompozycja funkcji — czyta, szyfruje i zapisuje:

```python
def szyfruj_plik(plik_wejsciowy, plik_wyjsciowy, przesuniecie):
    tekst = wczytaj_plik(plik_wejsciowy)
    zaszyfrowany = szyfruj_tekst(tekst, przesuniecie)
    zapisz_plik(plik_wyjsciowy, zaszyfrowany)
```

Przykładowe użycie (interakcyjne):

```python
wejscie = input("Podaj ścieżkę do pliku do zaszyfrowania: ")
wyjscie = input("Podaj ścieżkę do nowego pliku zaszyfrowanego: ")
przesuniecie = int(input("Podaj wartość przesunięcia (np. 3): "))

szyfruj_plik(wejscie, wyjscie, przesuniecie)
print("Plik został zaszyfrowany!")
```

---

## 7. Testowanie i bezpieczeństwo

Jak testować:

* Najpierw użyj pliku testowego z prostą zawartością (np. `test.txt`).
* Wypróbuj różne wartości przesunięcia (np. 1, 3, 10).
* Sprawdź, czy plik wyjściowy powstaje i ma zmienioną treść.
* Przywróć oryginalny plik z kopii, aby uniknąć utraty danych.

### Ograniczenia bezpieczeństwa:

* Szyfr Cezara jest nieskuteczny wobec podstawowych ataków (analiza częstotliwości, brute force).
* Nie stosuj go do ochrony wrażliwych danych.
* W produkcji używa się sprawdzonych algorytmów (**AES**, **RSA**) i bibliotek kryptograficznych (np. `cryptography` w Pythonie).

---

### 8. Pomysły na rozszerzenia (ćwiczenia / zadania domowe)

1. **Funkcja odszyfrowująca** — ta sama logika, ale przesunięcie ujemne.
2. **Ograniczenie szyfru do liter** — przesuwaj tylko znaki alfabetu (oddzielnie dla małych i wielkich liter), tak by zachować spacje i znaki interpunkcyjne.
3. **Obsługa polskich znaków** — zastosuj mapowanie na zakresy Unicode lub normalizację, aby poprawnie przetwarzać `ą`, `ę`, `ś` itp.
4. **Tryb binarny** — szyfruj pliki binarne (np. obrazy) — wymaga operowania w trybie `'rb'` i `'wb'` oraz odpowiedniej logiki.
5. **Użycie bezpiecznego algorytmu** — naucz się korzystać z biblioteki `cryptography` i zaimplementuj szyfrowanie symetryczne (AES) z hasłem.
6. **Interfejs CLI** — dodaj argumenty wiersza poleceń (np. z modułu `argparse`) zamiast interakcji `input()`.

---

## 9. Przykładowa pełna struktura projektu

```arduino
szyfrator/
├── szyfrator.py         # główny skrypt (z funkcjami: wczytaj_plik, szyfruj_tekst, zapisz_plik, szyfruj_plik)
├── tests/
│   └── test_input.txt   # plik testowy
└── README.md            # instrukcja (ten plik)
```

---

## 10. Przykładowa implementacja (skrót)

```python
def szyfruj_tekst(tekst, przesuniecie):
    zaszyfrowany = ""
    for znak in tekst:
        zaszyfrowany += chr(ord(znak) + przesuniecie)
    return zaszyfrowany

def wczytaj_plik(sciezka):
    with open(sciezka, 'r', encoding='utf-8') as plik:
        return plik.read()

def zapisz_plik(sciezka, tekst):
    with open(sciezka, 'w', encoding='utf-8') as plik:
        plik.write(tekst)

def szyfruj_plik(plik_wejsciowy, plik_wyjsciowy, przesuniecie):
    tekst = wczytaj_plik(plik_wejsciowy)
    zaszyfrowany = szyfruj_tekst(tekst, przesuniecie)
    zapisz_plik(plik_wyjsciowy, zaszyfrowany)
```

---

## ✅ Podsumowanie

W tej lekcji zrealizowałeś kompletny, praktyczny projekt:

* zbudowałeś szyfrator plików oparty na szyfrze **Cezara**,
* nauczyłeś się bezpiecznie czytać i zapisywać pliki z **kodowaniem UTF-8**,
* połączyłeś modularne funkcje w prosty program użytkowy,
* poznałeś ograniczenia takiego rozwiązania i możliwe kierunki rozwoju.

To świetne ćwiczenie łączące podstawy programowania z elementami praktycznego inżynierowania oprogramowania.   
Zachęcam do eksperymentów z rozszerzeniami — szczególnie do nauki bezpieczniejszych algorytmów kryptograficznych, gdy będziesz gotowy.

© 2025 PotęgaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version

# 🔐 Lesson 25 — File Encryptor (Project)

---

## 🎯 Lesson Objective

The goal of this lesson is to build a simple, standalone Python project — a file encryptor.

You will learn how to:

* read and write text files (with `utf-8` encoding),
* write an encryption function (simple Caesar cipher),
* compose a program from smaller functions (modularity),
* understand the limitations of basic encryption and explore possible improvements.

This is a hands-on project that combines file handling, character manipulation, and clean program structure.

---

## 1. Short Introduction to Encryption

Encryption is the process of transforming readable text (plaintext) into an unreadable form (ciphertext), so that only people with the right key can understand it.

In this project, we’ll use the simplest example — the **Caesar cipher** — which shifts each character’s code by a fixed value.

Example: with a shift of `3`   
`A → D`, `B → E`, `C → F`, etc.

> Note: this example is for educational purposes only.   
> The Caesar cipher is easy to break and should never be used for protecting sensitive data.   
> Here, it helps us understand the mechanics of encryption.

---

## 2. Program Plan

We will complete the project in a few clear steps:

1. Read the contents of an input text file.
2. Apply the encryption function (shift characters).
3. Save the encrypted text to an output file.
4. _(Optional)_ Add a decryption function — using the same logic with a negative shift.

---

## 3. Encryption Function (Caesar Cipher)

A simple function that takes text and a shift value:

```python
def encrypt_text(text, shift):
    encrypted = ""
    for char in text:
        encrypted += chr(ord(char) + shift)
    return encrypted
```

### 🗣️ Explanation:

* `ord(char)` — converts a character to its numeric code (e.g. `'A'` → 65).
* `chr(code)` — converts the number back to a character.
* Adding the shift changes each character to a new one.

#### ⚠️ Important note:    
This implementation shifts all characters (letters, digits, spaces, punctuation, etc.).

It can be improved by:

* limiting the shift to ASCII letters only,
* preserving case (uppercase/lowercase),
* handling special characters (like accented letters) properly — this requires Unicode-aware logic or normalization.

---

## 4. Reading Files Safely

We use `with open(..., encoding='utf-8')` to ensure correct reading of text files containing special characters:

```python
def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content
```

### 🗣️ Explanation:

* `with` automatically closes the file, even if an error occurs.
* `encoding='utf-8'` ensures proper handling of characters from multiple languages.

---

## 5. Writing Files

We save the encrypted text to a new file (overwriting if it exists):

```python
def save_file(path, text):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)
```

### 🗣️ Explanation:

* Mode `'w'` creates the file if it doesn’t exist, or overwrites it if it does.
* ⚠️ Overwriting is **permanent**, so test on copies of your files first.

---

## 6. Combining Everything: `encrypt_file`

This function ties everything together — reading, encrypting, and saving:

```python
def encrypt_file(input_file, output_file, shift):
    text = read_file(input_file)
    encrypted = encrypt_text(text, shift)
    save_file(output_file, encrypted)
```

Example usage (interactive):

```python
input_path = input("Enter the path of the file to encrypt: ")
output_path = input("Enter the path for the encrypted file: ")
shift = int(input("Enter the shift value (e.g. 3): "))

encrypt_file(input_path, output_path, shift)
print("File has been encrypted!")
```

---

## 7. Testing and Security

### How to test:

* Start with a simple text file (e.g. `test.txt`).
* Try different shift values (e.g. 1, 3, 10).
* Verify that the output file is created and the content has changed.
* Always keep a backup of the original file to avoid data loss.

### Security limitations:

* The Caesar cipher is **extremely weak** — it can be easily broken using frequency analysis or brute force.
* Never use it to protect real data.
* In real-world scenarios, use proven algorithms like **AES** or **RSA**, available in libraries such as Python’s `cryptography`.

---

## 8. Extension Ideas (Exercises / Homework)

1. **Decryption function** — same logic, but with a negative shift.
2. **Limit to letters only** — encrypt only alphabetic characters while preserving spaces and punctuation.
3. **Binary mode** — encrypt binary files (e.g. images) using `'rb'` and `'wb'` modes and appropriate logic.
4. **Secure algorithm** — learn to use the `cryptography` library and implement AES encryption with a password.
5. **CLI interface** — replace `input()` with command-line arguments using the `argparse` module.

---

## 9. Example Project Structure

```arduino
encryptor/
├── encryptor.py         # main script (functions: read_file, encrypt_text, save_file, encrypt_file)
├── tests/
│   └── test_input.txt   # test file
└── README.md            # this instruction file
```

---

## 10. Example Implementation (Summary)

```python
def encrypt_text(text, shift):
    encrypted = ""
    for char in text:
        encrypted += chr(ord(char) + shift)
    return encrypted

def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def save_file(path, text):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)

def encrypt_file(input_file, output_file, shift):
    text = read_file(input_file)
    encrypted = encrypt_text(text, shift)
    save_file(output_file, encrypted)
```

---

## ✅ Summary

In this lesson, you built a complete, hands-on project:

* created a file encryptor based on the **Caesar cipher**,
* learned how to read and write files safely using **UTF-8 encoding**,
* combined modular functions into a working program,
* understood the limitations of simple encryption and potential improvements.

This project combines programming fundamentals with practical software engineering concepts.   
Keep experimenting — especially with more advanced cryptographic algorithms once you’re ready.

© 2025 PotegaIT – Python Course for Beginners
