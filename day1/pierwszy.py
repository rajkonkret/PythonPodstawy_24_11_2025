# https://peps.python.org/pep-0008/
# https://kariera.comarch.pl/blog/clean-code-15-krokow-do-stworzenia-czystego-kodu/
# snake_case - konwencja nazewnicza
import sys

print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print()
# ctrl alt l - formatowanie kodu
print()  # wypisz/wydruk

print("Radek")  # Radek
print('Radek')  # Radek

# ctrl / - dodawanie komentarza
# print('Radek")
#   File "C:\Users\CSComarch\PycharmProjects\PythonPodstawy_24_11_2025\day1\pierwszy.py", line 19
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 19)
#
# Process finished with exit code 1 - program  zakończył się z błedem
print("Dalsza część programu")  # Dalsza część programu

print("Radek \"Radek\"")  # Radek "Radek"

# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'>, string, teksty

print("39" + "39")  # 3939, konkatenacja, łaczenie teksty
print(39 + 39)  # 78
print(type(39))  # <class 'int'>, integer, całkowite

print(sys.int_info)
# sys.int_info(bits_per_digit=30,
# sizeof_digit=4,
# default_max_str_digits=4300,
# str_digits_check_threshold=640)

# print(39 + "39")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# rzutowanie typów, zamiana
print(int("39"))  # rzutowanie, int(), 39
print(39 + int("39"))  # 78

print(str(39))  # str() - rzutoeanie na string
print(str(39) + "39")  # 3939

print(5 * "4")  # 44444
# 168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168
print("168" * 35)

print(int("168") * int(35))  # 5880
# print(int('A'))  # ValueError: invalid literal for int() with base 10: 'A'

# zmienna - pudełko na dane
# snake_case
# nazwa zmiennej powinna podpowiadac co przechowuje

# typowanie dynamiczne
# typ na podstawwie zawartości
name = "Radek"
print(name)  # wyswietlenie zawartości zmiennej
print(type(name))  # <class 'str'>

name = 90
print(name)
print(type(name))  # <class 'int'>

# print(name + "Kowalski") # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# podpowiedzi typów
name: str = "Radek"
print(type(name))  # <class 'str'>

name = 90
print(name)  # 90
# mypy - sprawdzanie użycia typów
# pip - menadżer pakietów pythona
#  pip install mypy
#  cd .\day1\ - przejscie do katalogu
#  mypy .\pierwszy.py
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonPodstawy_24_11_2025\day1> mypy .\pierwszy.py
# pierwszy.py:71: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# pierwszy.py:78: error: Name "name" already defined on line 67  [no-redef]
# pierwszy.py:81: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# Found 3 errors in 1 file (checked 1 source file)