import random

# działania na liczbach losowych

"""Return random integer in range [a, b], including both end points.
       """
print(random.randint(1, 100))  # int, od 1 do 100

print(random.randrange(1, 100))  # int, od 1 do 99
print(random.randrange(5))  # 3, int od 0 do 4

print(random.random())  # 0.9644083894862632, od 0 do 0.9999999
print(random.random() * 6)  # 1.2286307452759664, od 0 do 5.9999999
print(round(random.random() * 6))  # 5

lista = [67, 45, 32, 68, 90, 42, 69]
print(lista[random.randrange(len(lista))])  # 67

print(random.choice(lista))  # 68

lista_kule = list(range(1, 50))  # od 1 do 49
# print(lista_kule)

wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)

print(random.choices(lista_kule, k=6))  # [2, 43, 43, 4, 13, 21], losuje z powtórzeniami
print(random.sample(lista_kule, 6))  # [34, 14, 43, 36, 20, 39]
print(random.sample(lista_kule, k=6))  # [37, 7, 30, 40, 34, 29], bez powtórzeń
