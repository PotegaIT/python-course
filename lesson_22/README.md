## 🇵🇱 Wersja polska

# 🛠 Lekcja 22: Instalowanie bibliotek przez pip + virtualenv

---

## 🎯 Cel lekcji

W tej lekcji poznasz, jak **instalować zewnętrzne biblioteki w Pythonie** przy użyciu `pip` oraz jak **tworzyć i zarządzać wirtualnymi środowiskami** za pomocą `virtualenv`.  
Dzięki temu każdy projekt może mieć własne zależności i wersje pakietów – bez konfliktów między projektami.

---

## 📝 1. Co to jest pip?

`pip` to narzędzie pozwalające na instalowanie bibliotek z internetu, dokładnie z **PyPI (Python Package Index)**.  
Dzięki temu możesz rozszerzyć możliwości Pythona o gotowe funkcje i moduły.

### Przykład instalacji:

```bash
pip install requests
```

Po zainstalowaniu możesz używać biblioteki w kodzie:

```python
import requests

response = requests.get("https://potegait.com")
print("Kod odpowiedzi HTTP:", response.status_code)
```

* Jeżeli otrzymasz kod `200` – wszystko działa poprawnie.
* Właśnie użyłeś zewnętrznej biblioteki w Pythonie!

---

## 📝 2. Zarządzanie bibliotekami

### Sprawdzanie zainstalowanych pakietów:

```bash
pip list
```

### Usuwanie pakietów:

```bash
pip uninstall requests
```

* Dzięki temu możesz łatwo kontrolować środowisko i usuwać niepotrzebne paczki.

---

## 📝 3. Czym jest virtualenv?

`virtualenv` pozwala tworzyć **osobne środowiska Python** dla różnych projektów.
Dzięki temu możesz mieć różne wersje tych samych bibliotek bez konfliktów.

### Instalacja virtualenv:

```bash
pip install virtualenv
```

### Tworzenie środowiska:

```bash
virtualenv venv
```

### Aktywacja środowiska:

* Windows:

```bash
venv\Scripts\activate
```

* macOS/Linux:

```bash
source venv/bin/activate
```

### Dezaktywacja środowiska:

```bash
deactivate
```

* Po aktywacji każda zainstalowana paczka trafia tylko do tego środowiska.
* Profesjonalni programiści zawsze używają wirtualnych środowisk w większych projektach.

> 💡 Dygresja: Od Pythona 3.3 istnieje wbudowane narzędzie `venv`, które działa podobnie, ale `virtualenv` jest bardziej elastyczne i częściej spotykane w firmach.

---

## 📝 4. Zadanie praktyczne 1: ASCII Art

### Instalacja paczki:

```bash
pip install pyfiglet
```

### Przykład użycia:

```python
import pyfiglet

napis = pyfiglet.figlet_format("Python!")
print(napis)
```

## 📝 5. Zadanie praktyczne 2

### Instalacja paczki emoji:

```bash
pip install emoji
```

### Przykład użycia:

```python
import emoji

print(emoji.emojize("Python to jest :thumbs_up:", language="alias"))
```

* Zadanie pokazuje, jak znaleźć dokumentację i użyć paczki do własnych celów.

---

## 📝 6. Ciekawostka

* Niektóre biblioteki mają **zależności** – czyli inne paczki, które są wymagane do działania.
* `pip` instaluje je automatycznie, ale w środowisku globalnym może dojść do konfliktów – kolejny powód do stosowania `virtualenv`.

---

## ✅ Podsumowanie

W tej lekcji nauczyłeś się:

* Instalować zewnętrzne biblioteki za pomocą pip,
* Sprawdzać i usuwać pakiety,
* Tworzyć wirtualne środowiska za pomocą virtualenv,
* Aktywować i dezaktywować środowiska projektowe.

Dzięki tym narzędziom Twoje środowisko pracy będzie **czyste, uporządkowane i gotowe do rozwijania projektów**.
Możesz teraz korzystać z mocy społeczności Pythona i wzbogacać swoje aplikacje o gotowe funkcjonalności.

© 2025 PotęgaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version

# 🛠 Lesson 22: Installing Libraries with pip + virtualenv

---

## 🎯 Lesson Goal

In this lesson, you will learn how to **install external Python libraries** using `pip` and how to **create and manage virtual environments** using `virtualenv`.  
This allows each project to have its own dependencies and library versions – without conflicts between projects.

---

## 📝 1. What is pip?

`pip` is a tool for installing libraries from the internet, specifically from **PyPI (Python Package Index)**.  
It allows you to extend Python with ready-made functions and modules.

### Installation example:

```bash
pip install requests
```

After installation, you can use the library in your code:

```python
import requests

response = requests.get("https://potegait.com")
print("HTTP response code:", response.status_code)
```

* If you get code `200` – everything works correctly.
* You just used an external library in Python!

---

## 📝 2. Managing libraries

### List installed packages:

```bash
pip list
```

### Uninstall a package:

```bash
pip uninstall requests
```

* This allows you to easily control your environment and remove unnecessary packages.

---

## 📝 3. What is virtualenv?

`virtualenv` allows you to create **separate Python environments** for different projects.
This way, you can have different versions of the same libraries without conflicts.

### Install virtualenv:

```bash
pip install virtualenv
```

### Create an environment:

```bash
virtualenv venv
```

### Activate the environment:

* Windows:

```bash
venv\Scripts\activate
```

* macOS/Linux:

```bash
source venv/bin/activate
```

### Deactivate the environment:

```bash
deactivate
```

* After activation, every installed package goes **only to this environment**.
* Professional developers always use virtual environments for larger projects.

> 💡 Note: Since Python 3.3, there is a built-in `venv` tool that works similarly, but `virtualenv` is more flexible and commonly used in companies.

---

## 📝 4. Practical Exercise 1: ASCII Art

### Install the package:

```python
pip install pyfiglet
```

### Example usage:

```python
import pyfiglet

text = pyfiglet.figlet_format("Python!")
print(text)
```

---

## 📝 5. Practical Exercise 2

### Install the emoji package:

```bash
pip install emoji
```

### Example usage:

```python
import emoji

print(emoji.emojize("Python is :thumbs_up:", language="alias"))
```

* This exercise shows how to find documentation and use a package for your own projects.

---

## 📝 6. Fun Fact

* Some libraries have dependencies – other packages they need to work.
* `pip` installs them automatically, but in a global environment conflicts can happen – another reason to use `virtualenv`.

---

## ✅ Summary

In this lesson, you learned how to:

* Install external libraries using pip,
* List and uninstall packages,
* Create virtual environments using virtualenv,
* Activate and deactivate project-specific environments.

With these tools, your workspace will be **clean, organized, and ready for development**.
Now you can leverage the Python community’s resources and enhance your applications with ready-made functionality.

© 2025 PotegaIT – Python for Beginners Course

