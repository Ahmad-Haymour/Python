# -----------------------
# -- Strings Methods 1 --
#       1- len()            => Length
#       2- strip()          => Delete all Spaces (Right & Left) Only || You Can Add a value Inside To Delete specific Character 
#       3- rstrip()         => Delete Right Space
#       4- lstrip()         => Delete Left Space
#       5- title()          => Capitalize every single word in a String
#       6- capitalize()     => Capitalize the First letter Only and LowerCase the Rest words
#       7- zfill(x)         => Fill your String with Zeroes (x) Width is how many 
#       8- upper()          => To Upper Case
#       9- lower()          => To Lower Case
# -----------------------

a = "#@#@ I Love #@ Python # #@"

print(len(a))
print(len(a))      

print(a.strip('#@'))
print(a.rstrip())
print(a.lstrip())

# title()
b = "I Love 2d graphics and 3g technology and Python"

print(b.title())

# capitalize()
b = "I Love 2d Graphics and 3g technology and Python"

print(b.capitalize())

# zfill(x)

c, d, e, f = "1", "22", "ab", "4321"

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))


# upper()
g = "ahmad"

print(g.upper())

# lower()
g = "AHMAD"

print(g.lower())