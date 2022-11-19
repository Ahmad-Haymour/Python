# --------------------------
# -- Tuple Methods Part 1 --

#   ( You Cannot Add, Edit, Delete or any Update )
#       1- Tuple Items are enclosed in Parentheses => ()
#       2- You can remove the Parentheses () if u want
#       3- Tuple are Ordered, to Use Index to Access Item
#       4- Tuple are Immutable => You Cannot Add or Delete
#       5- Tuple Items is NOT Unique
#       6- Tuple can have Different Data Types
#   Important:
#       7- (Operators used in "Strings" and "Lists" Available in "Tuples")
# --------------------------

## Tuple Syntax

myTupleOne = ("Ahmad", "Sally")
myTupleTwo = "Ahmad", "Sally"

print(myTupleOne)
print(myTupleTwo)

print(type(myTupleOne))
print(type(myTupleTwo))

## Tuple Indexing

myTupleThree =(1, 2, 3, 4, 5)
print(myTupleThree[0])
print(myTupleThree[-1])
print(myTupleThree[2])

# Tuple Assign Values       => Cannot Assign(Edit) any Value

myTupleFour = (1, 2, 3, 4, 5)
# myTupleFour[2] = "Three"
# myTupleFour[2] = 5
# myTupleFour = [] 

print(myTupleFour)

## Tuple Items

myTupleFive = ("Ahmad", "Ahmad", 1, 2, 3, 100.5, True )
print(myTupleFive[0])
print(myTupleFive[-1])