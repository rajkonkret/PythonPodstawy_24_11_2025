def connect(**opcje):  # *8 dowolna ilość argumntów nazwanych (keywords) słownikowe
    print(opcje)


connect()
connect(a=100)  # {'a': 100}
connect(a=100, b=89, c=90, name="Radek", age=50)


# {'a': 100, 'b': 89, 'c': 90, 'name': 'Radek', 'age': 50}


def all_args(*args, **kwargs):
    print(args, kwargs)


all_args()  # () {}
all_args(1, 2, 3, 4, 5, 6, 7)  # (1, 2, 3, 4, 5, 6, 7) {}
all_args(a=10, b=10, c=90, name="Radek")  # () {'a': 10, 'b': 10, 'c': 90, 'name': 'Radek'}


def random_radek(*args, k=0):
    print(args, k)


random_radek(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 101, 23213, 213123)
random_radek(12, 3, k=6)  # (12, 3) 6
