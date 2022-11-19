# ------------------------------
#         -- Boolean --

#    -- Boolean Operators --
#[ == , != , <=]

#       1- and    ( && )       =>  All Conditions Must Be Met
#       2- or     ( || )       =>  IF Met One Condition or More
#       3- not    ( !  )       =>  Reverse Boolean
# ------------------------------

name = ""
print(name.isspace())
print(100 > 200)
print(100 > 200)
print(100 > 90)

print('='*50)

## True Values

print(bool("Ahmad"))
print(bool(100))
print(bool(10.50))
print(bool(True))
print(bool([1, 2, 3, 4, 5]))

print('='*50)
## False Values

print(bool(0))
print(bool(''))
print(bool(""))
print(bool(False))
print(bool([]))             #  List
print(bool(()))             #  Tuple
print(bool({False}))        #  Dictionary
print(bool(None))           #  Like (null) in JavaScript is also False

print('='*50)

## Boolean Operators ( and, or, not )

age = 30
name = "Shark"
rank = 10

## and
print(age >18 and name == "Shark" and rank > 8)         # True
print(age >18 and name == "Shark" and rank > 20)        # False
print('='*50)

## or
print(age > 50 or name == "Ahmad" or rank > 10)         # False   
print(age > 50 or name != "Shark" or rank > 11)          # True
print('='*50)

## not
print(age > 18)             # True
print(not age > 18)         # False => Not True  (Reverse Boolean)