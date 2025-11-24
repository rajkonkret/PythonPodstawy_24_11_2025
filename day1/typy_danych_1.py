import sys

wiek = 47  # int
rok = 2025  # int
temp = 36.6  # float

print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)
# 2072
# -1978
# 95175
# 0.023209876543209877 -> float
print(12 / 3)  # 4.0
print(2025 / 47)  # 43.08510638297872
print(2025 // 47)
print(rok // wiek)  # 43, część całkowita z dzielenia

print(rok % wiek)  # modulo, reszta z dzielenia, 4
print(43 * 47)  # 2021
print(2025 - 2021)  # 4

print(10 % 3)  # 1 reszty, modulo
print(5 % 2)  # 1
print(4 % 2)  # 0, parzysta

print(wiek ** rok)  # potęgowanie
# 47 ^ 2025
# print(len(wiek ** rok))  # TypeError: object of type 'int' has no len()
print(len(str(wiek ** rok)))  # długośc 3386
# print(len(str(wiek ** rok ** 2)))
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0

# float
# błąd zaokrąglenia
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
print(0.1 + 0.2)  # 0.30000000000000004
#  For example, in a floating-point arithmetic with five base-ten digits,
#  the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# decimal() - pozwala ominąć problem zaokrąglenia

print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308
# , min=2.2250738585072014e-308, min_exp=-1021,
# min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

# typ logiczny
# prawda, fałsz
# True, False
# 1, 0

czy_znasz_pythona = True
print(czy_znasz_pythona)  # True
print(type(czy_znasz_pythona))  # <class 'bool'>, boolean, typ logiczny

# zamienic True, False na liczbę
print(int(True))  # 1
print(int(False))  # 0

print(bool(1))  # True
print(bool(0))  # False

print(bool(100))  # True
print(bool(-100))  # True
print(bool("Radek"))  # True

print(bool(0))  # False
print(bool(""))  # False
print(bool(100 - 100))  # False
print(bool(None))  # False, null, stan nieokreslony, brak wartości, nie wiem, nie ma
