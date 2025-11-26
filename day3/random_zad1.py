import random

# działania na liczbach losowych

"""Return random integer in range [a, b], including both end points.
       """
print(random.randint(1, 100))  # int, od 1 do 100

print(random.randrange(1, 100))  # int, od 1 do 99
print(random.randrange(5))  # 3, int od 0 do 4

print(random.random())  # 0.9644083894862632, od 0 do 0.9999999
print(random.random() * 6)  # 1.2286307452759664, od 0 do 5.9999999


