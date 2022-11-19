# ------------------------
#   Strings Indexing and Slicing
#       1- All Data in Python is Object
#       2- Object Contain Elements
#       3- Every element has its own Index
#       4- Python use Zero based Indexing ( Index start from Zero )
#       5- Use Square Brackets to access Element
#       6- Enable Accessing parts of Strings, Tuples or Lists
# ------------------------

# Indexing ( Access Single Item )

myString = "I Love Python"

print(myString[0])
print(myString[9])

print(myString[-1])
print(myString[-6])

print('#--------------------------------------------------#')

# Slicing  ( Access Multiple Sequence Items )
# [ Start : End ]  => (End "not" include)
# [ Start : End : Steps ]

print(myString[2:6])
print(myString[7:13])

print(myString[:10])   #  =>  Start default is: Zero
print(myString[2:])    #  =>  Go to the End

print(myString[:])     #  => Full Data

print(myString[::1])   #  => Full Data

print(myString[::2])   #  => Full Data ( Slice (Skip) Even indexes)