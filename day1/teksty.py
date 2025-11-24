tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))  # <class 'str'>

# teksty są niemutowalne
""" Return a copy of the string converted to uppercase. """
tekst.upper()  # nie zmienia oryginału
print(tekst)  # Witaj Świecie
print(tekst.upper())  # wyswietlamy wynik działania funkcji, WITAJ ŚWIECIE
zm = tekst.upper()
print(zm)  # WITAJ ŚWIECIE
print(tekst)

print(tekst.lower())  # witaj świecie
# xtrl d - powielenie lini
print(tekst.capitalize())  # Witaj świecie

# Witaj świecie
# 0123456789....
print(tekst[2])
