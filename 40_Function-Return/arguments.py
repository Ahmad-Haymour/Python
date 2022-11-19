#---------------------------------------------#
# -- Function Packing, Unpacking Arguments -- #

#   *- *Args        => to Unpack All Arguments
#   *- *myFourParameters(*peoples)    => Like myFunction(...arguments) in (JS)
#---------------------------------------------#

##  Unpack Arguments    = *myList
myList = [1, 2, 3, 4]

print(myList)
# print(*myList)     => Error ( It should be unpacking myList )!

def say_hello(*peoples) :       # (n1, n2, n3, n4) || Instead of Arguments

    # peoples = [ n1, n2, n3, n4]

    for name in peoples :
        print('Hello {}'.format(name))

say_hello("Ahmad", "Sally", "Sam", "Mark", "Lara")

print("><"*40)
## Example

def show_details(name, *skills):

    print("Hello {} your Skills is: {}".format(name, skills))
    print("Hello {} your Skills is:".format(name))

    for skill in skills :
        print("*- {}".format(skill))

show_details("HTML", "CSS", 'Python', "JAVA")
show_details("John", "PHP", "SCSS", 'React', "JS")