import os                    # Importuje moduł os – pozwala na operacje na systemie plików (np. foldery, pliki) / Imports the os module – allows operations on the file system (e.g., folders, files)
from pathlib import Path     # Importuje klasę Path z modułu pathlib – nowszy i bardziej obiektowy sposób pracy z plikami/katalogami / Imports the Path class from the pathlib module – a newer, object-oriented way to work with files and directories

print(os.getcwd())           # Wyświetla bieżący katalog roboczy (current working directory) za pomocą modułu os / Displays the current working directory using the os module
print(Path.cwd())            # To samo co wyżej, ale z użyciem pathlib / Same as above, but using pathlib

os.mkdir("nowy_folder")      # Tworzy nowy folder o nazwie "nowy_folder" (jeśli jeszcze nie istnieje) / Creates a new folder named "nowy_folder" (if it doesn’t already exist)
Path("nowy_folder1").mkdir() # Tworzy nowy folder "nowy_folder1" – z użyciem pathlib / Creates a new folder "nowy_folder1" – using pathlib

zawartosc = os.listdir(".")  # Pobiera listę plików i folderów w bieżącym katalogu za pomocą os / Gets a list of files and folders in the current directory using os
print(zawartosc)             # Wyświetla listę zawartości katalogu / Prints the directory contents

zawartosc = Path(".").iterdir()  # Zwraca iterator po obiektach Path w bieżącym katalogu (czyli plikach i folderach) / Returns an iterator of Path objects in the current directory (files and folders)
for element in zawartosc:        # Iteruje przez wszystkie elementy w katalogu / Iterates through all elements in the directory
    print(element)               # Wyświetla każdy element (pełna ścieżka do pliku lub folderu) / Prints each element (full path to the file or folder)

sciezka = Path("plik.txt")       # Tworzy obiekt Path wskazujący na plik "plik.txt" / Creates a Path object pointing to the file "plik.txt"
print(sciezka.is_file())         # Sprawdza, czy "plik.txt" istnieje i jest plikiem / Checks if "plik.txt" exists and is a file
print(sciezka.is_dir())          # Sprawdza, czy "plik.txt" istnieje i jest katalogiem / Checks if "plik.txt" exists and is a directory

os.remove("plik.txt")            # Usuwa plik "plik.txt" (jeśli istnieje) – za pomocą os / Deletes the file "plik.txt" (if it exists) – using os
os.rmdir("pusty_folder")         # Usuwa pusty folder "pusty_folder" – za pomocą os / Deletes the empty folder "pusty_folder" – using os

Path("plik.txt").unlink()        # To samo co os.remove – usuwa plik "plik.txt" – tym razem za pomocą pathlib / Same as os.remove – deletes the file "plik.txt" – this time using pathlib
Path("pusty_folder").rmdir()     # To samo co os.rmdir – usuwa pusty folder "pusty_folder" – za pomocą pathlib / Same as os.rmdir – deletes the empty folder "pusty_folder" – using pathlib
