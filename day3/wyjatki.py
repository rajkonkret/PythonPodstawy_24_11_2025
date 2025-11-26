# wyjątki - błedy w wykonywaniu kodu

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PythonPodstawy_24_11_2025\day3\wyjatki.py", line 1, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

# obsługa wyjątków
# try - except - [else - finally]
try:
    # print(5 / 0)
    # int("A")
    # print("A" * "23")
    # raise KeyError("Brak klucza")  # rzucenie wyjątku
    wynik = 90 / 3
except ZeroDivisionError:
    print("Nie dziel przez zero")
except ValueError:
    print("Bład wartości")
except TypeError:
    print("Błąd typu")
except Exception as e:  # pozostałe błedu
    print("Błąd:", e)
else:  # gdy nie mabłędu
    print("Wynik:", wynik)
finally:  # wykona sie zawsze
    print('Kolejny element')

print("Dalszy ciąg programu")
# Nie dziel przez zero
# Dalszy ciąg programu
#
# Process finished with exit code 0
# Błąd:
# Dalszy ciąg programu
# Błąd: 'Brak klucza'
# Dalszy ciąg programu
# Wynik: 30.0
# Kolejny element
# Dalszy ciąg programu
