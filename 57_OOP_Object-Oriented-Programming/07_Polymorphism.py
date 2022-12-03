# ---------------------------------------------------
# -- Object Oriented Programming => Polymorphism --
# ----------------------------------------------------

n1 = 10
n2 = 20

print(n1 + n2)

s1 = "Hello"
s2 = "Python"

print(s1 + ' ' + s2)

print(len([1, 2, 3, 4, 5, 6]))
print(len("Ahmad Haymour"))
print(len({'Key_One': 1, 'Key_Two': 2}))

class A:

    def do_something(self):

        print('From Class A')

        '''Raise NotImplemented Error Mean => You Must Implement this Method In the Diverded Class'''
        raise NotImplementedError("Derived Class Must Implement this Method")

print('><'*50)
class B(A):

    def do_something(self):

        print('From Class B')

class C(A):

    """You Must Implement Method do_something(), else you recieve NotImplementedError with your Message"""
    pass

# my_instance = B()

my_instance = C()
my_instance.do_something()