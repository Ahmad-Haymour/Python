# --------------------------
#        -- Set --
# --------------------------

## Not Ordered and Not Indexed

mySetOne = {"Ahmad", "Sam", 100}
print(mySetOne)
# print(mySetOne[0])            =>  Cannot be indexed

## Slicing Cannot be Done
mySetTwo = {1, 2, 3, 4, 5, 6}
myTuple = ( 1, 2, 3, 4, 5, 6)

# print(mySetTwo[0:3])          =>  Cannot Slice Set
print(myTuple[0:3])

## Has Only Immutable Data Types

# mySetThree = {"Ahmad", 100, 22.52, True , [1, 2, 3]}      => Unhashable Type: "List"      => Set Cannot have List Element 
mySetThree = {"Ahmad", 100, "Ahmad", 22.52, True, (1, 2, 3) }   # => It Will Delete Each Value Match another Values (Unique)

print(mySetThree)

## Items is Unique

mySetFour = {1, 2, "A", "A", "A", "B"}
print(mySetFour)