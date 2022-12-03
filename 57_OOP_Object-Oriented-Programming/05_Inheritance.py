# --------------------------------------------------
# -- Object Oriented Programming => Inheritance --
# --------------------------------------------------

class Food:     # Base Class

    def __init__(self, name, price):

        self.name = name
        self.price = price
        print(f'{self.name} is created from Base Class')

    def eat(self):

        print('Eat Method from Base Class')

#   Inherit all Food Methods in apple Class
class Apple(Food):    # Derived Class

# This init Finction will Override Parameters

    def __init__(self, name, price, amount):

        # Food.__init__(self, name)       # Crete Instance from Base Class
        super().__init__(name, price)            # Crete Instance from Base Class(New Way)

        self.amount = amount

        print(f'{self.name} is created from Derived Class, and Price is: {self.price}, and Amount is: => {self.amount}')

    def get_from_tree(self):

        print(f'Get from tree from Derived Class => {self.price + 20}')

    # def eat(self):
    #
    #     print('This Method will Override the eat() Method from the Base Class Food')

# food_one = Food('Orange', 20)

food_two = Apple('Pizza', 150, 500)
food_two.eat()
print(food_two.name)
food_two.get_from_tree()

print('><'*40)


