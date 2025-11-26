# {"name":"John", "age":30, "car":null}
#  {
#         "description": "Zmienna to miejsce w pami\u0119ci komputera, gdzie przechowywana jest warto\u015b\u0107. W Pythonie zmienna przypisywana jest do nazwy za pomoc\u0105 operatora `=`.",
#         "example": "nazwa = \"Python\"\nwiek = 30\nczy_aktywny = True",
#         "id": 1,
#         "level": "podstawowy",
#         "term": "Co to jest zmienna w Pythonie?"
#     },
# json - dane typu klucz-wartość
# popularny typ danych wymiany miedzy komputerami
# odpowiednikiem jsona w pythonie jest -> słownik

import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>

# zapis jako json
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f)
# {"name": "Radek", "age": 40, "czy_pali": null}

# beautify
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f, indent=4)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }


with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

# wczytanie do słownika
with open('nasze_dane.json', "r") as f:
    data = json.load(f)

print(data)
print(type(data))
# {'age': 40, 'czy_pali': None, 'name': 'Radek'}
# <class 'dict'>

print(data['name'])  # Radek

# zamiana słownika na tekst (json)
json_tekst = json.dumps(data)
print(json_tekst)  # {"age": 40, "czy_pali": null, "name": "Radek"}
print(type(json_tekst))  # <class 'str'>

# zamiana json na słownik
dict_json = json.loads(json_tekst)
print(dict_json)
print(type(dict_json))
resp = '''{"description": "Zmienna to miejsce w pami\u0119ci komputera, gdzie przechowywana jest warto\u015b\u0107. W Pythonie zmienna przypisywana jest do nazwy za pomoc\u0105 operatora `=`.", "example": "nazwa = \"Python\"\nwiek = 30\nczy_aktywny = True","id": 1,"level": "podstawowy","term": "Co to jest zmienna w Pythonie?"}'''

dane = json.loads(resp)
for i in dane:
    print(i)