#-----------------------------------#
#  -- Built In Functions Part 6 --  #
#-----------------------------------#
#   - enumerate(  )
#-----------------------------------#

## enumerate()

mySkills = ["HTML", "CSS", "JS", "Python"]

skillsWithCounter = enumerate( mySkills, 20 )

print(type(skillsWithCounter))

for counter, skill in skillsWithCounter :

    print("- {} => {}".format(counter, skill))

print('><'*40)

## help()

# print(help(print))

print('><'*40)

## reverse()        #  Will Reflect Iterable Variables
#   - Reach Reversed Element only with (Loop)
myString = "Elzero"

print(reversed(myString))

for letter in reversed(myString) :
    print(letter)