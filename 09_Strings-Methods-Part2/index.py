# -----------------------
# -- Strings Methods 2 --
#       1- split()            => Make a List (Array) Every Space is a new Value in the List
#          split("x", max_split) => Second Value is Number declare how many splits u allow in this String or How many Values in a List
#       2- rsplit('x', 2)     => Starts the Split from the Right Side 
#       3- center(9, 'X')     => Center my String in 9 indexes, IF Second Value not defined Center in Spaces 
#       4- count('x')         => Count how many Char Match the Value
#          count('x', Start, End)  => Char Search From Index a ,(to Index) b.
#       5- swapcase()         => Swap UpperCase To LowerCase & !#
#       6- startswith('x')    => Is the String Starting with x ? Returns Boolean
#          startswith('x', Start, End)  => Boolean
#       7- endswith('x')         => Is the String Ending with x ? Returns Boolean
#          endswith('x', Start, End)    => Boolean
# -----------------------


# split()  rsplit()

a = "I Love Python and PHP and MySQL"
print(a.split())

b = "I-Love-Python-and-PHP-and-MySQL"
print(b.split("-"))

c = "I-Love-Python-and-PHP-and-MySQL"
print(c.split('-', 3))

d = "I-Love-Python-and-PHP-and-MySQL"
print(d.rsplit('-', 4))

# center()

e = "Ahmad"
print(e.center(9))
print(e.center(11, '-'))

# count("Char", Start, End)

f = "I Love Python and PHP because PHP is Easy"
print(f.count("PHP"))
print(f.count("PHP", 0, 25))

# swapcase()

g = "I Love Python"
h = "i lOVE pYTHON"
print(g.swapcase())
print(h.swapcase())

# startswith('x')

i = "I Love Python"
print(i.startswith("I"))