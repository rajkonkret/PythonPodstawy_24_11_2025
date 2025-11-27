# funkcja - wydzielony fragment programu, można użyć w dowolnym momencie
# funkcja musi zostac najpier zadeklarowana
# żeby użyc funkcji trzeba ją wywołać

a = 6
b = 8


# funkcje nie zwracaja wyniku
# deklaracja funkcji
def dodaj():  # funkcja bezargumentowa
    print(a + b)


def dodaj2(a, b):  # funkcja z argumentami a i b
    print(a + b)


# ominiecie problemu przeciążania funkcji liczbą argumentów
def odejmij(a, b, c=0):  # wartość domyślna
    print(a - b - c)


# wywołanie funkcji
dodaj()  # 14
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'

# przekazywanie po pozycji
dodaj2(14, 67)  # 81

odejmij(1, 2)  # -1
odejmij(1, 2, 4)  # -5

# przekazywanie po nazwie (keywords)
odejmij(b=9, a=10, c=11)  # -10
odejmij(b=9, a=19)  # 10
dodaj2(b=9, a=90)  # 99

# mieszane
odejmij(1, 2, c=78)  # -79
dodaj2(1, b=9)

# pozycyjne argumenty muszą być przed nazwanymi
# odejmij(a=9, 1, 2) # SyntaxError: positional argument follows keyword argument

# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# print(dodaj() + dodaj2(5, 9))
