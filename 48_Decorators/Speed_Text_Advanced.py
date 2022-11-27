# -------------------------------------#
#    -- Decorators => Speed Test --
#   *- Import Time Module to Calculate Functions Time
# -------------------------------------#

def decorator(func):
    def nestedFunc(*numbers):
        print('Function Started')

        for number in numbers:
            if number < 2 or number > 28 :
                print("Beware you have numbers less than Two or more than 28!")
                func(*numbers)
                print('If Condition Match')
                return

        func(*numbers)
        print('Decorate Done')
    return nestedFunc


@decorator
def calc(n1, n2, n3, n4):
    print(n1 + n2 + n3 + n4)


calc(10, 21, 20, 1)
print('><' * 40)

# import time
from time import time

print(dir(time()))

print('><' * 40)

## Speed Test

def speedTest(func):


    def wrapper():
        print('Wrapper Function Started')
        start = time()
        func()
        end = time()
        print(f"Function Time is => {end - start}")

    return wrapper

@speedTest
def bigLoop():
    for n in range(1, 2229984):
        print(n)

bigLoop()
print('><' * 40)
