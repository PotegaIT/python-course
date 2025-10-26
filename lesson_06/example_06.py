a = 8
b = 4

# Podstawowe działania arytmetyczne / Basic arithmetic operations
print(f"Suma / Sum: {a + b}")
print(f"Różnica / Difference: {a - b}")
print(f"Iloczyn / Product: {a * b}")
print(f"Iloraz / Quotient: {a / b}")  # wynik zawsze float / result is always float

# Operacje porównań i logiczne / Comparison and logical operations
print(f"Czy 'a' większe od 'b'? / Is 'a' greater than 'b'? {a > b}")
print(f"Czy 'a' jest podzielne przez 'b'? / Is 'a' divisible by 'b'? {a % b == 0}")

# Operatory logiczne AND / Logical operators AND
print(f"a > 5 and b < 20: {a > 5 and b < 20}  # oba warunki prawdziwe / both conditions are true")
print(f"a > 10 and b < 20: {a > 10 and b < 20}  # pierwszy warunek fałszywy / first condition is false")

# Operatory logiczne OR / Logical operators OR
print(f"a < 5 or b > 2: {a < 5 or b > 2}  # drugi warunek prawdziwy / second condition is true")
print(f"a > 10 or b < 3: {a > 10 or b < 3}  # oba warunki fałszywe / both conditions are false")

# Operator logiczny NOT / Logical operator NOT
print(f"not a > 5: {not a > 5}  # negacja a > 5 / negation of a > 5")
print(f"not b < 3: {not b < 3}  # negacja b < 3 / negation of b < 3")
