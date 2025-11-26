# pętla - pozwala wielokrotnie wykonac fragment kodu
# for - pętla iteracyjna
import random

for i in range(5):  # od 0 do 4
    print(i)

for i in range(20):
    pass  # nic nie rób

for _ in range(5):  # niema zmienna
    print("Test podłoga")
    print(_)
# Test podłoga
# 4

for i in range(5):
    print(i + 2)
    print(i * 2)

# przerobic lotto na pętle
# lista_wynik
lista_kule = list(range(1, 50))  # od 1 do 49
lista_wynik = []
for _ in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    # print(wyn)
    lista_wynik.append(wyn)

print(lista_wynik)  # [23, 20, 17, 30, 31, 48]

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

# parzyste do nowej listy
lista3 = []
for j in range(10):
    if j % 2 == 0:
        lista3.append(j)
print(lista3)  # [0, 2, 4, 6, 8]

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista3:  # podstawi kolejne elementy kolekcji
    print(c)

lista_nazwy = ["Ala", "Tomek", "Zenek", "Basia"]
for p in lista_nazwy:
    print(p)
    # Ala
    # Tomek
    # Zenek
    # Basia

for c in lista3:
    if c > 4:
        print(c, "Wieksze od 4")
    elif c == 4:
        print(c, "Równe 4")
    else:
        print(c, "Mniejsze od 4")

    print(c)  # dla kazdego elementu pętli

print("Po zakońćzeniu pętli")
# 0 Mniejsze od 4
# 0
# 2 Mniejsze od 4
# 2
# 4 Równe 4
# 4
# 6 Wieksze od 4
# 6
# 8 Wieksze od 4
# 8
# Po zakońćzeniu pętli

for i in range(10, 0, -2):  # krok -2, idziemy w dół od 10 do 1, (start, stop, krok)
    print(i)

for i in range(-10, 0):
    print(i)

imiona = ["Radek", "Tomek", "Agata", "Marek"]
for p in imiona:
    print(p)
# Radek
# Tomek
# Agata
# Marek

# 0 Randek
for i in range(len(imiona)):
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Agata
# 3 Marek

for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Agata
# 3 Marek

# enumerate() - zwraca numer i element kolekcji
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Agata')
# i, o = (3, 'Marek')

for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Agata
# 3 Marek

for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Agata
# 4 Marek

a, b = (3, 'Marek')
print(a, b)  # 3 Marek

imiona = ["Radek", "Tomek", "Agata", "Marek", "Magda"]
wiek = [44, 56, 23, 34]

# Radek 44
# 3 dla różnej długości list będzie bład:
# IndexError: list index out of range
# for p in imiona:
#     print(p, wiek[imiona.index(p)])
# Radek 44
# Tomek 56
# Agata 23
# Marek 34

# zip() - łaczy kolekcje
for i in zip(imiona, wiek):
    print(i)
# ('Radek', 44)
# ('Tomek', 56)
# ('Agata', 23)
# ('Marek', 34)
for i, w in zip(imiona, wiek):
    print(i, w)
# Radek 44
# Tomek 56
# Agata 23
# Marek 34

# 0 Radek 44
for i in enumerate(zip(imiona, wiek)):
    print(i)
# (0, ('Radek', 44))
# (1, ('Tomek', 56))
# (2, ('Agata', 23))
# (3, ('Marek', 34))
a, b = (0, ('Radek', 44))
print(a, b)  # 0 ('Radek', 44)
c, d = ('Radek', 44)
print(c, d)
(a, (c, d)) = (0, ('Radek', 44))
print(a, c, d)  # 0 Radek 44
for i, (o, w) in enumerate(zip(imiona, wiek)):
    print(i, o, w)
# 0 Radek 44
# 1 Tomek 56
# 2 Agata 23
# 3 Marek 34
