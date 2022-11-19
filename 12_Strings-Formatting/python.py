# ------------------------
# -- Strings Formatting --

#       - Exactly the same like [" C "] Technology => Placeholders

#           1- %s           =>  Value Type String       (String)
#           2- %d           =>  Value Type Number       (Digit)
#           2- %f           =>  Value Type Number       (Float)

#       - New Way for Placeholders  .format()

#           0- "{}".format(Value)  => Any Value
#           1- {:s}   {index:s}        =>  Value Type String       (String)
#           2- {:d}   {index:d}        =>  Value Type Number       (Digit)
#           3- {:f}   {index:.2f}      =>  Value Type Number       (Float)

#       - Format Version 3.6++
#           # print(f"My Name is: {myValue}")

# ------------------------

name = "Ahmad"
age = 28
rank = 10

print("My Name is: " + name)
# print("My Name is: " + name + ", and Age is: " + age)  # Error => Can't concatenate 'string' and 'integer' Objects

print("My Name is: %s" % name)
print("My New Name is : {}" .format(name))

print("My Name is: %s" % name + ", and my age is: %d" % age )
print("My New Name is: {}" .format(name) + ", and my age is: {}".format(age) )

print("My Name is: %s, and my age is: %d, My Rank is: %f" % (name, age, rank) )
print("My New Name is: {:s}, and my age is: {:d}, My Rank is: {:f}" .format(name, age, rank) )

# Practice

n = "Ahmad"
l = "Python"
y = 10

print("My Name is %s, i'am %s Developer with %d Years Experience" % (n, l, y))
print("My New Name is {:s}, i'am {:s} Developer with {:d} Years Experience" .format(n, l, y))

# Control Floating Point Number

myNumber = 22
print("My Number is: %d" % myNumber)
print("My Number is: {:d}".format(myNumber))
print("My Number is: {:f}".format(myNumber))
print("My Number is: %.2f" % myNumber)
print("My Number is: {:.3f}".format(myNumber))

# Truncate

myLongString = "Hello People, We are learning Python Technology"
print("Message is : %s" % myLongString )
print("Message is : %.5s" % myLongString )            #  => Show First 5 Letters from myString
print("Message is : {:.20s}" .format(myLongString) )           #  => Show First 20 Letters from myString

# Format Money

myMoney = 50097225010

print("My Money in Bank is: {:d}".format(myMoney))
print("My Money in Bank is: {:,d}".format(myMoney))


# ReArrange Items

a, b, c = "One", "Two", "Three" 

print("Hello {} {} {}".format(a, b, c))
print("Hello {2} {1} {0}".format(a, b, c))
print("Hello {2} {1} {0}".format(a, b, c))

x, y, z = 10, 20, 30

print("Hello {} {} {}".format(x, y, z))
print("Hello {2:f} {1:.2f} {0:d}".format(x, y, z))
print("Hello {2:.1f} {1:.2f} {0:.5f}".format(x, y, z))

# Format in Version 3.6++      (f)

myName = "Mark"
myAge = 28
  
print("My Name is: {myName}, my age is: {myAge}")
# print(f"My Name is: {myName}")            ## ##    Wrong Code ! didn't Work