# dekorator
# przyjmuje inna fukcje jako argument
# wykorzystuje konstrukcje funkcji wew
from colorama import init, Fore, Style

init(autoreset=True)


#  pip install colorama
def dekor(fun):
    def wew():
        print("Dekorujemy")
        return fun()

    return wew


def color_decorator(fun):
    def wrapper():
        result = fun()
        return Fore.RED + result + Style.RESET_ALL

    return wrapper


@dekor
def hej():
    print("Hej!!")


hej()  # Hej!!


# Dekorujemy
# Hej!!

@color_decorator
def napis():
    return "HELLO WORLD!!"


print(napis())
