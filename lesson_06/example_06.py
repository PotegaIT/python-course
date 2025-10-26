a = 8
b = 4

# Podstawowe działania arytmetyczne / Basic arithmetic operations
print(f"Suma: {a + b}")         # dodawanie / addition
print(f"Różnica: {a - b}")      # odejmowanie / subtraction
print(f"Iloczyn: {a * b}")      # mnożenie / multiplication
print(f"Iloraz: {a / b}")       # dzielenie (wynik zawsze float) / division (result is always float)

# Operacje porównań i logiczne / Comparison and logical operations
print(f"Czy 'a' większe od 'b'? {a > b}")          # porównanie: czy a jest większe od b? / comparison: is a greater than b?
print(f"Czy 'a' jest podzielne przez 'b'? {a % b == 0}")  # sprawdzenie, czy a jest podzielne przez b (reszta == 0) / check if a is divisible by b (remainder == 0)

# Operatory logiczne AND / Logical operators AND
print(a > 5 and b < 20)   # True, bo oba warunki są prawdziwe / True, because both conditions are true
print(a > 10 and b < 20)  # False, bo pierwszy warunek jest fałszywy / False, because the first condition is false

# Operatory logiczne OR / Logical operators OR
print(a < 5 or b > 2)     # True, bo drugi warunek jest prawdziwy / True, because the second condition is true
print(a > 10 or b < 3)    # False, oba warunki fałszywe / False, both conditions are false

# Operator logiczny NOT / Logical operator NOT
print(not a > 5)           # False, bo a > 5 jest True, więc NOT True → False / False, because a > 5 is True, so NOT True → False
print(not b < 3)           # True, bo b < 3 jest False, więc NOT False → True / True, because b < 3 is False, so NOT False → True
