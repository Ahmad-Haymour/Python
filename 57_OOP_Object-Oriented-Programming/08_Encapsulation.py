# ---------------------------------------------------
# -- Object Oriented Programming => Encapsulation --
#   classVariable._ClassName__AttributeName
# ----------------------------------------------------
# Encapsulation
# - Restrict Access to the Data Stored in Attributes and Methods
# ----------------------------------------------------
# Public    ->  Access & Modified
# - Every Attributes and Method that we used so far is Public
# - Attributes and Methods can be Modified and Run frm Everywhere
# - Inside our/Outside the Class
# ----------------------------------------------------
# Protected    ->  Access & Modified
# - Attributes and Methods can be accessed from within the Class and Sub Classes(Derived)
# - Attributes and Methods Prefixed with one Underscore _name
# ----------------------------------------------------
# Private
# - Attributes and Methods can be accessed from within the Class or Object Only
# - Attributes cannot be Modified from Outside the Class
# - Attributes and Methods Prefixed with two Underscore __name
# ----------------------------------------------------
# - Attributes = Variables = Properties

# class Member:
#
#     def __init__(self, name):
#
#         self.name = name    # [Public]  =>  It can be accessed and modified inside or outside the class
#
#
# one = Member('Ahmad')
# print(one.name)
# one.name = 'Osama'
# print(one.name)

# class Member:
#
#     def __init__(self, name):
#
#         self._name = name    # [Protected]  =>  It can be accessed and modified inside or outside the class
#                                             - Protected Only Hide Suggestion
#
# one = Member('Ahmad')
# print(one._name)
# one._name = 'Osama'
# print(one._name)

class Member:

    def __init__(self, name):

        self.__name = name    # [Private]   =>

    def say_hello(self):

        print(f'Hello {self.__name}')

one = Member('Ahmad')
# print(one.__name)     => Error - AttributeError -  => You cant access it normally, it cannot be Modified without Getter and Setter Methods
one.say_hello()
print(one._Member__name)        #   => This is How to access Private Attribute