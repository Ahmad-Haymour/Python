## Function Without () => Means Return all Data
#   Write your Function in Decoration Parameter, and your Function Parameters in Nested Decoration Function and in your Function in Nested Function from Decoration
def myDecoration(func):

    def nestedFunc():

        print("Before Function")

        func()

    return nestedFunc()

@myDecoration
def say_hello():
    print('Hello there...')


say_hello

def testDecoration(func):

    def nestedFunc(num1, num2):

        if num1 <= 10 or num2 <= 10:
            print("Beware the Number is less or equal than 10")
        print("Before Test Function with Parameter")

        func(num1, num2)

    return nestedFunc       # Return All Data

def lastDecorator(func):
    def nested(num1, num2):
        print('Heeey, from Last Decorator')
        func(num1, num2)
    return nested
@testDecoration
@lastDecorator
def calc(n1, n2):
    print(n1 + n2)

calc(10 , 20)