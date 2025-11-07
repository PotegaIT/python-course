import requests  # Importuje bibliotekę requests do wykonywania żądań HTTP / Imports the requests library to perform HTTP requests

# Wykonanie żądania GET na stronę potegait.com / Perform a GET request to the potegait.com website
response = requests.get("https://potegait.com")

# Wyświetlenie kodu odpowiedzi HTTP / Print the HTTP response code
print("Kod odpowiedzi HTTP:", response.status_code)  # Jeśli 200 -> wszystko działa poprawnie / If 200 -> everything works correctly
