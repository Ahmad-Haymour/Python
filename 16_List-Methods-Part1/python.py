# --------------------------
# -- Lists Methods Part 1 --

#       1- .append()         =>  Same as .push() in JavaScript
#                            =>  You can also append a List [1, ["a", "b"]]
#       2- .extend()         =>  Put the List Elements next to my List Elements
#       3- .remove()         =>  Delete First Element Match
#       4- .sort()           =>  Sort my List witch has Only One Type Elements (NOT All Types)
#           list.sort(revered=True)     =>  Reverse Sort  (Default is: reversed=False)
#       5- .reverse()        =>  Reverse my List, No Sort and Accept All Types
# --------------------------

## append()

myFriends = ["Ahmad", "Ali"]
myOldFriends = ["Sam", "Sally", "Moon"]

myFriends.append("Suzan")
myFriends.append("Steve")
myFriends.append(22)
myFriends.append(True)
myFriends.append(myOldFriends)

print(myFriends)

# Reach an Element in Lists like in JavaScript
print(myFriends[2])
print(myFriends[6][2])

## extend()     => myList next to another List

a = [1, 2, 3]
b = ["A", "B", "C"]
c = ["One", "Two"]

a.extend(b)
a.extend(c)

print(a)

## remove()

x = [1, 2, 3, 4, 5, "Ahmad", True, "Ahmad", "Ahmad"]
x.remove("Ahmad")

print(x)

## sort()   Only One Type Elements

y = [1, 2, 100, 120, -10, 17, 29]
# y = ["A", "Z", "C"]

y.sort(reverse = True)

print(y)

# reverse() 

z = [10, "A", False, 80, 100, "Sally"]
z.reverse()

print(z)