class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca - konstruktor
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """

        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    # self - obiekt
    def powitanie(self):
        print(f"Nazywam się: {self.imie}")
        # print(f"Nazywam się: {cz1.imie}")

    def ruszaj(self):

        if self.plec == "m":
            print("Ruszył e m w drogę.")
        else:
            print("Ruszyał a m w drogę.")

    # wypisz_wiek(), wypisz_wzrost()
    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat.")

    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu.")


# TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
# cz1 = Human()

cz1 = Human("Radek", 45, 189, "m")
print(cz1.imie)
print(cz1.wiek)
print(cz1.wzrost)
print(cz1.plec)
# Radek
# 45
# 189
# m

cz1.powitanie()
cz1.ruszaj()
# Nazywam się: Radek
# Ruszył e m w drogę.

cz1.wypisz_wiek()
cz1.wypisz_wzrost()
# Mam 45 lat.
# Mam 189 cm wzrostu.