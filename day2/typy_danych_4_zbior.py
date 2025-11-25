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
