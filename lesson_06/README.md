# 🧮 Lekcja 6: Operatory arytmetyczne i logiczne

W tej lekcji poznasz coś, bez czego żaden język programowania się nie obejdzie – **operatory**.  
To dzięki nim program potrafi **liczyć, porównywać i podejmować decyzje**.  
Dowiesz się:
- jak w Pythonie działa dodawanie, odejmowanie, mnożenie czy dzielenie,  
- jak sprawdzać warunki (np. czy coś jest większe od czegoś),  
- oraz jak łączyć różne warunki za pomocą operatorów logicznych.

---

## 🔹 1. Operatory arytmetyczne

Operatory arytmetyczne służą do wykonywania **podstawowych działań matematycznych**.  
Działają na liczbach (`int` i `float`), a wynik również jest liczbą.

| Operator | Opis | Przykład | Wynik |
|-----------|------|-----------|-------|
| `+` | dodawanie | `10 + 3` | `13` |
| `-` | odejmowanie | `10 - 3` | `7` |
| `*` | mnożenie | `10 * 3` | `30` |
| `/` | dzielenie (zawsze float) | `10 / 3` | `3.333...` |
| `//` | dzielenie całkowite | `10 // 3` | `3` |
| `%` | reszta z dzielenia | `10 % 3` | `1` |
| `**` | potęgowanie | `10 ** 3` | `1000` |

### 📘 Przykład:
```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

## 2. Operatory porównań i logiczne

### 🔸 Operatory porównań

Pozwalają sprawdzić, czy dwie wartości są **równe, różne, większe lub mniejsze**.  
Zwracają wartość logiczną (`True` lub `False`).

| Operator | Opis | Przykład | Wynik |
|-----------|------|-----------|-------|
| `==` | równość | `5 == 5` | `True` |
| `!=` | nierówność | `5 != 3` | `True` |
| `>` | większe niż | `5 > 3` | `True` |
| `<` | mniejsze niż | `5 < 3` | `False` |
| `>=` | większe lub równe | `5 >= 5` | `True` |
| `<=` | mniejsze lub równe | `3 <= 5` | `True` |

### 📘 Przykład:
```sh
x = 5
y = 10

print(x == y)      # False
print(x < y)       # True
print(x != y)      # True
```
### 🔸 Operatory logiczne

Pozwalają łączyć różne warunki w jedną całość.
Używamy ich np. przy sprawdzaniu, czy dwa warunki są prawdziwe jednocześnie.

| Operator | Opis                                       | Przykład             | Wynik   |
| -------- | ------------------------------------------ | -------------------- | ------- |
| `and`    | oba warunki muszą być prawdziwe            | `(x < 10 and y > 5)` | `True`  |
| `or`     | wystarczy, że jeden warunek jest prawdziwy | `(x > 10 or y > 5)`  | `True`  |
| `not`    | odwraca wartość logiczną                   | `not x > 3`          | `False` |

### 📘 Przykład:
```sh
x = 5
y = 10

print(x < 10 and y > 5)   # True
print(x > 10 or y > 5)    # True
print(not x > 3)          # False
```

## 💡 3. Mini projekt – Prosty kalkulator i warunki

Zróbmy coś praktycznego — mały kalkulator, który wykona kilka działań i sprawdzi warunki logiczne.
```sh
a = 8
b = 4

print(f"Suma: {a + b}")
print(f"Różnica: {a - b}")
print(f"Iloczyn: {a * b}")
print(f"Iloraz: {a / b}")

print(f"Czy a większe od b? {a > b}")
print(f"Czy a jest podzielne przez b? {a % b == 0}")
```
### 🔍 Co tu się dzieje?

* a - b → różnica,

* a * b → iloczyn,

* a / b → iloraz (wynik zawsze float),

* operator % sprawdza resztę z dzielenia. Jeśli reszta to 0, liczba jest podzielna przez drugą.

## 🧠 4. Operatory logiczne – w praktyce

Przyjrzyjmy się dokładniej operatorom and, or, not:
```sh
a = 8
b = 4

print(a > 5 and b < 20)
print(a > 10 and b < 20)

print(a < 5 or b > 2)
print(a > 10 or b < 3)

print(not a > 5)
print(not b < 3)
```
#### Wyjaśnienie krok po kroku:

| Kod                 | Wynik   | Dlaczego                                    |
| ------------------- | ------- | ------------------------------------------- |
| `a > 5 and b < 20`  | `True`  | oba warunki prawdziwe                       |
| `a > 10 and b < 20` | `False` | pierwszy fałszywy                           |
| `a < 5 or b > 2`    | `True`  | drugi warunek prawdziwy                     |
| `a > 10 or b < 3`   | `False` | oba fałszywe                                |
| `not a > 5`         | `False` | `a > 5` to `True`, więc `not True → False`  |
| `not b < 3`         | `True`  | `b < 3` to `False`, więc `not False → True` |

## ✅ Podsumowanie

Dziś nauczyłeś się:

* korzystać z operatorów arytmetycznych,

* wykonywać podstawowe działania matematyczne,

* raz używać operatorów logicznych, które pozwalają łączyć warunki.

To fundament każdego programu — dzięki temu komputer potrafi analizować dane i podejmować decyzje.
