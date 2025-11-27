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

cz2