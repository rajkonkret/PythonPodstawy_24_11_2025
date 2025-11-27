# stworzyć funkcję obliczającą średnią
def srednia(name=None, *cyfry):  # dowolna ilośc argumentów pozycyjnych
    print(cyfry)

    count = len(cyfry)

    suma_p = sum(cyfry)
    suma = 0
    try:
        for c in cyfry:
            suma += c

        avg = suma / count
        avg_p = suma_p / count
    except Exception as e:
        print("Błąd:", e)
    else:  # gdy nie ma błedu
        print(f"Średnia dla ucznia: {name}, wynosi: {avg}")
        print(f"Średnia dla ucznia: {name}, wynosi: {avg_p}")
    finally:  # wykona się zawsze
        print("Następny uczeń")


srednia()  # ()
srednia(1, 2)  # (1, 2)
srednia(1, 2, 3)  # (1, 2, 3)
srednia(1, 2, 3, 4)  # (1, 2, 3, 4)
