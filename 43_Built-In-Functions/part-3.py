#-----------------------------------#
#  -- Built In Functions Part 3 --  #
#-----------------------------------#
#   [1]- abs()                  =>     The Distance between [ 0 => Number ] 
#   [2]- pow()                  =>     Number**
#   [3]- min()                  =>     The Minimum Value
#   [4]- max()                  =>     The Maximum Value
#   [5]- slice()
#------------------------------

## abs()        =>  Absolute Value

print(abs(100))
print(abs(-100))
print(abs(10.22))
print(abs(-10.22))

## pow( base, exponent , module )       =>  Power

print(pow(2, 3))        # => ( 2 * 2 * 2 ) = 8
print(pow(2, 5, 10))        # => ( 2 * 2 * 2 * 2 * 2 ) = 32 % ( 10 ) => 2

print('><'*40)

## min()        =>  Minimum Value

myNumbers = (1, 20, -50, -100, 100)
print(min(1, 10, 20, -50, 15 ))
print(min("X-blabla", "Z-blabla", "Ahmad" ))
print(min(myNumbers))

print('><'*40)

## max()        =>  Maximum Value

myNumbers = (1, 20, -50, -100, 100)
print(max(1, 10, 20, -50, 15 ))
print(max("X-blabla", "Z-blabla", "Ahmad" ))
print(max(myNumbers))

print('><'*40)

## slice( Start, End, Step )        => Not Include End

a = ["A", "B", "C", "D", "E", "F"]

print(a[:3])
print(a[slice(3)])
print(a[slice(2, 5)])
print(a[slice(0, 6, 2)])



