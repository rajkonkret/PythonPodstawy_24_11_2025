dictionary = {"imie": "Radek", 'nazwisko': "Kowalski"}

# wypisze klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for i in dictionary.keys():
    print(i)
# imie
# nazwisko

# wypisanie wartości
for i in dictionary.values():
    print(i)
# Radek
# Kowalski

# wypisanie par
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

# sep
#         string inserted between values, default a space.
for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski

for k, v in dictionary.items():
    print(k, v, sep="<===>")
# imie<===>Radek
# nazwisko<===>Kowalski

#  end
#         string appended after the last value, default a newline.
for k, v in dictionary.items():
    print(k, v, sep="<===>", end=" | ")
# imie<===>Radek | nazwisko<===>Kowalski |

print()  # zresetowanie end, end="\n"
pol_ang = {'pies': 'dog', "kot": 'cat', "dach": "roof"}
ang_pol = {}
for k, v in pol_ang.items():
    ang_pol[v] = k
print(ang_pol)  # {'dog': 'pies', 'cat': 'kot', 'roof': 'dach'}

# dict comprehensions
print({v: k for k, v in pol_ang.items()})
# {'dog': 'pies', 'cat': 'kot', 'roof': 'dach'}
