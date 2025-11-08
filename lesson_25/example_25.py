# Prosty szyfrator plików wykorzystujący szyfr Cezara
# Simple file encryptor using Caesar cipher

def szyfruj_tekst(tekst, przesuniecie): 
    # Funkcja szyfruje tekst przesuwając każdy znak o podaną wartość przesunięcia
    # Function encrypts text by shifting each character by a given shift value
    zaszyfrowany = "" 
    for znak in tekst: 
        # Zamiana znaku na kod ASCII, przesunięcie, zamiana z powrotem na znak
        # Convert character to ASCII code, shift it, convert back to character
        zaszyfrowany += chr(ord(znak) + przesuniecie) 
    return zaszyfrowany             

def wczytaj_plik(sciezka): 
    # Funkcja wczytuje zawartość pliku tekstowego
    # Function reads the content of a text file
    with open(sciezka, 'r', encoding='utf-8') as plik: 
        zawartosc = plik.read() 
    return zawartosc                   

def zapisz_plik(sciezka, tekst): 
    # Funkcja zapisuje tekst do pliku o podanej ścieżce
    # Function writes text to a file at the given path
    with open(sciezka, 'w', encoding='utf-8') as plik: 
        plik.write(tekst)  

def szyfruj_plik(plik_wejsciowy, plik_wyjsciowy, przesuniecie): 
    # Funkcja szyfruje zawartość pliku wejściowego i zapisuje wynik do pliku wyjściowego
    # Function encrypts the content of the input file and writes the result to the output file
    tekst = wczytaj_plik(plik_wejsciowy) 
    zaszyfrowany = szyfruj_tekst(tekst, przesuniecie) 
    zapisz_plik(plik_wyjsciowy, zaszyfrowany) 

# Pobranie od użytkownika ścieżek do plików oraz wartości przesunięcia
# Getting file paths and shift value from the user
wejscie = input("Podaj sciezke do pliku do zaszyfrowania: ") 
wyjscie = input("Podaj ciezke do nowego pliku zaszyfrowanego: ") 
przesuniecie = int(input("Podaj wartosc przesuniecia (np. 3): ")) 

# Szyfrowanie pliku
# Encrypting the file
szyfruj_plik(wejscie, wyjscie, przesuniecie) 

print("Plik zostal zaszyfrowany!")  
# File has been encrypted!
