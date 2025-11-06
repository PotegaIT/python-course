# Przykłady błędów w Pythonie / Examples of errors in Python

# SyntaxError – błąd składniowy / SyntaxError – syntax mistake
print("Witaj"  # Brakuje zamykającego nawiasu / Missing closing parenthesis

# ValueError – błąd konwersji typu / ValueError – type conversion error
liczba = int("abc")  # Próba zamiany tekstu na liczbę / Trying to convert text to int

# NameError – niezdefiniowana zmienna / NameError – undefined variable
print(imie)  # Zmienna 'imie' nie została zdefiniowana / Variable 'imie' is not defined

# IndexError – odwołanie do nieistniejącego indeksu listy / IndexError – accessing non-existing list index
lista = [1, 2, 3]
print(lista[5])  # Lista ma tylko 3 elementy / The list has only 3 elements

# ZeroDivisionError – dzielenie przez zero / ZeroDivisionError – division by zero
wynik = 10 / 0  # Nie wolno dzielić przez zero / Cannot divide by zero

# TypeError – operacja na niekompatybilnych typach / TypeError – operation on incompatible types
wynik = "tekst" + 5  # Nie można dodawać tekstu i liczby / Cannot add string and integer

# Użycie print-debugging / Using print-debugging
def dzielenie(a, b):
    print("a =", a)  # Wyświetla wartość a / Shows value of a
    print("b =", b)  # Wyświetla wartość b / Shows value of b
    wynik = a / b
    return wynik

dzielenie(10, 0)  # Wywołanie spowoduje ZeroDivisionError / This call will raise ZeroDivisionError

# Przykład try/except / Example of try/except
try:
    liczba = int(input("Podaj liczbę: "))  # Pobranie liczby od użytkownika / Get number from user
    print("Liczba x 2 =", liczba * 2)      # Wypisanie podwojonej wartości / Print doubled value
except ValueError:
    print("To nie była liczba!")           # Obsługa błędu konwersji / Handle conversion error
  
