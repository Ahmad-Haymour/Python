# --------------------------
# -- Lists --
#       
#       [+] You can Manipulate Lists in Python Like Arrays in JavaScript
#       [+] List Is NOT Array  => and we have arrays in Python not Like list

#       => myList[ Start : End : Skip ]  =>    IT Will Count the Start Index,
#                                              IT Will NOT Count the End Index,
#                                              Skip Starts from 2

# --------------------------

myAwesomeList = ["One", "Two", "One", 1, 100.5, True]

# myList[Index]       => String
print(myAwesomeList)
print(myAwesomeList[3])
print(myAwesomeList[-1])
print(myAwesomeList[-3])

# myList[Start : End]       => List

print(myAwesomeList[1:4])
print(myAwesomeList[:4])
print(myAwesomeList[1:])

# myList[Start : End : Skip]        => List

print(myAwesomeList[::1])       # Don't Skip    => Whole List
print(myAwesomeList[::2])       # Skip the Next Element
print(myAwesomeList[::3])       # Skip the Next Two Elements

myAwesomeList[2] = "Three"
myAwesomeList[-1] = "False"

print(myAwesomeList)

print(myAwesomeList[0:3:2] )


print(myAwesomeList)
myAwesomeList[1:5] = [2, 3, 4, "Hello"]

print(myAwesomeList)
# myAwesomeList[0:3] = []           => Delete [Start : End]
myAwesomeList[0:4] = ["A-B-C"]
print(myAwesomeList)

# myAwesomeList[0:4] = "A-B-C"  # Every Character is an Element in my List
print(myAwesomeList)


print((",".join(myAwesomeList)))