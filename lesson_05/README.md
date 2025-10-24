## 🇵🇱 Wersja polska

# Lekcja 5 – Zmienne i typy danych (string, int, float, bool)

W tej lekcji poznasz podstawy zmiennych w Pythonie oraz cztery najważniejsze typy danych: **string**, **int**, **float** i **bool**. Zmienna to nazwa, pod którą przechowujemy jakąś wartość – tekst, liczbę lub wartość logiczną. Dzięki zmiennym możemy przechowywać dane i wykorzystywać je w różnych miejscach programu.

## Co to są zmienne?

Zmienna to nazwa, pod którą przechowywana jest wartość. Nadajemy jej nazwę, używamy znaku **równości =** i przypisujemy wartość. Typ danych określa rodzaj wartości przechowywanej w zmiennej.

#### Przykłady:
```sh
name = "Greg" # string – tekst
age = 30 # int – liczba całkowita
height = 1.75 # float – liczba zmiennoprzecinkowa
is_student = True # bool – wartość logiczna
```

## Typy danych – string, int, float, bool

Każda zmienna w Pythonie ma typ danych, który mówi, jakiego rodzaju dane są w niej przechowywane i jak Python ma je traktować.
Poznanie typów danych jest podstawą nauki programowania.

**string (str)** – tekst, ciąg znaków w pojedynczych lub podwójnych cudzysłowach. Przykłady: "Python", "123", 'Hello world'

**int** – liczby całkowite. Przykłady: 5, -100, 2025

**float** – liczby zmiennoprzecinkowe, z częścią dziesiętną (używamy kropki). Przykłady: 3.14, 0.5, -2.0

**bool** – wartości logiczne True lub False. Stosowane do sprawdzania warunków.

## Funkcja type()

Python posiada wbudowaną funkcję **type()**, która pozwala sprawdzić typ zmiennej. 

#### Przykład:
```sh
city = "Oslo"
year = 2025
temperature = 4.5
is_raining = False

print(type(city)) # <class 'str'>
print(type(year)) # <class 'int'>
print(type(temperature)) # <class 'float'>
print(type(is_raining)) # <class 'bool'>
```
Dzięki **type()** można sprawdzić, jakiego typu jest dana zmienna i unikać błędów, np. przy próbie dodania tekstu do liczby.

## Mini projekt

Przykładowy program tworzący zmienne różnych typów i wyświetlający je:

```sh
name = "Anna"
age = 25
height = 1.68
is_logged_in = True

print(f"Użytkownik {name}, wiek: {age}, wzrost: {height} m")
print(f"Czy zalogowany? {is_logged_in}")
```

## Podsumowanie

Dzisiaj nauczyłeś się, czym są zmienne i jak przechowywać w nich różne typy danych. 
Poznałeś cztery podstawowe typy w Pythonie: 

* string,
* int,
* float
* bool.

Dzięki nim możesz przechowywać tekst, liczby i informacje logiczne. 
Te umiejętności są fundamentem każdego programu i będą wykorzystywane w kolejnych lekcjach.
Podsumowanie

Dzisiaj nauczyłeś się, czym są zmienne i jak przechowywać w nich różne typy danych. Poznałeś cztery podstawowe typy w Pythonie: string, int, float i bool. Dzięki nim możesz przechowywać tekst, liczby i informacje logiczne. Te umiejętności są fundamentem każdego programu i będą wykorzystywane w kolejnych lekcjach.

---
