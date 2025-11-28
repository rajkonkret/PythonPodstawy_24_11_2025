# github copilot, tabnine, jetbrain ai
print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")
input()
print("Radek")
print("Radek")
input()

# napisz funkcje obliczanie sredniej
def srednia(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

def oceny():
    oceny = []
    while True:
        ocena = input("Podaj ocenę (koniec aby zakończyć): ")
        if ocena.lower() == "koniec":
            break
        try:
            ocena = float(ocena)
            oceny.append(ocena)
        except ValueError:
            print("Nieprawidłowa ocena, spróbuj ponownie.")
    return oceny

oceny_lista = oceny()
srednia_ocen = srednia(*oceny_lista)
print(f"Średnia ocen: {srednia_ocen}")
# Średnia ocen: 4.5


def filtruj_parzyste(*args):
    return list(filter(lambda x: x % 2 == 0, args))

parzyste_liczby = filtruj_parzyste(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"Parzyste liczby: {parzyste_liczby}")
# Parzyste liczby: [2, 4, 6, 8, 10]

# napisz funkcje tabliczka mnożenia jako macierz
def tabliczka_mnozenia_macierz():
    return [[i * j for j in range(1, 11)] for i in range(1, 11)]
print("Tabliczka mnożenia jako macierz:")
macierz = tabliczka_mnozenia_macierz()
for wiersz in macierz:
    print(wiersz)

def tabliczka_mnozenia(n):
    return [n * i for i in range(1, 11)]
print(f"Tabliczka mnożenia dla 5: {tabliczka_mnozenia(5)}")

# chtgpt, gemini, grok, claude
# Tabliczka mnożenia jako macierz:
# [1, 2, 3, 4, 5, 6,
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# [3, 6, 9, 12, 15, 18,
