# -------------------------------------------------------------
# -- Object Oriented Programming => Class Syntax and Info --
# -------------------------------------------------------------
# [01] Class is the Blueprint or Constructor of the Object
# [02] Class Instantiate Means Crete Instance of a Class
# [03] Instance => Object Created from Class and have their Methods and Attributes
# [04] Class defined with Keyword class
# [05] Class Name written with PascalCase [UpperCamelCase]
# [06] Class may Contain Methods and Attributes
# [07] When Creating Object, Python Look for the Built-In __init__ Method
# [08] __init__ Method Called Every Time You Create Object from class
# [09] __init__ Method is Initialize the Data for the Object
# [10] Any Method with two Underscore in the Start and End Called Dunder or Magic Method
# [11] Self Refer to the Current Instance Created from the Class and must be First Param
# [12] Self can be Named Anything
# [13] In Python you don't need to call new() Keyword to Create Object
# -------------------------------------------------------------
# Syntax =>

# class Name:
#       Constructor=> Do Instantiation [ Create Instance from a Class ]
#       Each Instance is Separate Object
#       def __init__(self):
#           Body Of Function

class Member:

    def __init__(self):

        # pass
        print('A new Member has been Added')


Member()
Member()

print(dir(Member))

member_one = Member()
member_two = Member()
member_three = Member()

print(member_one.__class__)

# -------------------------------------------------------------

my_dictionary = {
    'name': "Ahmad",
    'age': 28,
    'monthly_salary': 5000,
    'yearly_salary': ''  # Something
}