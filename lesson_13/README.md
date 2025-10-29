## 🇵🇱 Wersja polska

# 🧠 Lekcja 13 – Sterowanie przebiegiem pętli: break i continue

---

## 🎯 Cel lekcji

W tej lekcji nauczysz się, jak dokładnie kontrolować działanie pętli.
Poznasz dwa bardzo przydatne słowa kluczowe w Pythonie – `break` i `continue`.

Dzięki nim możesz:

* przerwać pętlę w dowolnym momencie (`break`),
* pominąć jeden krok i przejść dalej (`continue`).

To potężne narzędzia, które dają Ci większą kontrolę nad przebiegiem programu.

---

## 📝 1. Instrukcja `break` – przerywanie pętli

Instrukcja `break` działa jak **przycisk awaryjny**.
Kiedy Python ją napotka, **natychmiast kończy działanie pętli**, nawet jeśli warunek pętli wciąż jest spełniony.
Używamy jej wtedy, gdy nie ma sensu kontynuować dalszego działania – np. gdy znaleźliśmy to, czego szukaliśmy.

```python
for liczba in range(10):
    if liczba == 5:
        print("Znaleziono 5! Kończę.")
        break
    print("Sprawdzam:", liczba)
```

### 🔍 Wyjaśnienie:

* Program sprawdza liczby od 0 do 9.
* Gdy napotka 5 – przerywa pętlę.
* Liczby po 5 nie zostaną już sprawdzone.

---

## 📝 2. Instrukcja `continue` – pomijanie jednej iteracji

Instrukcja `continue` działa odwrotnie niż `break`.
Nie kończy pętli, ale pomija tylko bieżący krok i przechodzi do następnego.

To tak, jakbyś powiedział:

> „Tego przypadku nie chcę – idź dalej!”

```python
liczby = [3, -1, 7, -4, 5]

for liczba in liczby:
    if liczba < 0:
        continue
    print("Pozytywna liczba:", liczba)
```

### 🔍 Wyjaśnienie:

* Program pomija liczby ujemne (`continue`).
* Dla dodatnich wykonuje `print()`.
* Dzięki temu pętla działa selektywnie – przetwarza tylko dane, które nas interesują.

---

## 🧮 3. break i continue w pętli while

Obie instrukcje działają również w pętli `while`.
To szczególnie przydatne, gdy pętla działa na podstawie danych użytkownika lub zmieniających się warunków.\

```python
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    if i == 7:
        break
    print(i)
```

### 🔍 Wyjaśnienie:

* Zmienna `i` zwiększa się od 1 do 10.
* Gdy osiągnie 3 – `continue` pomija drukowanie.
* Gdy osiągnie 7 – `break` kończy pętlę.
* Efekt: program drukuje 1, 2, 4, 5, 6.

---

## 🧩 4. Mini projekt – filtr liczb od użytkownika

> Stwórz program, który pobiera liczby od użytkownika i przetwarza je w zależności od wartości.

```python
while True:
    liczba = int(input("Podaj liczbę: "))

    if liczba == 0:
        print("Koniec – wpisałeś 0.")
        break

    if liczba == 100:
        print("Liczba specjalna 100 – kończę program.")
        break

    if liczba < 0:
        print("Liczba ujemna – pomijam.")
        continue

    print("Liczba:", liczba)
```

### 🔍 Wyjaśnienie:

* Pętla działa w nieskończoność (`while True`).
* `break` przerywa program dla 0 lub 100.
* `continue` pomija liczby ujemne.
* Tylko liczby dodatnie są drukowane.

### 💡 Rozbudowana wersja – licznik i suma liczb dodatnich

Dodajmy licznik i sumę liczb dodatnich, aby pod koniec wyświetlić podsumowanie:

```python
licznik = 0
suma = 0

while True:
    liczba = int(input("Podaj liczbę: "))

    if liczba == 0:
        print("Koniec – wpisałeś 0.")
        break

    if liczba == 100:
        print("Liczba specjalna 100 – kończę program.")
        break

    if liczba < 0:
        print("Liczba ujemna – pomijam.")
        continue

    licznik += 1
    suma += liczba
    print("Liczba:", liczba)

print(f"\nWprowadziłeś {licznik} liczb dodatnich. Suma to {suma}.")
```

### 🔍 Wyjaśnienie:

* `licznik` zlicza liczby dodatnie.
* `suma` dodaje ich wartości.
* `break` kończy działanie programu.
* `continue` pomija niechciane dane.

### 🧠 Wniosek

To już całkiem praktyczny program!  
Łączy w sobie:

* pętle `while`,
* instrukcje `break` i `continue`,
* obsługę danych użytkownika,
* warunki i operacje arytmetyczne.

To jedne z fundamentów programowania – dzięki nim Twoje programy stają się elastyczne i inteligentne.  

---

## 🎉 Podsumowanie lekcji 13

* `break` – przerywa pętlę w dowolnym momencie.
* `continue` – pomija jeden krok i przechodzi dalej.
* Obie instrukcje dają Ci większą kontrolę nad przebiegiem programu.

Dzięki nim możesz tworzyć bardziej precyzyjne i efektywne rozwiązania.

© 2025 PotęgaIT – Kurs Python dla początkujących

---

