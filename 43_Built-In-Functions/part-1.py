#-----------------------------------#
#  -- Built In Functions Part 1 --  #
#-----------------------------------#
#   [1]- all()          =>      Return True If (ALL) Values Are (True) in the ( Iterable )
#   [2]- any()          =>      Return True If (ANY) Values Are (True) in the ( Iterable )
#   [3]- bin()          =>      Change the Value to My Computer Language so it can be readable from my Computer
#   [4]- id()           =>      (Print ID),Every Element or Value in Python has a Different ID Number 
#------------------------------

x = [1, 2, 3, 4, 0]         # => 0 == False

if all(x) :
    print("All Elements are True")
else :
    print("There is at Least One Element is False")

print('><'*40)

##  any()

x = [0, 0, None, [], 0]

if any(x) :
    print("There is at least one Element is True")
else :
    print("There is no any True Elements")
    print(bool(-1))

print('><'*40)

## bin()        => Binary

print(bin(100))

print('><'*40)

## id()     =>  

a = 1
b = 2

print(id(a))
# print(bin(a))
print(id(b))
# print(bin(b))