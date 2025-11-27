def all_params(a, b, /, c=42, d=256):
    print(f"{a=}, {b=}")
    print(f"{c=}, {d=}")


all_params(1, 2)
# a=1, b=2
# c=42, d=256
all_params(1, 2, 3, 4)
# a=1, b=2
# c=3, d=4
# TypeError: all_params() got some positional-only arguments passed as keyword arguments: 'a, b'
# all_params(a=1, b=2, c=3, d=4)
# / - wymusza koniecznośc podawania argumetów z lewej strony po pozycji
all_params(1, 2, c=3, d=4)


def all_params2(name, b, /, c=42, *args, **kwargs):
    print(f"{name=}")
    print(f"{b=}")
    print(f"{c=}")
    print(f"{args=}")
    print(f"{kwargs=}")


all_params2(1, 2, name="Radek")
# name=1
# b=2
# c=42
# args=()
# kwargs={'name': 'Radek'}


