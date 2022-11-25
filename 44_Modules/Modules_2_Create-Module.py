#---------------------------------------#
#  -- Modules => Create your Modules -- #
#---------------------------------------#

## Search in All Files for All Modules in System and your Path

##  Ctrl + b  => Search settings.json then =>
#   "python.auto-complete.extraPaths": ["home/user/Desktop/Python"]     => Thats Your Path Location, It work Without this Step too.


# import sys
# # Add new Path to System
# sys.path.append("/home/user/Desktop/Python/44_Modules/Games")
# print( sys.path)

# import elzero

# elzero.say_hello('Ahmad')
# elzero.sayHowAreYou('Ahmad')

## Alias  =>  Nickname

import elzero as zero

print(dir(zero))

zero.say_hello('Ahmad')
zero.sayHowAreYou('Ahmad')


from elzero import say_hello as sh

sh('Sally')
hru('Suzan')