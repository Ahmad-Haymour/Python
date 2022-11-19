# ------------------------
# -- Strings Methods 4 --

#       1- replace('x', 'y')            => Find X in my String => Replace it with Y
#          replace('x', 'y', num)       => num With How many X

#       2- "Char".join( List )          => Make a String From List (Array) => Put a Character between Values
#          
# ------------------------

# replace( Old value, New Value, Count )

a = "Hello One Two Three One One"
print(a.replace("One", "1"))
print(a.replace("One", "X", 1))
print(a.replace("One", "NoOne", 2))

print('#--------------------------------------------------#')

# "Char".join( Iterable ) => Iterable is a list u can loop

myList = ["World", "Of", "Warcraft"]

print( "-".join(myList) )
print( " ".join(myList) )
print( ", ".join(myList) )
print( type(",".join(myList)) )