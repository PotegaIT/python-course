# Lista liczb od 1 do 5 / List of numbers from 1 to 5
liczby = [1, 2, 3, 4, 5]

# Tworzymy nową listę – kwadraty liczb z poprzedniej listy / Create a new list – squares of numbers from the previous list
kwadraty = [x * x for x in liczby]  # List comprehension (szybki sposób tworzenia listy) / List comprehension (quick way to create a list)
print(kwadraty)  # [1, 4, 9, 16, 25] / Output: [1, 4, 9, 16, 25]


# Lista liczb od 1 do 6 / List of numbers from 1 to 6
liczby = [1, 2, 3, 4, 5, 6]

# Tworzymy listę zawierającą tylko liczby parzyste z listy 'liczby' / Create a list containing only even numbers from the 'numbers' list
parzyste = [x for x in liczby if x % 2 == 0]  # x % 2 == 0 oznacza liczby podzielne przez 2 / x % 2 == 0 means numbers divisible by 2
print(parzyste)  # [2, 4, 6] / Output: [2, 4, 6]


# Lista owoców zapisanych małymi literami / List of fruits in lowercase
owoce = ["jablko", "banan", "gruszka"]

# Tworzymy nową listę, gdzie każdy owoc jest zapisany wielkimi literami / Create a new list where each fruit is in uppercase
duze_litery = [owoc.upper() for owoc in owoce]  # upper() zamienia tekst na wielkie litery / upper() converts text to uppercase
print(duze_litery)  # ['JABLKO', 'BANAN', 'GRUSZKA'] / Output: ['APPLE', 'BANANA', 'PEAR']


# Tworzymy pustą listę, do której zapiszemy liczby podane przez użytkownika / Create an empty list to store numbers provided by the user
liczby = []

# Pętla 5 razy prosi użytkownika o podanie liczby / Loop asks the user for a number 5 times
for i in range(5):
    liczba = int(input(f"Podaj liczbe nr {i+1}: "))  # Pobieramy liczbę i zamieniamy ją na typ int / Get number from user and convert it to int
    liczby.append(liczba)  # Dodajemy liczbę do listy 'liczby' / Add the number to the 'numbers' list

# Tworzymy nową listę, zawierającą tylko liczby większe niż 10 / Create a new list containing only numbers greater than 10
wieksze_niz_10 = [x for x in liczby if x > 10]  # Filtrowanie liczb większych niż 10 / Filter numbers greater than 10

# Wyświetlamy wynik / Display the result
print("Liczby wieksze niz 10:")  # Numbers greater than 10:
print(wieksze_niz_10)  # Wyświetlamy nową listę / Print the new list
