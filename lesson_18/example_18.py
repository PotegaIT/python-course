# Otwieramy plik "plik.txt" w trybie odczytu ("r") / Open the file "plik.txt" in read mode ("r")
dokument = open("plik.txt", "r") 

# Odczytujemy całą zawartość pliku jako jeden ciąg tekstowy / Read the entire content of the file as a single text string
zawartosc = dokument.read() 

# Wyświetlamy zawartość pliku w konsoli / Display the file content in the console
print(zawartosc) 

# Zamykamy plik (ważne, żeby zwolnić zasoby systemowe) / Close the file (important to free system resources)
dokument.close() 


# Lepszy sposób: użycie instrukcji with — plik zamknie się automatycznie / Better way: use "with" – the file will close automatically
with open("plik.txt", "r") as dokument: 
    # Czytamy całą zawartość pliku / Read the entire file content
    zawartosc = dokument.read() 
    # Wyświetlamy zawartość / Display the content
    print(zawartosc) 


# Tworzymy (lub nadpisujemy) plik "nowy_plik.txt" w trybie zapisu ("w") / Create (or overwrite) the file "nowy_plik.txt" in write mode ("w")
with open("nowy_plik.txt", "w") as dokument: 
    # Zapisujemy pierwszą linię tekstu / Write the first line of text
    dokument.write("Witaj w nowym pliku!\n") 
    # Zapisujemy drugą linię tekstu / Write the second line of text
    dokument.write("To druga linia tekstu.\n")  


# Otwieramy plik "nowy_plik.txt" w trybie dopisywania ("a") / Open the file "nowy_plik.txt" in append mode ("a")
with open("nowy_plik.txt", "a") as dokument: 
    # Dopisujemy kolejną linię na końcu pliku / Append another line at the end of the file
    dokument.write("Dopisujemy nowy wiersz.\n") 


# Tworzymy (lub nadpisujemy) plik "moje_zdania.txt" w trybie zapisu / Create (or overwrite) the file "moje_zdania.txt" in write mode
with open("moje_zdania.txt", "w") as plik: 
    # Pętla, która wykona się 3 razy / Loop that runs 3 times
    for i in range(3): 
        # Pobieramy od użytkownika zdanie (z numerem) / Ask the user to enter a sentence (with number)
        zdanie = input(f"Podaj zdanie nr {i + 1}: ") 
        # Zapisujemy zdanie do pliku i dodajemy znak nowej linii / Write the sentence to the file and add a newline
        plik.write(zdanie + "\n") 


# Informujemy użytkownika, że dane zostały zapisane / Inform the user that the data has been saved
print("Zdania zostały zapisane!") 
