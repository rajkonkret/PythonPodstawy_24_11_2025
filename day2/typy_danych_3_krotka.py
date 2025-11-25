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
