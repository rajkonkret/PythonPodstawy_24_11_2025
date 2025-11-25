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


