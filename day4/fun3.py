a = 10
b = 10


def dodaj():
    a = 7  # zmienne lokalne,
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a  # uzyj globalnej zmiennej
    a = 9  # zmienna globalna
    b = 90  # zmienna loklana
    print(a + b)


print(f"Wartość a z góry: {a} (globalna)")  # Wartość a z góry: 10 (globalna)
dodaj()
print(f"Wartość a z góry: {a} (globalna)")  # Wartość a z góry: 10 (globalna)
dodaj2()
print(f"Wartość a z góry: {a} (globalna)")  # Wartość a z góry: 10 (globalna)
dodaj3()
print(f"Wartość a z góry: {a} (globalna)")  # Wartość a z góry: 9 (globalna)
print(f"{a=}, {b=}")  # a=9, b=10
dodaj2()
