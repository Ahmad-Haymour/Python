#-----------------------------------------#
# -- Function Parameters and Arguments -- #
#-----------------------------------------#

# *- def             ==>  ( Define ) Function Keyword
# *- say_hello()     ==>  Function Name
# *- name            ==>  Parameter
# *- print(hello{n})  =>  Task
# *- say_hello(Ahmad) =>  Argument

def say_hello(n):
    print("Hello {}".format(n))

say_hello("Ahmad")

print('><'*50)

## Integers

def addition(n1, n2) :

    if type(n1) != int or type(n2) != int:
        print('Only integers allowed')
    else :    
        print(n1 + n2)

addition( 100, "asb")

print('><'*50)

## Parameters

def full_name(first, middle, last) :
    print("Hello {} {} {}".format(first.strip().capitalize(), middle.upper(), last.capitalize()))

full_name('Ahmad', "A", "Haymour")

print('><'*50)

## Default Parameters

def greetings(name, age = "Unknown", country = "Unknown") :

    print("Hello {}, your Age is => {}, and your Country is => {}".format(name, age, country))

greetings("Ahmad", 28, "Syria")
greetings("Ahmad", 28)
greetings("Ahmad")