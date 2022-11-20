#---------------------------------------------#
# -- Function Packing, Unpacking Arguments -- #

#   *- *Args        => to Unpack All Arguments  => Tuple
#   *- **Args       => to Unpack All Arguments  => Dictionary

#   *- *myFourParameters(*peoples)    => Like myFunction(...arguments) in (JS)
#---------------------------------------------#

##  Unpack Arguments  [ List ]   = *myList
myList = [1, 2, 3, 4]

print(myList)
# print(*myList)     => Error ( It should be unpacking myList )!

##  Unpack Arguments  [ Tuple ] 

def say_hello(*peoples) :       # (n1, n2, n3, n4) || Instead of Arguments

    # peoples = [ n1, n2, n3, n4]

    for name in peoples :
        print('Hello {}'.format(name))
        print(type(name))
        print(type(peoples))


say_hello("Ahmad", "Sally", "Sam", "Mark", "Lara")

print("><"*40)

## Example

def show_details(name, *skills):

    print("Hello {} your Skills is: {}".format(name, skills))
    print("Hello {} your Skills is:".format(name))

    for skill in skills :
        print("*- {}".format(skill))

show_details("Ahmad", "CSS", 'Python', "JAVA")
show_details("John", "PHP", "SCSS", 'React', "JS")

print("><"*40)

## Unpacking Arguments [ Dictionary ]

## We become a Dictionary look like this Dictionary below =>

mySkills = {
    "Html" : '10%',
    "Css" : "8%",
    "Python" : "5%",
    "JS" : "7%"
}

def show_skills(**skills) :

    print(skills)
    print(type(skills))

    for skill, value in skills.items() : 
        print("{} => {}".format(skill, value))

show_skills( Html = '100%', Css = "80%", Python = "50%", JS = "70%")

print("><"*40)
print(mySkills)
print("><"*40)
show_skills(**mySkills)