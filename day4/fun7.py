def connect(**opcje):  # *8 dowolna ilość argumntów nazwanych (keywords) słownikowe
    print(opcje)


connect()
connect(a=100)  # {'a': 100}
connect(a=100, b=89, c=90, name="Radek", age=50)
# {'a': 100, 'b': 89, 'c': 90, 'name': 'Radek', 'age': 50}


