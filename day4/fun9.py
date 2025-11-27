# funkcja lambda
# skrócony zapis funkcji
# lambda zwraca wynik (return)
# funkcja anonimowa

def odejmij(a, b):
    return a - b


print(odejmij(10, 8))  # 2

odejmij2 = lambda a, b: a - b  # domyślnie posiada return
print(odejmij2(10, 8))  # 2

oblicz_vat = lambda kwota, vat=23: kwota * (100 + vat) / 100
print(oblicz_vat(1000))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(29))  # dorosły

# mapowanie danych
lista = [1, 2, 14, 24, 50, 67, 80, 100, 200, 500]
l1 = []
for i in lista:
    l1.append(i * 2)
print(l1)
# [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]

print([i * 2 for i in lista])


# [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]

def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))
print(l2)
# [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]


# map() - wykonuje funkcje na zadanych elementach kolekcji
# funkcja wyższego rzędu, jako argument przyjmuje inną funkcję

print(f"Zastosowanie map():{list(map(zmien, lista))}")  # zmien - adres funkcji
# Zastosowanie map():[2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]

# lambda jako funkcja anonimowa
print(f"Zastosowanie map():{list(map(lambda x: x * 2, lista))}")  # zmien - adres funkcji
print(f"Zastosowanie map():{list(map(lambda x: x * 4, lista))}")  # zmien - adres funkcji
print(f"Zastosowanie map():{list(map(lambda x: x * 5, lista))}")  # zmien - adres funkcji
# Zastosowanie map():[2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]
# Zastosowanie map():[4, 8, 56, 96, 200, 268, 320, 400, 800, 2000]
# Zastosowanie map():[5, 10, 70, 120, 250, 335, 400, 500, 1000, 2500]

# filtrowanie danych

l4 = []
for i in lista:
    if i < 3:
        l4.append(i)
print(l4)  # [1, 2]

# [1, 2, 14, 24, 50, 67, 80, 100, 200, 500]
# filter() - zwraca eleemnty spełniające warunek
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 3, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 50, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 30, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 150, lista))}")
# Zastosowanie filter(): [1, 2]
# Zastosowanie filter(): [1, 2, 14, 24]
# Zastosowanie filter(): [50, 67, 80, 100, 200, 500]
# Zastosowanie filter(): [1, 2, 14, 24, 50, 67, 80, 100]
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 3 and x < 150, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: 3 < x < 150, lista))}")
# Zastosowanie filter(): [14, 24, 50, 67, 80, 100]
# Zastosowanie filter(): [14, 24, 50, 67, 80, 100]
