#---------------------------------------------#
#  -- Modules => Install External Packages -- #
#---------------------------------------------#

import datetime

print(dir(datetime))

print(dir(datetime.datetime))

##  print the Current Date and Time

print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)

print('><'*40)

## Print Start and End of Date

print(datetime.datetime.min)        # Start 0001  =>  End 9999
print(datetime.datetime.max)

print('><'*40)

## Print the Current Time

print(datetime.datetime.now().time())
print(datetime.datetime.now().time().hour)      #=> Hour
print(datetime.datetime.now().time().minute)    #=> Minute
print(datetime.datetime.now().time().second)    #=> Second

print('><'*40)

## Print Start and End of Time

print(datetime.time.min)
print(datetime.time().max)

print('><'*40)

## Print Specific Date

print(datetime.datetime(1994, 5, 11))       #  =>  Year, Month, Day => Required
print(datetime.datetime(1994, 5, 11, 22, 22, 00))

print('><'*40)
print('><'*40)

## Example      =>  We Receive the Number of Days

myBirthDay = datetime.datetime(1994, 5, 11)
dateNow = datetime.datetime.now()

print("My Birthday is {} And ".format(myBirthDay))
print("Date Now is {}".format(dateNow))

print("I lived for => {}".format(dateNow - myBirthDay))             #  =>  It will add "days ,hours, minutes etc to your String"
print("I lived for => {} Days".format((dateNow - myBirthDay).days))      #  =>  Will Print only Days(integer)


# myAge = date - myBirthDay
# print("My Age is => {}".format(myAge))
# print("My Age is => {} Days.".format(myAge.days))