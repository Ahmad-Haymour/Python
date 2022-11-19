# --------------------------
#  -- Set Methods Part 2--

#       1- .difference(b, c)                    =>  Values in "A" Not Exist in "b, c" 
#       2- .difference_update(b)                =>  Update mySet to Values in "A" Not Exist in "b, c"
#       3- .intersection(b)                     =>  Only Matched Values
#       4- .intersection_update(b)              =>  Update mySet to Only Matched Values
#       5- .symmetric_difference(b)             =>  Values Do Not Match
#       6- .symmetric_difference_update()       =>  Update mySet to Non Matched Values
# --------------------------

## difference()             => Do Not Change Anything

a = {1, 2, 3, 4}
b = {1, 2, 3, "Ahmad", "Shark"}
print(a)

print(a.difference(b))      #  a - Matched values in "b"
print(a)

print('-'*50)
## difference_update()      => Change (Update) the Original Set

c = {1, 2, 3, 4}
d = {1, 2, "Ahmad", "Shark"}
print(c)

c.difference_update(d)    #  c - Matched Values in "d"
print(c)

print('-'*50)

## intersection()       => Matched Values

e = {1, 2, 3, 4, "X", "Shark"}
f = {"Shark", 2, 7, "A"}

print(e)
print(e.intersection(f))      # e & Match in "f"
print(e)

print('-'*50)

## intersection_update()        => Update mySet Matched Values 

g = {1, 2, 3, 4, "X", "Shark"}
h = {"Shark", 2, "X", 7, "A"}

print(g)
g.intersection_update(h)      # g & Match in "h"
print(g)

print('-'*50)

## symmetric_difference()           => Print All Values didn't Match

i = {1, 2, 3, 4, 5, "X"}
j = {"Ahmad", "Shark", 1, 3, 4, "X"}

print(i)
print(i.symmetric_difference(j))        #  j ^ i
print(i)

print('-'*50)

## symmetric_difference_update()        => Update All Values didn't Match

k = {1, 2, 3, 4, 5, "X"}
l = {"Ahmad", "Shark", 1, 3, 4, "X"}

print(k)
k.symmetric_difference_update(l)        #  k ^ l
print(k)