a = 8
b = 4

# Podstawowe działania arytmetyczne / Basic arithmetic operations
print(f"Suma / Sum: {a + b}")         # dodawanie / addition
print(f"Różnica / Difference: {a - b}")      # odejmowanie / subtraction
print(f"Iloczyn / Product: {a * b}")      # mnożenie / multiplication
print(f"Iloraz / Quotient: {a / b}")       # dzielenie (wynik zawsze float) / division (result is always float)

# Operacje porównań i logiczne / Comparison and logical operations
print(f"Czy 'a' większe od 'b'? / Is 'a' greater than 'b'? {a > b}")          # porównanie / comparison
print(f"Czy 'a' jest podzielne przez 'b'? / Is 'a' divisible by 'b'? {a % b == 0}")  # sprawdzenie reszty / check remainder

# Operatory logiczne AND / Logical operators AND
print(f"a > 5 and b < 20: {a > 5 and b < 20}")   # True, oba warunki prawdziwe / both conditions are true
print(f"a > 10 and b < 20: {a > 10 and b < 20}")  # False, pierwszy warunek fałszywy / first condition is false

# Operatory logiczne OR / Logical operators OR
print(f"a < 5 or b > 2: {a < 5 or b > 2}")     # True, drugi warunek prawdziwy / second condition is true
print(f"a > 10 or b < 3: {a > 10 or b < 3}")    # False, oba warunki fałszywe / both conditions are false

# Operator logiczny NOT / Logical operator NOT
print(f"not a > 5: {not a > 5}")           # False, negacja a > 5 / negation of a > 5
print(f"not b < 3: {not b < 3}")           # True, negacja b < 3 / negation of b < 3
