#------------------------------------#
#  -- Modules => Built In Modules -- #
#------------------------------------#
#   [1]  Module is a File Contain a Set of Functions
#   [2]  You can Import Module in your app to help you
#   [3]  You can Import Multiple Modules
#   [4]  You can Create your own Modules
#   [5]  Modules Saves your Time
#-----------------------------------

## Import Main Module
# import random
# Where is my Module ?
# print(random)

# print("Random a Float Number {}".format(random.random()))

## dir()     =>  Show all Functions Inside Module

# print(dir(random))

##  Import Function or more from Module
##  (Not the [Module], Only Multiple Functions)

from random import randint, random

print("Print Random Integer => {}".format(randint(100, 500)))
print("Print Random Float => {}".format(random()))

## Import All Functions from Module Random
from random import *