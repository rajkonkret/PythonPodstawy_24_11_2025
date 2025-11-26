# działania z plikami
# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
# filehandler
# context manager
# with - kontekst manager
with open("test.log", "w") as f:
    f.write("Powitanie\n")

# FileExistsError: [Errno 17] File exists: 'test.log'
# x - gdy plik istnieje bład
# with open("test.log", "x") as f:
#     f.write("Powitanie\n")

with open("test.log", "w") as f:
    f.write("Parametr1\n")
    f.write("Parametr2\n")
    f.write("Parametr3\n")
    f.write("Parametr4\n")

# a - dodanie do istniejącego pliku
with open("test.log", "a") as f:
    f.write("Dodane\n")
    f.write("Dodane2\n")
    f.write("Dodane3\n")
    f.write("Dodane4\n")

with open('test.log', "r") as file:
    lines = file.read()

print(lines)
# Parametr1
# Parametr2
# Parametr3
# Parametr4
# Dodane
# Dodane2
# Dodane3
# Dodane4
