class Car:
    """
    Klasa opisująca samochód w pythonie
    """

    def __init__(self, model, year):
        """
        Konstruktor - metoda inicjalizująca
        :param model:
        :param year:
        """

        self.model = model
        self.year = year
        # pole prywatne
        # hermetyzacja
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi: {self.__predkosc} km/h")

    def hamulec(self):
        self.__predkosc -= 10
        self.__zmina_biegu()

    def __zmina_biegu(self):
        print("Zmiana biegów")


car = Car("Toyota", 2025)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(car.__predkosc)  # 50
car.licznik()  # Prędkość wynosi: 50 km/h
car.__predkosc = 0  # pole publiczne
car.licznik()  # Prędkość wynosi: 50 km/h

car.hamulec()
car.hamulec()
car.hamulec()
car.hamulec()
car.hamulec()
car.licznik()  # Prędkość wynosi: 0 km/h
# Prędkość wynosi: 50 km/h
# Zmiana biegów
# Zmiana biegów
# Zmiana biegów
# Zmiana biegów
# Zmiana biegów
# Prędkość wynosi: 0 km/h
#


# enkapsulacja - hermetyzacja pól, wystawienie metod do zapisu i odczytu
# settery, gettery
