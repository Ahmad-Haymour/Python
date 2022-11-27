#-------------------------------------#
#       -- Decorators => Intro -- 
#-------------------------------------#
# [1] Sometimes calls Meta programming
# [2] Everything in Python is Object even Functions
# [3] Decorator take a Function and add some Functionality and Return it
# [4] Decorator wrap other function and Enhance their behavior
# [5] Decorator is High Order Function ( Function Accept Function as Parameter)
#-----------------------------------------------------------------------------


def myDecorator(func) :

    def nestedFunction():

        print("before my Function")

        func()

        print("after my Function")
    
    return nestedFunction

@myDecorator                # => Add @Decoration Function before defining a function To Decorate it Automatically
def say_hello():
    print("Hello Someone")


def say_howAreYou():
    print("How are you Someone?")

say_hello()        #  =>  Decorated Function
say_howAreYou()    #  =>  Decorated Function

print('><'*40)

## Dont use this stupid way :) , Return Same thing
# myDecorator(say_hello())
