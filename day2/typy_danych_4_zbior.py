# zbior (set) - przechowuje unikalne wartości (brak duplikatów)
# nie zachowuje kolejności przy dodawaniu elementu
# nie posiadają indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>

# pusty zbior
zb2 = set()  # tylko iwyłaczenie słowkiem set()
print(zb2)  # set()
print(type(zb2))  # <class 'set'>

# dodanie elementu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(33)
zbior.add(24)
zbior.add(24)
zbior.add(25)

print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55, 24, 25}

# usunięcie elemntu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 24, 25}

# pop() - zwraca i usunie pierwszy element
print(zbior.pop())  # 33

zmienna = zbior.pop()
print(f"Zmienna: {zmienna}")  # Zmienna: 66
print("Zmienna:", zmienna)  # Zmienna: 66

zbior_copy = zbior.copy()
print(zbior_copy)
print(id(zbior))  # 2296409860448
print(id(zbior_copy))  # 2296415232608

zbior_2 = {667, 11, 44, 12.34, 18, 52, 667, 62}

# suma zbiorów - zwraca nowy zbiór
print(zbior | zbior_2)  # {777, 11, 44, 12.34, 18, 52, 22, 24, 25, 667, 62}
print(zbior.union(zbior_2))  # {777, 11, 44, 12.34, 18, 52, 22, 24, 25, 667, 62}

# część wspólna - tworzy nowy zbior
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# różnica zbiorów - zwraca nowy zbiór
print(zbior - zbior_2)  # {24, 777, 22, 25}
print(zbior.difference(zbior_2))  # {24, 777, 22, 25}
print(zbior_2.difference(zbior))  # {667, 52, 12.34, 62}

# łączy zbiory, zmienia bazowy!!!
zbior.update(zbior_2)
print(zbior)  # {777, 11, 44, 12.34, 18, 52, 22, 24, 25, 667, 62}

krotka = tuple(zbior)
print(krotka)  # (777, 11, 44, 12.34, 18, 52, 22, 24, 25, 667, 62)

lista = list(zbior)
print(lista)  # [777, 11, 44, 12.34, 18, 52, 22, 24, 25, 667, 62]

print(667 in zbior)  # True, najszybsze wyszukiwanie
print(667 in krotka)  # True
print(667 in lista)  # True
print(767 in lista)  # False
