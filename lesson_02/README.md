# Lekcja 2: Instalacja i konfiguracja środowiska (Windows/Linux/macOS)

## Wprowadzenie:
Zanim zaczniemy pisać kod, musimy przygotować środowisko, w którym będziemy pracować. W tej lekcji pokażę Ci, jak zainstalować Pythona na różnych systemach operacyjnych i jak skonfigurować prosty edytor kodu lub IDE, które pomoże Ci wygodnie pisać programy. To bardzo ważny krok – bez tego Python nie będzie działał na Twoim komputerze.

## Instalacja Pythona

### Windows:
Na stronie [python.org](https://python.org) pobieramy najnowszą wersję instalatora dla Windows.

⚠️ Podczas instalacji bardzo ważne jest, żeby zaznaczyć opcję Add Python to PATH – to umożliwi uruchamianie Pythona z dowolnego miejsca.

### Linux (np. Ubuntu):
Python jest domyślnie zainstalowany, ale często warto zainstalować nowszą wersję lub zainstalować dodatkowe narzędzia, np. pip.

Można to zrobić przez terminal komendą:
```sh
sudo apt install python3 python3-pip
```

### macOS:
Na Macu również możemy pobrać instalator ze strony [python.org](https://python.org) albo użyć Homebrew, wpisując w terminalu:

```sh 
brew install python3
```

Upewnij się, że masz też zainstalowany pip.

**Sprawdzenie wersji:**
Po instalacji otwieramy terminal (lub CMD na Windowsie) i wpisujemy:
```sh
python --version
```
lub
```sh
python3 --version
```

## Wybór edytora lub IDE

Do pisania kodu potrzebujemy narzędzia, które ułatwia pracę – koloruje składnię, podpowiada błędy i pozwala wygodnie uruchamiać programy. Takie narzędzie to edytor kodu albo IDE (zintegrowane środowisko programistyczne).

Na początek możesz skorzystać z bardzo prostego programu [Thonny](https://thonny.org/), który jest polecany dla początkujących – wszystko działa od razu po zainstalowaniu, a interfejs jest bardzo intuicyjny.

Jednak w tym kursie będziemy pracować w [Visual Studio Code (VS Code)](https://code.visualstudio.com/) – to darmowy, nowoczesny edytor kodu, który pozwala na znacznie więcej. Sam z niego korzystam na co dzień, dlatego wszystkie przykłady, które zobaczysz w kursie, będą pisane właśnie w VS Code.

Nie martw się, jeśli VS Code wydaje Ci się na początku trochę bardziej rozbudowany – krok po kroku pokażę Ci, jak z niego korzystać.

### Jak zainstalować VS Code:

* Wejdź na [code.visualstudio.com](https://code.visualstudio.com/)

* Pobierz wersję dla swojego systemu (Windows, macOS, Linux)

* Zainstaluj program jak każdą inną aplikację

Po uruchomieniu zainstaluj rozszerzenie Python (ikonka rozszerzeń po lewej stronie, wyszukaj “Python”, kliknij Install)

Po zainstalowaniu edytora jesteś gotowy do pisania swojego pierwszego kodu w Pythonie!

## Twój pierwszy **plik .py**

Po zainstalowaniu środowiska możemy stworzyć pierwszy plik z rozszerzeniem **.py**. W edytorze otwieramy nowy plik, zapisujemy go jako **hello.py**, a potem wpisujemy dowolny kod, np. 
```sh
print("Hello, Python!")
```
i uruchamiamy go.

## Podsumowanie

Gratulacje! Udało Ci się skonfigurować swoje środowisko pracy. Teraz Twój komputer jest gotowy do programowania w Pythonie. Umiesz zainstalować Pythona, wiesz jak sprawdzić wersję, wybrać odpowiedni edytor i uruchomić swój pierwszy plik .py. To fundament, na którym będziemy budować całą resztę. Jesteś gotowy na prawdziwe programowanie!
