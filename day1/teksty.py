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
# ctrl d - powielenie lini
print(tekst.capitalize())  # Witaj świecie

# Witaj świecie
# 0123456789....
print(tekst[2])  # t

print(tekst.index("Ś"))  # index numer: 6

print(tekst.count("i"))  # wystepuje 3 razy

print(tekst.count("w"))  # 1 jeden  raz
print(tekst.lower().count("w"))  # 2, wystepuje 2 razy

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# strip() - usunięcie białych znaków, wiodących i kończących spacji
print(tekst.removesuffix("Świecie").strip())  # "Witaj"

encode_s = tekst.encode("utf-8")
print(encode_s)  # b'Witaj \xc5\x9awiecie'
print(type(encode_s))  # <class 'bytes'>
# \xc5\x9a - dane w postaci szesnastkowej
print(encode_s.decode('utf-8'))  # Witaj Świecie
