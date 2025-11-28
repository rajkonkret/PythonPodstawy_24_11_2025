from abc import ABC, abstractmethod


# klasa abstrakcyjna posiada metode abstrakcyjną
class Ptak(ABC):
    """
    Klasa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca
        :param gatunek:
        :param szybkosc:
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością:", self.szybkosc, "km/h")

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    """
    Klasa Kura dziedziczy po klasie Ptak
    """

    def __init__(self, gatunek):
        """
        Nadpisujemy konstruktor
        :param gatunek:
        """

        # musimu użyć słówka super()
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam.")

    def wydaj_odglos(self):
        print("Ko ko ko ko ko")


class Orzel(Ptak):

    def wydaj_odglos(self):
        print("kier kir kier kir")


# klasa abstrakcyjna - nie można tworzyc obiektów takiej klasy
# TypeError: Can't instantiate abstract class Ptak without
# an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzeł", 50)
# or1.latam()  # Tu Orzeł Lecę z szybkością: 50 km/h
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością: 0 km/h

kur2 = Kura("Kura zlocista")
kur2.latam()  # Tu Kura zlocista Ja nie latam.
kur2.wydaj_odglos()
# Tu Kura zlocista Ja nie latam.
# Ko ko ko ko ko

or2 = Orzel("Orzel Bielik", 56)
or2.latam()
or2.wydaj_odglos()
# Tu Orzel Bielik Lecę z szybkością: 56 km/h
# kier kir kier kir