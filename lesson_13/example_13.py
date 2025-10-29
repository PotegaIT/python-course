# Pętla for – liczby od 0 do 9 (range(10) to 0...9) / For loop – numbers from 0 to 9 (range(10) means 0...9)
for liczba in range(10):  
    if liczba == 5:  # Jeśli liczba równa 5 / If the number equals 5
        print("Znaleziono 5! Koncze.")  # Wyświetlamy komunikat / Display a message
        break  # Przerywamy działanie pętli / Stop the loop immediately
    print("Sprawdzam:", liczba)  # Wypisujemy sprawdzaną liczbę (dopóki nie natrafimy na 5) / Print the current number (until we reach 5)


liczby = [3, -1, 7, -4, 5]
for liczba in liczby:
    if liczba < 0:
        continue  # Pomijamy liczby ujemne / Skip negative numbers
    print("Pozytywna liczba:", liczba)  # / Positive number

i = 0
while i < 10:
    i += 1
    if i == 3:
        continue  # Pomijamy 3 / Skip number 3
    if i == 7:
        break  # Kończymy pętlę / End the loop
    print(i)
