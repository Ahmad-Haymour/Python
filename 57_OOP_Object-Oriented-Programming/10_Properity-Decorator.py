# ----------------------------------------------------------
# -- Object Oriented Programming => @Property Decorator --
# ----------------------------------------------------------
# - Change Method to Property Variable
# ----------------------------------------

class Member:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def say_hello(self):

        return f'Hello {self.name}'

    @property
    def age_in_days(self):

        return self.age * 365


myClass = Member('Ahmad', 28)

print(myClass.name)
print(myClass.age)
print(myClass.say_hello())
# print(myClass.age_in_days())

print(myClass.age_in_days)