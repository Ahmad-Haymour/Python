#-----------------------------------#
#  -- Built In Functions Part 2 --  #
#-----------------------------------#
#   [1]- sum(List)                  =>     Sum a List of Numbers
#   [2]- round(Number)              =>     Round to the Maximum Number IF if Number is half or more. Else to the Minimum
#   [3]- range(start, end, step)    =>     Start Default = 0, End must be Given, Steps starts with 2 
#   [4]- print()                    =>       
#------------------------------

## sum( iterable, start )

a = [1, 10, 19, 40]

print(sum(a))
print(sum(a, 50))

## round( Number, Number of Digits )

print(round(7.500))     # 8     up to maximum
print(round(7.499))     # 7     low to minimum

print(round(2.499))
print(round(2.499, 3))

print(round(2.500))
print(round(2.501, 3))
print('><'*40)

## range( Start, End, Steps )

print(range(10))
print(list(range(10)))

print(range(1, 11, 2))

print('><'*40)

##  print()     => 
# Separator => sep=" " (Default Value Space)
# End of print => end="\n" (Default New Line)

print("Hello there, How are you?")
print("Hello", "Ahmad,", "how", "you", "doing")
# print("Hello", "Ahmad,", "how", "you", "doing", sep=" | ")    # Error didn't work

print("First Line", end=" => ")
print("Second Line")