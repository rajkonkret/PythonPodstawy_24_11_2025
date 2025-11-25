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
