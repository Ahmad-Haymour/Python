# -----------------------------------------------------------------
# -- Object Oriented Programming => ABCs => Abstract Base Class --
# -----------------------------------------------------------------
# - Class called abstract class if it has one or more abstract methods
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Class
# - By adding @abstractmethod Decorator on the Methods
# - ABCMeta Class is a metacass used for Defining Abstract Base Class
# ----------------------------------------------------------------------------------------

from abc import ABCMeta, abstractmethod


class Programming(metaclass=ABCMeta):

    @abstractmethod
    def has_oop(self):      #   This Method must run on Derived Classes

        pass


class Python(Programming):

    def has_oop(self):

        return 'Yes'


class Pascal(Programming):

    def has_oop(self):

        return 'NO'


# one = Programming()
two = Python()
three = Pascal()

print(two.has_oop())
print(three.has_oop())