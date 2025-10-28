# ===============================
# 📝 Komentarze / Comments
# ===============================

print("Hello, world!")  # wypisuje powitanie na ekranie / prints a greeting on the screen

# wypisuje powitanie na ekranie / prints a greeting on the screen
print("Hello, world!")

"""Wypisuje powitanie na ekranie. / Prints a greeting on the screen."""
print("Hello, world!")

# ===============================
# ❌ Złe praktyki / Bad practices
# ===============================

# Nieczytelne nazwy zmiennych / unclear variable names
x = 5
y = 10
z = x + y
print(z)  # wynik 15 / result 15

# Brak spacji i zbyt długie linie / no spaces, long line
a=5+10*2/3-4
print(a)  # wynik 7.666... / result 7.666...

# Brak komentarzy / no comments
print("Cześć")  # nikt nie wie, po co to jest / nobody knows why this is here

# ===============================
# ✅ Dobre praktyki / Good practices
# ===============================

# Czytelne nazwy zmiennych i funkcji / clear variable and function names
user_age = 25
total_score = 98
print(user_age, total_score)  # 25 98


# Rozdzielanie sekcji kodu pustymi liniami / separate code sections with blank lines
name = input("Jak masz na imię? ")  # What is your name?

print(f"Cześć, {name}!")  # Hi, {name}!
