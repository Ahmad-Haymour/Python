# ------------------------------
#     -- Type Conversion --
#                                   =>  Need Iterable Loop Value (Not Number Cuz Unhashable)
#       1- str()
#       1- tuple()
#       1- list()
#       1- dict()               => We Always Need a Key & Value 
#                               => Strings & Sets are Unhashable by Dictionaries
# ------------------------------

# str()         =>      String

a = 10
print(type(a))
print(type(str(a)))

## tuple()      => Need Iterable Loop Value Not Number

c = "Ahmad"          # String
d = [1, 2, 3, 4, 5]  # List
e = {"A", "B", "C"}  # Set (Never Sorted)
f = {"A": 1, "B": 2} # Dictionary

print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))
# print(tuple(500))  => Error Cuz Cannot Loop Numbers
print('='*50)

## List()      =>       List

c = "Ahmad"          # String
d = (1, 2, 3, 4, 5)  # Tuple
e = {"A", "B", "C"}  # Set (Never Sorted)
f = {"A": 1, "B": 2} # Dictionary

print(list(c))
print(list(d))
print(list(e))
print(list(f))

print("="*50)


## set()      =>        Set

c = "Ahmad"          # String
d = (1, 2, 3, 4, 5)  # Tuple
e = ["A", "B", "C"]  # List 
f = {"A": 1, "B": 2} # Dictionary

print(set(c))
print(set(d))
print(set(e))
print(set(f))

print("="*50)


## dict()      =>       Dictionary Need { Key : Value }  Or It Wouldn't Work

##             =>   Set Is Unhashable. It Wont Work with Dictionaries

# c = {"Ahmad"}          # String     No Value Won't Work

d = (1, 2, 3, 4, 5)  # Tuple
d = (("A", 1), ("B", 2), ("C", 3))

e = ["A", "B", "C"]  # List 
e = [["One", 1], ["Two", 2], ["Three", 3]]  # List 

# f = {"A": 1, "B": 2} # Dictionary

# print(dict(c))        => String Unhashable
print(dict(d))
print(dict(e))
# print(dict(f))        => Set Unhashable