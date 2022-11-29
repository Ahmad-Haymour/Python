#----------------------------------------------#
# -- Doc String & Commenting vs Documenting --
#---------------------------------------------#
# [1] Documentation String for Class, Module or Function
# [2] Can be accessed from the Help and Doc Attributes
# [3] Made for understanding the Functionality of the Complex Code
# [4] There is One Line and Multiple Line Doc String
#---------------------------------------------------

def elzero_function(name):
    # '''This is function to say hello from elzero'''
    """
    Elzero Function
        It say Hello From Elzero
    :param name:
        Person Name that use Function
    :return:
        Return Hello Message to the Person
    """
    print(f'Hello {name} from Elzero')

elzero_function('Ahmad')

print(dir(elzero_function))       #   => dir( )  to see the attributes of something and what contains

print(elzero_function.__dir__)

print(elzero_function.__doc__)      # Print the Document in this Function
print('><'*40)
help(elzero_function)               # Print the info about my Function and its Document
