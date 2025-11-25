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

print(lista[2:20])  # ['Zenek', 'Marek', 'Mateusz', 'Marcin', 'Magda', 'Paulina']
print(lista[12:45])  # []

print(bool(lista[12:45]))  # False

print(lista[:])  # ['Radek', 'Tomek', 'Zenek', 'Marek', 'Mateusz', 'Marcin', 'Magda', 'Paulina']

# ['Radek', 'Tomek', 'Zenek', 'Marek', 'Mateusz', 'Marcin', 'Magda', 'Paulina']
#     0         1       2        3         4          5         6        7
#     -8        -7      -6       -5        -4         -3        -2       -1
print(lista[-2:0])  # [5:0] -> []
print(lista[0:-2])  # ['Radek', 'Tomek', 'Zenek', 'Marek', 'Mateusz', 'Marcin']

# range() - generuje liczby z zakresu
lista_15 = list(range(15))  # od 0 do 14
print(lista_15)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(lista_15[0:15:2])  # [start:stop:krok], [0, 2, 4, 6, 8, 10, 12, 14]
print(lista[::2])  # ['Radek', 'Zenek', 'Mateusz', 'Magda']
print(lista_15[::3])  # [0, 3, 6, 9, 12]

print(list(range(0, 15, 2)))  # (start,stop,krok), [0, 2, 4, 6, 8, 10, 12, 14]

# wyświetli listę w odwrotnej kolejności
print(lista[::-1])
# ['Paulina', 'Magda', 'Marcin', 'Mateusz', 'Marek', 'Zenek', 'Tomek', 'Radek']

# nadpisanie elementu w liscie, na wskazanym indeksie
lista[3] = "Asia"
print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Asia', 'Mateusz', 'Marcin', 'Magda', 'Paulina']

# wstawienie elementu na wskazanym indeksie
lista.insert(1, "Ola")
print(lista)
# ['Radek', 'Ola', 'Tomek', 'Zenek', 'Asia', 'Mateusz', 'Marcin', 'Magda', 'Paulina']

lista_darek = []
lista_darek.insert(1, "Darek")
print(lista_darek)  # ['Darek']

# usunięcie elemntów z listy po elemencie, pierwwszy napotkany
lista.remove("Tomek")
print(lista)  # ['Radek', 'Ola', 'Zenek', 'Asia', 'Mateusz', 'Marcin', 'Magda', 'Paulina']
# dodac np.: Asia, usunąc Asia
lista.append("Asia")
print(lista)
# ['Radek', 'Ola', 'Zenek', 'Asia', 'Mateusz', 'Marcin', 'Magda', 'Paulina', 'Asia']
lista.remove("Asia")
print(lista)
# ['Radek', 'Ola', 'Zenek', 'Mateusz', 'Marcin', 'Magda', 'Paulina', 'Asia']

# usnięcie po indeksie, zwraca usunięty element
# pop()
print(lista.pop(2))  # , Zenek
zmienna = lista.pop(-1)
print("Usunięto:", zmienna)  # Usunięto: Asia
print(lista)  # ['Radek', 'Ola', 'Mateusz', 'Marcin', 'Magda', 'Paulina']
print(lista.pop())  # usunie ostatni, Paulina

# sprawdzenie indexu dla danego elementu, pierwszy napotkany
print(lista.index("Marcin"))  # indeks: 3

a = 1
b = 3
a = b
print(f"{a=}, {b=}")  # a=3, b=3
# b = a -> a=1, b=1
b = 9
print(f"{a=}, {b=}")  # a=3, b=9

lista2 = lista  # kopia adresu, referencja
lista_copy = lista.copy()  # kopia elementów listy do nowej listy
print(lista)  # ['Radek', 'Ola', 'Mateusz', 'Marcin', 'Magda']
print(lista2)  # ['Radek', 'Ola', 'Mateusz', 'Marcin', 'Magda']
lista.clear()  # usunięcie wszystkich elementów z listy
print(lista)  # []
print(lista2)  # []
print(lista_copy)  # ['Radek', 'Ola', 'Mateusz', 'Marcin', 'Magda']

# id() - pokazuje referencje
print(id(lista))  # 2213587636160
print(id(lista2))  # 2213587636160
print(id(lista_copy))  # 2213590273152

liczby = [54, 999, 34, 12.34, 567, 999]
print(liczby)  # [54, 999, 34, 12.34, 567, 999]
print(type(liczby))  # <class 'list'>

liczby.sort()
print(liczby)  # [12.34, 34, 54, 567, 999, 999]
#
# liczby = [54, 999, 34, 12.34, 567, 999, "A"]
# print(liczby)  # [54, 999, 34, 12.34, 567, 999, 'A']
# liczby.sort()
# # TypeError: '<' not supported between instances of 'str' and 'int'

print(lista_copy)  # ['Radek', 'Ola', 'Mateusz', 'Marcin', 'Magda']
lista_copy.sort()
print(lista_copy)  # ['Magda', 'Marcin', 'Mateusz', 'Ola', 'Radek']

lista_copy.sort(reverse=True)  # sortowanie i odwrócenie
print(lista_copy)  # ['Radek', 'Ola', 'Mateusz', 'Marcin', 'Magda']

lista_copy.reverse()  # tylko odwróćenie
print(lista_copy)
# ['Magda', 'Marcin', 'Mateusz', 'Ola', 'Radek']

liczby[3] = 666
print(liczby[0:3])  # [12.34, 34, 54] -> indeksy 012
print(liczby[-3])  # 666
print(liczby)  # [12.34, 34, 54, 666, 999, 999]
