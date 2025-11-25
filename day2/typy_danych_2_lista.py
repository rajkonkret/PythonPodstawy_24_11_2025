# kolekcje

# lista - przechowuje dowolną ilość danych, róznego typu na raz
# zachowuje kolejność przy dodawaniu

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# append() - dodawanie do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Marek")
lista.append("Mateusz")
lista.append("Marcin")
lista.append("Magda")
lista.append("Paulina")

print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Marek', 'Mateusz', 'Marcin', 'Magda', 'Paulina']
#     0         1       2        3         4          5         6        7

print(len(lista))  # długośc 8

print(lista[2])  # Zenek
print(lista[4])  # Mateusz

# print(lista[10]) # IndexError: list index out of range

print(lista[7])  # Paulina
print(lista[len(lista) - 1])  # Paulina
print(lista[-1])  # Paulina
# ['Radek', 'Tomek', 'Zenek', 'Marek', 'Mateusz', 'Marcin', 'Magda', 'Paulina']
#     0         1       2        3         4          5         6        7
#     -8        -7      -6       -5        -4         -3        -2       -1
print(lista[-3])  # Marcin

# slicowanie - fragment listy
print(lista[0:3])  # ['Radek', 'Tomek', 'Zenek'] 012, z prawej niewłacznie
print(lista[:3])  # ['Radek', 'Tomek', 'Zenek']

print(lista[2:])  # ['Zenek', 'Marek', 'Mateusz', 'Marcin', 'Magda', 'Paulina'], z ostatnim włacznie
print(lista[2:7])  # ['Zenek', 'Marek', 'Mateusz', 'Marcin', 'Magda'], bez ostatniego, niewlacznie
