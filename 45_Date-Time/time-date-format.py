#---------------------------------------------#
#     -- Date and Time => Format Date -- 
#---------------------------------------------#

#   DATE PACKAGE HELP
#   https://strftime.org/

import datetime

myBirthDay = datetime.datetime(1994, 2, 11)

print(myBirthDay)
print(myBirthDay.strftime('%a'))
print(myBirthDay.strftime('%A'))
print(myBirthDay.strftime('%b'))
print(myBirthDay.strftime('%B'))

print('><'*40)

print(myBirthDay.strftime("%d %B %Y"))
print(myBirthDay.strftime("%d, %B, %Y"))
print(myBirthDay.strftime("%d%B%Y"))
print(myBirthDay.strftime("%d - %B - %Y"))
print(myBirthDay.strftime("%B - %Y"))