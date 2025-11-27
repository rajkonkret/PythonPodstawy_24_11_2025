# funkcja zwracające wynik
# kończy się return (zwróc)

def dodaj(a, b):
    return a + b


def odejmij(a=0, b=0, c=0):
    return a - b - c


print(dodaj(6, 8))  # 14
wynik = dodaj(6, 90)
print("Wynik:", wynik)  # Wynik: 96

print(odejmij())  # 0
print(odejmij(a=8, b=9, c=89))  # -90
print(odejmij(1, 2, 3))
print(odejmij(1, 2))  # -1
print(odejmij(1, b=9, c=90))  # -98


def oblicz_vat(kwota, vat=23):
    return kwota * (100 + vat) / 100


print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))
print(oblicz_vat(vat=15, kwota=3500))
# 1230.0
# 1080.0
# 4025.0

zm = oblicz_vat(1000)
print(zm)
print(type(zm))  # <class 'float'>
if zm == 1230:
    print("Ok")  # Ok

print(dodaj(5, 9) + odejmij(5, 9))  # 10
print(print("Radek"))
# Radek
# None
