# Prosty menedżer zadań (TODO CLI)
# Simple Task Manager (TODO CLI)

# ---------------------------------------------------------------
# Funkcja dodaje nowe zadanie do listy.
# The function adds a new task to the list.
def dodaj_zadanie(zadania, nowe_zadanie):
    zadania.append(nowe_zadanie)  # Dodaj nowe zadanie na koniec listy / Add the new task to the end of the list


# ---------------------------------------------------------------
# Funkcja wyświetla wszystkie zadania z listy.
# The function displays all tasks from the list.
def pokaz_zadania(zadania):
    if not zadania:  # Jeśli lista jest pusta / If the list is empty
        print("Brak zadan na liscie.")  # Komunikat o braku zadań / Message when there are no tasks
    else:
        print("Lista zadan:")  # Nagłówek listy zadań / Tasks list header
        for idx, zadanie in enumerate(zadania, start=1):  # enumerate() numeruje zadania od 1 / enumerate() numbers tasks starting from 1
            print(f"{idx}. {zadanie}")  # Wyświetl numer i treść zadania / Print the task number and its content


# ---------------------------------------------------------------
# Funkcja usuwa zadanie o podanym numerze.
# The function deletes a task with the given number.
def usun_zadanie(zadania, numer):
    if 0 < numer <= len(zadania):  # Sprawdź, czy numer mieści się w zakresie / Check if the number is within valid range
        zadania.pop(numer - 1)  # Usuń zadanie z listy (indeksy zaczynają się od 0) / Remove task (indexes start at 0)
        print("Zadanie zostalo usuniete.")  # Potwierdzenie / Confirmation message
    else:
        print("Niepoprawny numer zadania.")  # Błąd, jeśli numer nie istnieje / Error if the task number doesn’t exist


# ---------------------------------------------------------------
# Funkcja zapisuje wszystkie zadania do pliku tekstowego.
# The function saves all tasks to a text file.
def zapisz_zadania(zadania, sciezka):
    # Otwieramy plik w trybie zapisu ('w') i kodowaniu UTF-8 / Open file in write mode with UTF-8 encoding
    with open(sciezka, 'w', encoding='utf-8') as plik:
        for zadanie in zadania:  # Dla każdego zadania w liście / For each task in the list
            plik.write(zadanie + '\n')  # Zapisz treść zadania w nowej linii / Write task to a new line


# ---------------------------------------------------------------
# Funkcja wczytuje zadania z pliku tekstowego (jeśli istnieje).
# The function loads tasks from a text file (if it exists).
def wczytaj_zadania(sciezka):
    try:
        # Otwieramy plik w trybie odczytu ('r') / Open file in read mode
        with open(sciezka, 'r', encoding='utf-8') as plik:
            # Każda linia to jedno zadanie; usuwamy znaki nowej linii / Each line is a task; strip newline characters
            return [linia.strip() for linia in plik]
    except FileNotFoundError:
        # Jeśli plik nie istnieje, zwróć pustą listę / If file doesn’t exist, return an empty list
        return []


# ---------------------------------------------------------------
# Główna funkcja programu – zawiera menu i logikę działania.
# The main function of the program – contains the menu and logic.
def main():
    sciezka = "zadania.txt"  # Nazwa pliku, w którym przechowujemy zadania / Name of the file where tasks are stored
    zadania = wczytaj_zadania(sciezka)  # Wczytaj istniejące zadania / Load existing tasks

    # Główna pętla programu – działa aż użytkownik wybierze "zapisz i zakończ"
    # Main program loop – runs until the user chooses "save and exit"
    while True:
        print("\n--- MENU ---")
        print("1. Pokaz zadania")       # Show tasks
        print("2. Dodaj zadanie")       # Add a new task
        print("3. Usun zadanie")        # Delete a task
        print("4. Zapisz i zakoncz")    # Save and exit

        wybor = input("Wybierz opcje: ")  # Pobierz wybór użytkownika / Get user’s choice

        if wybor == "1":
            pokaz_zadania(zadania)  # Wyświetl listę zadań / Display the list of tasks

        elif wybor == "2":
            nowe = input("Podaj tresc nowego zadania: ")  # Pobierz treść zadania / Ask for new task text
            dodaj_zadanie(zadania, nowe)  # Dodaj zadanie do listy / Add the task to the list

        elif wybor == "3":
            pokaz_zadania(zadania)  # Najpierw pokaż listę zadań / Show the list first
            try:
                numer = int(input("Podaj numer zadania do usuniecia: "))  # Pobierz numer zadania / Get task number
                usun_zadanie(zadania, numer)  # Usuń wskazane zadanie / Delete selected task
            except ValueError:
                print("Musisz podac numer.")  # Obsługa błędu przy złym typie danych / Handle wrong input type

        elif wybor == "4":
            zapisz_zadania(zadania, sciezka)  # Zapisz wszystkie zadania do pliku / Save all tasks to file
            print("Zadania zapisane. Do zobaczenia!")  # Komunikat końcowy / Exit message
            break  # Zakończ działanie programu / End the program

        else:
            print("Niepoprawny wybor. Sprobuj ponownie.")  # Obsługa błędnego wyboru / Handle invalid menu option


# ---------------------------------------------------------------
# Punkt wejścia programu – uruchamia main() tylko przy bezpośrednim uruchomieniu pliku.
# Program entry point – runs main() only when the file is executed directly.
if __name__ == "__main__":
    main()
