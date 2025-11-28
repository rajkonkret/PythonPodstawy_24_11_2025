# REST API (Representational State Transfer) to styl
# architektury oprogramowania umożliwiający komunikację między różnymi systemami przez internet,
# np. między aplikacją mobilną a serwerem.
# Działa na zasadzie wysyłania żądań (requests)
# i otrzymywania odpowiedzi (responses) zazwyczaj w formacie JSON lub XML,
# co pozwala na dostęp do danych i zarządzanie nimi
# za pomocą standardowych metod HTTP (Create, Read, Update, Delete)
import requests

#  pip install requests
url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)
print(response)  # <Response [200]>
# 200 ok
# 3xx - warningi, przekierowanie
# 4xx, 404 - brak zasobu, 400 Bad Req
# 5xx - 500 Internal Server Error

print(response.text)

data = response.json()
print(data)
print(type(data))

for k in data:
    print(k)
# categories
# created_at
# icon_url
# id
# updated_at
# url
# value

print(data['value'])
# Life is like a box of chocolates. They are all for Chuck Norris.

# https://api.chucknorris.io/img/avatar/chuck-norris.png
response_img = requests.get(data['icon_url'])
with open('icon.png', "wb") as f:
    f.write(response_img.content)

print("Zdjęcie zostało zapisane.")
