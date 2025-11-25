# krotka - tuple - lista tylko do odczytu, niemutowalne
# pozwala efektywniej zarządzać pamięcią
# krotka jednoelementowej - stała, szczególny przypadek zmiennej

tupla_imiona = "Zenek", "Marek", "Radek", "Ania"
print(type(tupla_imiona))  # <class 'tuple'>
print(tupla_imiona)  # ('Zenek', 'Marek', 'Radek', 'Ania')

# tupla liczbowa
# tupla_liczby = 43, 55, 22.34, 11, 200
tupla_liczby = (43, 55, 22.34, 11, 200)
print(type(tupla_liczby))  # <class 'tuple'>
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)

# tupla jedoelementową
tupla_jeden = 45,
print(tupla_jeden)
print(type(tupla_jeden))
# (45,)
# <class 'tuple'>

# PEP8 zaleca by jednoelemntowe tuple robic z nawiasami
tupla_jeden = (45,)
print(tupla_jeden)
print(type(tupla_jeden))

# tupla jest niemutowalne
# tupla_jeden[0] = 123  # TypeError: 'tuple' object does not support item assignment

# usunięcie całej tupli
del tupla_jeden
# print(tupla_jeden)# NameError: name 'tupla_jeden' is not defined

print(tupla_imiona.index("Radek"))  # index 2
print(tupla_imiona.count("Radek"))  # wystepuje 1 raz

print(len(tupla_imiona))  # długośc 4

tup = 1, 2
print(type(tup))  # <class 'tuple'>

# a - pierwsza wartosc, b - druga wartosc
a = tup[0]
b = tup[1]
print(a, b)  # 1 2

# rozpakowanie krotki
a, b = 1, 2
print(a, b)  # 1 2

a, b = tup
print(a, b)  # 1 2

print(tupla_imiona)
# name1, name2, name3 = ('Zenek', 'Marek', 'Radek', 'Ania')
# name1, name2, name3 = tupla_imiona# ValueError: too many values to unpack (expected 3, got 4)
name1, name2, *name3 = tupla_imiona  # * - worek na pozostale dane
print(name1, name2, name3)  # Zenek Marek ['Radek', 'Ania']

*name1, name2, name3 = tupla_imiona  # * - worek na pozostale dane
print(name1, name2, name3)  # ['Zenek', 'Marek'] Radek Ania

name1, *name2, name3 = tupla_imiona  # * - worek na pozostale dane
print(name1, name2, name3)  # Zenek ['Marek', 'Radek'] Ania
print(f"Pierwsza grupa:", name1)
print(f"Druga grupa:", name2)
print(f"trzecia grupa:", name3)
# Pierwsza grupa: Zenek
# Druga grupa: ['Marek', 'Radek']
# trzecia grupa: Zenek

# sortowanie sorted()  - zwraca posortowaną listę!!!
print(sorted(tupla_imiona))  # ['Ania', 'Marek', 'Radek', 'Zenek']
# tupla_imiona nie została zmieniona
print(tupla_imiona)  # ('Zenek', 'Marek', 'Radek', 'Ania')
