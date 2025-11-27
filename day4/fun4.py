# funkcja wewnętrza, funkcja zagnieżdzona
# dekorator - wykorzystuje zasady funkcji zagnieżdzonej

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    # fun2() uruchomienie funkcji
    return fun2  # zwracamy adres funkcji


fun1()
print(fun1())  # <function fun1.<locals>.fun2 at 0x000002580A077480>
xfun = fun1()
print(xfun)  # <function fun1.<locals>.fun2 at 0x00000233699F7480>
print(type(xfun))  # <class 'function'>
xfun()  # uruchomienie fun2
xfun()
# To jest fun2
# To jest fun2
