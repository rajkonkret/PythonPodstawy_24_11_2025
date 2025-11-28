# baza danych - system przechowywania danych
# silnik - mechanizm zarządzania danymi w bazie
# sql, nosql, relacyjne, nierelacyjne
# sqlite, mysql, postgress, oracle, mssql
import sqlite3

try:
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    print("Baza danych została podłaczona")
except sqlite3.Error as e:
    print("Bład podłaczenia z bazą:", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zosyało zamknięte")
