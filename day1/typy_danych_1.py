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
