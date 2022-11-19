# ------------------------
# -- Strings Methods 3 --
#       1- index('x')            => Find Index of Character in a String => Return Number
#       2- find('x')             => Find Index of Character in a String => Return Number
#          find(SubString, Start, End)
#       3- rjust(10)             => Justify my text Right in 10 Characters, IF Second Value not Exist do Spaces instead
#       4- ljust(10)             => Justify my text Left
#          ljust(20, '#')        => # instead of Spaces
#       5- center(11, '-')       => Justify my Text Center
#       6- splitlines()          => Split Lines in a String To List (Array)
#       7- expandtabs(num)       => Control the Number of Spaces in Each Tab

#  -- Matching -- => Returns Boolean
#       1- istitle()             => Is All First Characters UpperCase ?
#       2- isspace()             => Is it a Space ?
#       3- isidentifier()        => Error not Exist anymore!
#       4- islower()             => Is the String LowerCase ?
#       5- isupper()             => Is the String UpperCase ?
#       5- isalpha()             => Is it from 'A-Z, a-z' ?
#       7- isalnum()             => Is it from 'A-Z, a-z' or with Numbers ?
# ------------------------

# index(SubString, Start, End)

a = "I Love Python"
print(a.index("P"))              # Index Number 7
print(a.index("P", 7, 10))       # Index Number 7
# print(a.index("P", 0, 5))      # Error

# find(SubString, Start, End)

b = "I Love Python"
print(b.find("P"))              # Index Number 7
print(b.find("P", 7, 10))       # Index Number 7
print(b.find("P", 0, 5))        # -1 Not Found

# rjust()  ljust()

c = "Alex"
print(c.rjust(10))
print(c.rjust(10, "/"))

d = "Alex"
print(d.ljust(10))
print(d.ljust(10, "#"))

# splitlines()

e = """First Line
Second Line
Third Line"""
print(e.splitlines())

f = "First Line\nSecond Line\nThird Line"
print(f.splitlines())

# expandtabs(num)

g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(5))

print('#---------------------One Two-----------------------------#')

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())
print(two.istitle())
print('#----------------------Three Four----------------------------#')

three = " "
four = ""
print(three.isspace())
print(four.isspace())
print('#----------------------Five Six----------------------------#')

five = "i love python"
six = "I LOVE ME"
print(five.islower())
print(six.isupper())

print('#-------------------------Seven Eight Nine-------------------------#')
# isidentifier()      => Error Not Exist Anymore!
# seven = "john_food"
# eight = "JohnFood"
# nine = "John--Food"

# print(seven.isidentifier())
# print(eight.isidentifier())
# print(nine.isidentifier())
print('#--------------------------------------------------#')

x = "AbCdEfg"
y = "Abcdef1234"
print(x.isalpha())
print(y.isalpha())

print('#--------------------------------------------------#')

u = "AbCdEfg"
z = "Abcdef1234"
print(u.isalnum())
print(z.isalnum())