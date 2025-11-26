# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if
# w zależności od warunku wykona jeden lub drugi blok programu
# instrukcja w warunku musi zwrac bool

odp = True
print(bool(True))  # True
if odp: print("Test")
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

# podatek = 0
# zarobki = int(input("Podaj zarobki:"))
# # kolejnośc ma znaczenia
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 40_000:
#     # elif zarobki < 40_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else:  # pozostałe
#     podatek = 0.9
#
# print(f"Podatek wynosi: {zarobki * podatek} pln.")
# # podatek 0.2, od 10000 do 39999
# # Podaj zarobki:15000
# # Podatek wynosi: 3000.0 pln.

suma_zam = 150
if suma_zam > 100:
    rabat = 25
else:
    rabat = 0
print(f"Rabat wynosi: {rabat}")  # Rabat wynosi: 25

# operator warumkowy
rabat = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi: {rabat}")  # Rabat wynosi: 25

#
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1
# napisac test z....
# dodac punktację
# punkty = 0
# odp = input("Podaj rok Chrztu Polski:")
# if odp.strip().casefold() == '966'.strip().casefold():
#     print("Prawidłowa odpowiedź")
#     punkty += 1  # punkty = punkty + 1
# else:
#     print("Błędna odpowiedż")
# print("Zdobyte punkty:", punkty)
#
# odp = input("czy Ala ma kota?")
# if odp.strip().casefold() == 'tak'.strip().casefold():
#     print("Prawidłowa odpowiedź")
#     punkty += 1  # punkty = punkty + 1
# else:
#     print("Błędna odpowiedż")
# print("Zdobyte punkty:", punkty)

# Podaj rok Chrztu Polski:966
# Prawidłowa odpowiedź
# Zdobyte punkty: 1
# czy Ala ma kota?tak
# Prawidłowa odpowiedź
# Zdobyte punkty: 2

# zasymulujemy system zbierania logów
# zmienna: przechowuje typ sestemu np.: console, email, inny

# console: "Stało się coś strasznego"
# email: "System email"
# zmienna: przechowuje rodzaj błędu: error, medium i inny
# dla email: do listy błedów dopisać error -> krytyczny
alert_system = "email"
error_level = "error"
lista_b = []

if alert_system == "console":
    print("Stało się coś strasznego")
elif alert_system == "email":
    print("System email")
    if error_level == "error":
        lista_b.append("krytyczny")
    elif error_level == "medium":
        lista_b.append("ostrzeżenie")
    else:
        lista_b.append("inny")
else:
    print("Inny system")

print(lista_b)  # ['krytyczny']
