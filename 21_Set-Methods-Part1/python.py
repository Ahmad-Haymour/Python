# --------------------------
#  -- Set Methods Part 1 --

#       1- .union(a, b, c)              => Merge Sets Variables
#       2- .update(a)                   => Merge Sets Variables
#       3- .add(Value)                  => Add Only One Element
#       4- .copy()                      => Shallow Copy
#       5- .remove()                    => Add Only One Element
#       6- .discard()                   => Shallow Copy
#       6- .pop()                       => Give us a Random Element From my Set
# --------------------------

a = {1, 2, 3}
a.clear()

print(a)

## union()          => To Merge Sets

b = {"One", "Two", "Three", "1", "2"}
c = {"1", "2", "3"}
x = {"Zero", "Cool", "4", "One"}

print(b | c)
print(b.union(c, x))

## add()    It Take only One Argument

d = {1, 2, 3, 4}
d.add(5)
d.add(6)

print(d)

## copy()

e = {1, 2, 3, 4}
f = e.copy()

print(e)
print(f)

e.add(7)
print(e)
print(f)

## remove()         => IF Value NOT Found (Error)

g = {1, 2, 3, 4, 5}
g.remove(1)
# g.remove(9)        => Error Value Not Found

print(g)

## discard()         => Like remove() BUT, IF Value NOT Found (NO Errors)

h = {1, 2, 3, 4, 5}
h.discard(4)
h.discard(7)

print(h)

## pop()             => Give us a Random Element From my Set

i = {"A", True, 1, 2, 3, 4, 5}
print(i.pop())

## update()             =>  To Merge Sets

j = {1, 2, 3}
k = {1, "A", "B", 2}

j.update(["HTML", "CSS"])
print(j)
j.update({"HTML", "CSS"})
print(j)
j.update(("HTML", "CSS"))

j.update(k)

print(j)