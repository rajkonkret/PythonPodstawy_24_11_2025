# klasa - przepis, szablon
# cechy (zmienne)
# metody - funkcje w klasie
# obiekt - instancja klasy
# klasa musi zostac zadeklarowana
# tworzenie obiektu uruchamia funkcję inicjalizującą (konstruktor) __init__
# paradygmaty -> hermetyzacja, dziedziczenie, polimorfizm, abstrakcja

# PascalCase, UpperCamelCase
class Human:
    """
    Klasa Human opisujaca człowieka w pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    # self - obiekt
    def powitanie(self):
        print(f"Nazywam się: {self.imie}")
        # print(f"Nazywam się: {cz1.imie}")

    def ruszaj(self):

        if self.plec == "m":
            print("Ruszył e m w drogę.")
        else:
            print("Ruszyał a m w drogę.")


# print(print.__doc__)
# print(Human.__doc__)  # Klasa Human opisujaca człowieka w pythonie
# pydoc - dokumentacja
#  cd day4 - wejscie do katalogu
#  pydoc -b - serwer dokumentacji
# cd .. - wyjscie katalog wyżej
#  pydoc -w kl1 - generuje html z dokumentacją

cz1 = Human()  # tworzenie obiektu
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)

cz1.wiek = 44
cz1.imie = "Radek"
cz1.plec = "m"
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# Radek
# 44
# m

cz2 = Human()
cz2.imie = "Anna"
cz2.wiek = 34
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
# Anna
# 34
# k

cz1.powitanie()  # Nazywam się: Radek
cz2.powitanie()  # Nazywam się: Anna

cz1.ruszaj()
cz2.ruszaj()
# Ruszył e m w drogę.
# Ruszyał a m w drogę.
