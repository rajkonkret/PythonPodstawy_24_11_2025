# słownik - para klucz - wartość
# {"user" :"Radek", "wiek":35}
# odpowiednik jsona
# klucze nie mogą się powtarzać

# pusty słownik
dictionary = {}
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dictionary_1 = dict()
print(dictionary_1)  # {}
print(type(dictionary_1))  # <class 'dict'>

# dodanie elementu do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 45
print(dictionary)  # {'imie': 'Radek', 'wiek': 45}

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Radek', 45])
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', 45)])

dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 45}

# wypisanie wartości dla klucza
print(dictionary['imie'])  # Tomek

dictionary['imie'] = ["Radek", "Tomek", "Magda"]
print(dictionary)  # {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 45}
print(dictionary['imie'])  # ['Radek', 'Tomek', 'Magda']
print(dictionary['imie'][0])  # Radek

# print(dictionary["Imie"])  # KeyError: 'Imie'
print(dictionary["Imie".lower()])  # ['Radek', 'Tomek', 'Magda']

print(dictionary.get("Imie"))  # None
print(dictionary.get("Imie", "default"))  # default

name1 = "GROSS"
name2 = "groß"

print(name1.lower() == name2.lower())  # False
# """ Return a version of the string suitable for caseless comparisons. """
print(name1.casefold() == name2.casefold())  # True

dictionary.update({"data": "12-12-2050"})
print(dictionary)
# {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 45, 'data': '12-12-2050'}

dict_small = {'x': 2}
dict_small.update([("y", 3), ("z", 8)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 8}

# # input() - pozwala wprowadzic dane np.: klawiatury
# zwraca stringa
# tekst = input("Podaj imię:")
# print(tekst)
# # Podaj imię:Radek
# # Radek

# # napisać aplikację kalkulator
# a = int(input("Podaj pierwszą liczbę:"))
# b = input("Podaj drugą liczbę:")
# print(a + float(b))
# print(int(a) + float(b))
# # Podaj pierwszą liczbę:2
# # Podaj drugą liczbę:4
# # 6.0


# napisac apliakcje słownik pol-ang
pol_ang = {'pies': 'dog', "kot": 'cat', "dach": "roof"}
print("Znam takie słowka:", pol_ang.keys())
odp = input("Podaj słówko do przetłumaczenia:")
print(f"Prawidłowa odpowiedż dla: {odp} to: {pol_ang.get(odp.strip().casefold(), "Nie ma w słowniku")}")
# Podaj słówko do przetłumaczenia:kot
# Prawidłowoa odpowiedż dla: kot to: cat
# Znam takie słowka: dict_keys(['pies', 'kot', 'dach'])
# Podaj słówko do przetłumaczenia: Kot
# Prawidłowa odpowiedż dla:  Kot to: cat

print("\N{LATIN SMALL LETTER SHARP S}")  # ß
