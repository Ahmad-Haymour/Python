# -------------------------------------------------------
# -- Object Oriented Programming => Getters & Setters --
# -------------------------------------------------------
# - Get and Set Methods are used to Modified Private Attributes
# --------------------------------------------------------------

class Member:

    def __init__(self, name):

        self.__name = name      # Private

    def say_hello(self):

        return f'Hello {self.__name}'


    def get_name(self):     # Getter

        return self.__name

    def set_name(self, new_name):   # Setter

        self.__name = new_name

one = Member('Ahmad')

print(one._Member__name)

print(one.get_name())

one.set_name('Mark')
print(one.get_name())
