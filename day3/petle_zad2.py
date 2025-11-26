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

pol_ang = {'pies': 'dog', "kot": 'cat', "dach": "roof"}