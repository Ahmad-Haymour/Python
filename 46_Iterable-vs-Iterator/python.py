#-------------------------------------#
#     -- Iterable vs Iterator -- 
#-------------------------------------#
# Iterable
# [1] Object contains data that can be Iterated Upon
# [2] Examples (String, List, Set, Tuple, Dictionary)
#-------------------------------------#
# Iterator
# [1] Object used to Iterate Over Iterable Using Using next() Method Return 1 Element at a Time
# [2] You can Generate Iterator from Iterable when Using iter() Method
# [3] For Loop Already calls iter() Method on the Iterable Behind the Scene
# [4] Gives "StopIteration" IF there is No Next Element



myString = "Ahmad"
myList = [1, 2, 3, 4, 5]

# for letter in myString:
#     print(letter)

# for num in myList:
#     print(num)


# print(next(myString))         =>  Error myString Must be Iterator
#                               =Y By calling next() it Resume from where it called Last Time not from the Beginning

# myIterator = iter(myString)

# print(myIterator.next())
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))     #  => Iterator is over => Error "StopIteration"


## iter()     => its Default in Loop, python add it always behind the scene

for letter in iter("Shark") :

    print(letter)