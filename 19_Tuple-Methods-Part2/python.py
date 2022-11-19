# --------------------------
# -- Tuple Methods Part 2 --
#       [a, b, _, d]  => Underscore mean ignore
# --------------------------

## Tuple With One Element

myTuple1 = "Ahmad"          #  => String 
myTuple2 = ("Ahmad")        #  => String

print(myTuple1)
print(myTuple2)
print(type(myTuple1))
print(type(myTuple2))

myTuple3 = "Sally",          #  => Tuple 
myTuple4 = ("Sally",)        #  => Tuple

print(myTuple3)
print(myTuple4)
print(type(myTuple3))
print(type(myTuple4))

print(len(myTuple1))    # String Length
print(len(myTuple4))    # Tuple Length

## Tuple Concatenation

a = (1, 2, 3, 4)
b = (5, 6)
c = a + b
d = a + ("A", "B", True) + b

print(c)
print(d)

## (*Repeat) Tuple, List, String Repeat (*)

myString = "Ahmad"
myList = [1, 2, 3]
myTuple = "A", "B"

print(myString * 5)
print(myList * 3)
print(myTuple * 2)

## count()

a = 1, 3, 7, 8, 2, 6, 5, 8
print(a.count(8))

## index()

b = 1, 3, 7, 8, 2, 6, 5

# print("The Position of Index is: " + b.index(7))              =>  Error Data Type 
print("The Position of Index is: %d" % b.index(7))            # =>  Old Way   

print("The Position of Index is: {:d}" .format(b.index(7)))   # =>  New Way
# print(f"The Position of Index is: {b.index(7)}")              =>  Error NOt Working!!!

# Tuple Destruct

a = ("A", "B", 4, "C")

x, y, _, z = a      #  _ Ignore 4. Else Error

print(x)
print(y)
print(z)