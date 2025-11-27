# stworzyc funkcję kantor
# ma miec dwie wewnętrzne funkcje: usd, eur
# w zależności od parametrów ma zwrócić jedną lub drugę funkcja (if)
# przekazenie argumentu (kwota) do funkcji usd i eur

def kantor(waluta):
    def usd(kwota=0):
        print(f"Zamiana {kwota} usd na {kwota * 3.65} pln.")

    def eur(kwota=0):
        print(f"Zamiana {kwota} eur na {kwota * 4.23} pln.")

    if waluta == "usd":
        return usd
    else:
        return eur


kantor_usd = kantor('usd')
kantor_usd(10000)
kantor_usd(10000)
kantor_usd(10000)
kantor_usd(1.10)
kantor_usd(100)
kantor_usd(1000)
# Zamiana 10000 usd na 36500.0 pln.
# Zamiana 10000 usd na 36500.0 pln.
# Zamiana 10000 usd na 36500.0 pln.
# Zamiana 1.1 usd na 4.015000000000001 pln.
# Zamiana 100 usd na 365.0 pln.
# Zamiana 1000 usd na 3650.0 pln.

kantor_eur = kantor("eur")
kantor_eur(567)
kantor_eur(5067)
kantor_eur(1567)
kantor_eur(5679)
# Zamiana 567 eur na 2398.4100000000003 pln.
# Zamiana 5067 eur na 21433.410000000003 pln.
# Zamiana 1567 eur na 6628.410000000001 pln.
# Zamiana 5679 eur na 24022.170000000002 pln.
