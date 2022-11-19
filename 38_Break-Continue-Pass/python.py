#-----------------------------------
#   -- Break - Continue - Pass--

#       - Break      =>  End the Loop
#       - Continue   =>  Ignore the Condition and Continue Looping
#       - Pass       =>  It will pass Errors or Undefined Variables ( Code will run anyway )
#-----------------------------------

myNumbers = range(1, 21)        # => List
# print(myNumbers)


## Continue 

for number in myNumbers :

    if number == 13 or number == 3 :
        continue

    print(number)

print('<Break>'*5)


## Break 

for number in myNumbers :

    if number == 13 :
        break

    print(number)

print('<Pass>'*5)

## Pass 

for number in myNumbers :

    if number == 2 :
        pass

    print(number)

print('<>'*50)


