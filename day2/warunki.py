# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if
# w zależności od warunku wykona jeden lub drugi blok programu
# instrukcja w warunku musi zwrac bool

odp = True
print(bool(True))  # True

# debugger - wykonywanie kodu krok po kroku
# pułapka
odp = False
if odp:
    # blok programu wykonany gdy warynek True
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

# instrukcja poza warunkiem
print("Dalsza część programu")
# True
# Dalsza część programu

odp = "Radek"

if odp:
    print("Dane zostały wczytane")  # Dane zostały wczytane

if odp == "Radek":  # porównanie
    print("Jesteś Radek")  # Jesteś Radek

odp = 0
print(bool(odp))  # False
if odp:
    print("Działa")
else:  # w przeciwnym przypadku
    print("Zero -> False")
# Zero -> False

a = "Radek"
# Długośc wynosi: dl, wiecej niz 3
if len(a) > 3:
    print(f"Długośc wynosi {len(a)}, więcej niż 3")

n = len(a)
if n > 3:
    print(f"Długośc wynosi {n}, więcej niż 3")

# walrus operator, operator morsa
if (n := len(a)) > 3:
    print(f"Długośc wynosi {n}, więcej niż 3")
# Długośc wynosi 5, więcej niż 3
