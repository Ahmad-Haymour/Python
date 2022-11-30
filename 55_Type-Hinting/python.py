# -------------------------------------------
#           -- Type Hinting --
# -------------------------------------------
# Hinting do nothing to your code, return Nothing in Console, you just write the type that you'll return

def say_hello(name) -> str:

    print(f'Hello {name}')
    return name

say_hello('Ahmad')

def calc(n1, n2) -> int:

    print(n1 + n2)

calc(2, 6)

def max_number(myList) -> list:

    print(myList)

max_number(max([100,20,4,70,33]))