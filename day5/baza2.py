import sqlite3

try:
    conn = sqlite3.connect('baza_danych.db')
    print("Baza danych została podłaczona")

    query = """CREATE TABLE IF NOT EXISTS developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    salary REAL NOT NULL);"""


    c.execute(query)
    conn.commit()


except sqlite3.Error as e:
    print("Bład podłaczenia z bazą:", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zosyało zamknięte")
# https://sqlitebrowser.org/