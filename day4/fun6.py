# stworzyć funkcję obliczającą średnią
def srednia(*cyfry):  # dowolna ilośc argumentów pozycyjnych
    print(cyfry)

    count = len(cyfry)
    suma = 0
    try:
        for c in cyfry:
            suma += c

        avg = suma / count
    except Exception as e:
        print("Błąd:", e)
    else:
        print(f"Średnia wynosi: {avg}")
    finally:
        print("Następny uczeń")


srednia()  # ()
srednia(1, 2)  # (1, 2)
srednia(1, 2, 3)  # (1, 2, 3)
srednia(1, 2, 3, 4)  # (1, 2, 3, 4)
