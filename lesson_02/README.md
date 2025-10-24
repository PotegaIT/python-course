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


# Lesson 2: Installing and Setting Up the Environment (Windows/Linux/macOS)

## Introduction
Before we start writing code, we need to prepare the environment in which we will be working. In this lesson, I will show you how to install Python on different operating systems and how to set up a simple code editor or IDE that will help you write programs comfortably. This is a very important step – without it, Python will not work on your computer.

## Installing Python

### Windows:
Download the latest installer for Windows from [python.org](https://python.org).

⚠️ During the installation, it is very important to check the **Add Python to PATH** option – this allows you to run Python from any location.

### Linux (e.g., Ubuntu):
Python is usually pre-installed, but it is often a good idea to install a newer version or additional tools like pip.

You can do this via the terminal with the command:
```sh
sudo apt install python3 python3-pip
```

### macOS:
On a Mac, you can also download the installer from [python.org](https://python.org) or use Homebrew by typing in the terminal:

```sh
brew install python3
```
Make sure that pip is also installed.

**Check the version:**  
After installation, open the terminal (or CMD on Windows) and type:
```sh
python --version
```
or
```sh
python3 --version
```
## Choosing an Editor or IDE

To write code, we need a tool that makes our work easier – it highlights syntax, suggests errors, and allows us to run programs conveniently. Such a tool is a code editor or an IDE (Integrated Development Environment).

At the beginning, you can use the very simple [Thonny](https://thonny.org/) program, which is recommended for beginners – everything works immediately after installation, and the interface is very intuitive.

However, in this course we will be using [Visual Studio Code (VS Code)](https://code.visualstudio.com/) – a free, modern code editor that allows you to do much more. I use it every day, so all examples you will see in the course are written in VS Code.

Don't worry if VS Code seems a bit more complex at first – I will guide you step by step on how to use it.

### How to Install VS Code:

* Go to [code.visualstudio.com](https://code.visualstudio.com/)

* Download the version for your system (Windows, macOS, Linux)

* Install the program like any other application

After launching, install the Python extension (click the Extensions icon on the left, search for “Python”, click Install)

Once the editor is installed, you are ready to write your first Python code!

## Your First **.py File**

After setting up the environment, we can create our first **.py** file. Open a new file in your editor, save it as **hello.py**, and then write any code, for example:
```sh
print("Hello, Python!")
```
and run it.

## Summary

Congratulations! You have successfully set up your working environment. Now your computer is ready for Python programming. You know how to install Python, check its version, choose a suitable editor, and run your first .py file. This is the foundation on which we will build the rest of the course. You are ready for real programming!

