# --------------------------
#  -- Set Methods Part 3--

#       1- .issuperset(b)                 =>  True -IF All Elements in Second Set are in my Original Set
#       2- .issubset()                    =>  True -IF All Elements in Original Set are in my Second Set
#       3- .isdisjoint()                  =>  True -IF No Value Match in Both Sets
# --------------------------


## issuperset()         =>  All "b" Elements are Included in my Original Set "a"?

a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}

print(a.issuperset(b))      #  True
print(a.issuperset(c))      #  False  => 5 NOT Found in a Set

print('-'*50)

## issubset()               =>  All my Original Set "a" Elements are Included in my Second Set "b"?

d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {1, 2, 3, 4, 5}

print(d.issubset(e))      #  False      =>  4 is Not in Second Set "e"
print(d.issubset(f))      #  True

print('-'*50)

## isdisjoint()         => True => If The Values in Original Set Not Match another Values in Second Set

g = {1, 2, 3, 4}
h = {1, 2, 3, "A", 5}
i = {11, 22, 49}

print(g.isdisjoint(h))
print(g.isdisjoint(i))