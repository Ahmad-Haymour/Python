#-------------------------------------#
#           -- Generator -- 
#-------------------------------------#

# [1] Generator is a function with "yield" Keyword Instead of "return"
# [2] It Support Iteration and Return Generator Iterator By Calling "yield"
# [3] Generator Function can have one or more "yield"
# [4] By using next() it Resume from where it Called "yield" Not from Beginning
# [5] When called, it's not start Automatically, its only give you the Control
#-----------------------------------------------------------------------------

# def myFunction():
#     return 1

# print(myFunction())

print('><'*40)

def myGenerator():

    yield 1
    yield 2
    yield 3
    yield 4

# print(myGenerator())

myGen = myGenerator()

print(next(myGen))
print('Hello')
print(next(myGen))
print('I\'m Python')
print(next(myGen))
print('Generator')
print(next(myGen))

print('><'*40)

for number in myGen :           #   => myGen is Empty because we used next() Method on all our Iteration,
    print(number)               #   => It start loop from the last time used next(), never from beginning

print('><'*40)

for number in myGenerator() :       # =>    It Show all our yields because we didn't use this Function before, otherwise it Resume from next() Method
    print(number)