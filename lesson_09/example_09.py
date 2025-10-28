# Tworzymy listę owoców / Creating a list of fruits
owoce = ["jablko", "banan", "gruszka"]
print("Lista owoców:", owoce)  # Lista owoców / List of fruits

# Dodajemy nowy owoc na koniec listy / Adding a new fruit to the end of the list
owoce.append("sliwka")
print("Po dodaniu śliwki:", owoce)  # Po dodaniu śliwki / After adding plum

# Usuwamy konkretny element 'banan' z listy / Removing a specific element 'banana' from the list
owoce.remove("banan")
print("Po usunięciu banana:", owoce)  # Po usunięciu banana / After removing banana

# Usuwamy i zwracamy ostatni element listy (pop) / Remove and return the last element (pop)
ostatni = owoce.pop()
print("Usunięto:", ostatni)  # Usunięto / Removed
print("Lista po usunięciu ostatniego elementu:", owoce)  # Lista po usunięciu ostatniego elementu / List after removing the last element

# Usuwamy i zwracamy pierwszy element (indeks 0) / Remove and return the first element (index 0)
pierwszy = owoce.pop(0)
print("Usunięto pierwszy element:", pierwszy)  # Usunięto pierwszy element / Removed first element
print("Lista po usunięciu pierwszego elementu:", owoce)  # Lista po usunięciu pierwszego elementu / List after removing first element

print()

# Ponownie tworzymy listę owoców, by pokazać dostęp po indeksie i modyfikację / Re-create the fruit list to show indexing and modification
owoce = ["jablko", "banan", "gruszka"]
print("Nowa lista owoców:", owoce)  # Nowa lista owoców / New list of fruits

# Dostęp do elementu przez indeks / Access an element by index
drugi_owoc = owoce[2]
print("Trzeci owoc na liście to:", drugi_owoc)  # Trzeci owoc na liście / Third fruit in the list

# Modyfikujemy drugi element listy / Modifying the second element in the list
owoce[1] = "kiwi"
print("Po zmianie drugiego owocu:", owoce)  # Po zmianie drugiego owocu / After changing the second fruit

# Dostęp do ostatniego elementu przez indeks ujemny / Access the last element using negative index
ostatni = owoce[-1]
print("Ostatni owoc to:", ostatni)  # Ostatni owoc / Last fruit

# Długość listy / Length of the list
print("Liczba owoców:", len(owoce))  # Liczba owoców / Number of fruits

print()

# Tworzymy pustą listę potraw / Creating an empty list of dishes
potrawy = []

# Dodajemy potrawy podane przez użytkownika / Adding dishes entered by the user
potrawy.append(input("Podaj 1. potrawę: "))  # Podaj 1. potrawę / Enter dish 1
potrawy.append(input("Podaj 2. potrawę: "))  # Podaj 2. potrawę / Enter dish 2
potrawy.append(input("Podaj 3. potrawę: "))  # Podaj 3. potrawę / Enter dish 3

# Wyświetlamy wprowadzone potrawy oraz ich liczbę / Print the entered dishes and their count
print("Twoje ulubione potrawy:", potrawy)  # Twoje ulubione potrawy / Your favorite dishes
print("Liczba potraw:", len(potrawy))  # Liczba potraw / Number of dishes
