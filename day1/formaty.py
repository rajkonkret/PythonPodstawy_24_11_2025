user = "Tomek"  # str
wiek = 39  # int
wersja = 3.90001
print(type(wersja))  # <class 'float'>, zmiennoprzecinkowe
liczba = 345678098123678  # int

print("Witaj %s, masz teraz %d lat." % (user, wiek))
# Witaj Tomek, masz teraz 39 lat.
# %s - string
# %d - digit - liczba

# sprawdza typy
# print("Witaj %d, masz teraz %s lat." % (user, wiek))
# TypeError: %d format: a real number is required, not str

print(f"Witaj {user}, masz teraz {wiek} lat.") # Witaj Tomek, masz teraz 39 lat.

