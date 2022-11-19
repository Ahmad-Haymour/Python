# --------------------------
# -- Lists Methods Part 2 --

#       1- .clear()                  =>  (Error) Same as .push() in JavaScript
#       2- .copy()                   =>  (Error) Make a Copy of a List
#       3- .count(Value)             =>  Count the Repetition, How many Same Element in my List
#       4- .index(index)             =>  Sort my List witch has Only One Type Elements (NOT All Types)
#       5- .insert (index, value)    =>  Insert a Value before the given Index
#       6- .pop(Number)              =>  Delete (Cut) a Number from List and save the Value to show
# --------------------------

## clear()      # Error => not supported!

a = [1, 2, 3, 4]
# a.clear()
a = []

print(a)

## copy()       # Error !!!

b = [1, 2, 3, 4]
# c = b.copy()
print(b)
# print(c)

## count()      
print("--------Count-------")
d = [1, 2, 10, 2, 50, 100, 2, 2, 10, 10]
dd = ["A", "B", "A", "A"]

print(d.count(2))
print(d.count(10))

print(dd.count("A"))
print(dd.count("B"))

## index()
print('----------Index---------')

e = ["Sam", "Ahmad", "Ram", "Amin"]

print(e.index("Amin"))
print(e.index("Ahmad"))

## insert( Index, Value)

f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0, "insert")
f.insert(-1, "Test")

print(f)

## pop()        => For Numbers

g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(1))
print(g.pop(2))

print(g)