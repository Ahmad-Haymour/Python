# ----------------------------------------------------------
# -- Object Oriented Programming => Multiple Inheritance --
# ----------------------------------------------------------
#   Class.mro()     =>
class BaseOne:

    def __init__(self):

        print('Base One')

    def func_one(self):

        print('One')
class BaseTwo:

    def __init__(self):

        print('Base Two')

    def func_two(self):
        print('Two')


class Derived(BaseOne, BaseTwo):

    pass


my_var = Derived()
print(Derived.mro())
print('><'*50)
print(my_var.func_one)
print(my_var.func_two)
print('><'*50)

my_var.func_one()
my_var.func_two()

print('><'*50)

class Base:

    pass

class DerivedOne(Base):
    '''
        This Class will inherit all Attributes and Methods from Base Class
        Has Base
    '''
    pass

class DerivedTwo(DerivedOne):
    '''
        This Class will inherit all Attributes and Methods from DerivedOne Class and its inherits Classes, like Base Class
        Has DerivedOne and Base
    '''
    pass