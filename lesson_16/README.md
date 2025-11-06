## 🇵🇱 Wersja polska

# 🧠 Lekcja 16 – Domyślne wartości argumentów

---

## 🎯 Cel lekcji

W tej lekcji dowiesz się, jak korzystać z **domyślnych wartości argumentów w funkcjach Pythona**.  
Dzięki nim funkcje mogą działać nawet wtedy, gdy nie podasz wszystkich danych, co pozwala tworzyć bardziej elastyczny i przejrzysty kod.

---

## 📝 1. Co to jest domyślny argument?

Czasami chcemy, aby funkcja miała parametr, ale nie był on obowiązkowy.  
Wtedy możemy nadać mu wartość domyślną.

```python
def przywitaj(imie="Gościu"):
    print("Cześć,", imie)

przywitaj()        # użyje domyślnej wartości
przywitaj("Ania")  # nadpisze domyślną wartość
```

### 🔍 Wyjaśnienie:

* arametr `imie` ma domyślną wartość `"Gościu"`.
* Jeśli wywołamy funkcję bez podania imienia, użyta zostanie wartość domyślna.
* Jeśli podamy argument, np. `"Ania"`, funkcja użyje przekazanej wartości.

---

## 📝 2. Wiele domyślnych wartości

Można ustawić domyślne wartości dla wielu parametrów i łączyć je z parametrami obowiązkowymi.
Pamiętaj: parametry domyślne zawsze powinny być na końcu listy parametrów.

```python
def przywitaj(imie="Gościu", jezyk="polski"):
    if jezyk == "angielski":
        print("Hello,", imie)
    else:
        print("Cześć,", imie)

przywitaj()
przywitaj("Anna")
przywitaj("Tom", "angielski")
```

### 🔍 Wyjaśnienie:

* Parametry `imie` i `jezyk` mają wartości domyślne.
* Funkcja działa nawet bez podania żadnych argumentów.
* Możemy nadpisać tylko jeden parametr lub oba jednocześnie.

🛑 **Uwaga:** Python nie pozwala na umieszczanie parametru bez domyślnej wartości po tych z wartością domyślną — spowoduje to błąd.

---

## 🧩 3. Mini projekt: Funkcja generująca powitanie

Tworzymy funkcję, która generuje powitanie w różnych językach, z możliwością podania imienia.

```python
def powitanie(imie="Przyjaciel", jezyk="polski"):
    if jezyk == "angielski":
        return f"Hello, {imie}!"
    elif jezyk == "hiszpański":
        return f"¡Hola, {imie}!"
    else:
        return f"Cześć, {imie}!"

print(powitanie())
print(powitanie("Anna"))
print(powitanie("Carlos", "hiszpański"))
print(powitanie(jezyk="angielski"))
```

### 🔍 Wyjaśnienie:

* Funkcja `powitanie` przyjmuje dwa parametry z domyślnymi wartościami.
* Można wywołać ją bez argumentów, z jednym argumentem lub z oboma.
* Python automatycznie dopasuje wywołanie funkcji do podanych wartości.

---

## 🎉 Podsumowanie lekcji 16

* domyślne wartości parametrów sprawiają, że funkcje są bardziej elastyczne.
* Jedna funkcja może obsłużyć wiele przypadków bez konieczności pisania dodatkowych warunków.
* Dzięki temu kod staje się bardziej czytelny i łatwiejszy do utrzymania.
* Warto korzystać z domyślnych argumentów wszędzie tam, gdzie dany parametr nie musi być zawsze wymagany.

© 2025 PotęgaIT – Kurs Python dla początkujących

---

## 🇬🇧 English Version

# 🧠 Lesson 16 – Default Argument Values

---

## 🎯 Lesson Goal

In this lesson, you will learn how to use **default argument values in Python functions**.  
They allow functions to work even if not all data is provided, making your code more flexible and readable.

---

## 📝 1. What is a default argument?

Sometimes we want a function to have a parameter, but it shouldn't be mandatory.  
In that case, we can assign it a default value.

```python
def greet(name="Guest"):
    print("Hello,", name)

greet()        # will use the default value
greet("Anna")  # overrides the default value
```

### 🔍 Explanation:

* The parameter `name` has a default value `"Guest"`.
* If we call the function without providing a name, the default value is used.
* If we provide an argument, e.g. `"Anna"`, the function will use the provided value.

---

## 📝 2. Multiple default values

You can set default values for more than one parameter and combine them with required parameters.
Remember: default parameters should always come **after** required ones.

```python
def greet(name="Guest", language="polish"):
    if language == "english":
        print("Hello,", name)
    else:
        print("Cześć,", name)

greet()
greet("Anna")
greet("Tom", "english")
```

### 🔍 Explanation:

* Both `name` and `language` have default values.
* The function works even without providing any arguments.
* You can override just one parameter or both at the same time.

🛑 **Note:** Python does not allow placing a non-default parameter after parameters with default values — it will raise an error.

---

## 🧩 3. Mini Project: Greeting Function

Let's create a function that generates greetings in different languages, with an optional name.

```python
def greeting(name="Friend", language="polish"):
    if language == "english":
        return f"Hello, {name}!"
    elif language == "spanish":
        return f"¡Hola, {name}!"
    else:
        return f"Cześć, {name}!"

print(greeting())
print(greeting("Anna"))
print(greeting("Carlos", "spanish"))
print(greeting(language="english"))
```

### 🔍 Explanation:

* The function greeting takes two parameters with default values.
* You can call it without arguments, with one argument, or with both.
* Python automatically matches the function call to the provided values.

---

## 🎉 Lesson 16 Summary

* Default parameter values make functions more flexible.
* One function can handle multiple cases without writing additional conditions.
* This improves code readability and maintainability.
* Use default arguments whenever a parameter does not need to be mandatory.

© 2025 PotęgaIT – Python for Beginners Course
