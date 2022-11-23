#-----------------------------------#
#  -- Built In Functions Part 6 --  #
#               Reduce
#-----------------------------------#
#   [1] Reduce take a Function & Iterator
#   [2] Filter run a Function on First and Second Element and Give Result
#   [3] Then Run Function on Result and Third Element
#   [4] Then Run Function on Result and Fourth Element and so on
#   [5] Till one Element is left and this is the Result of the Reduce
#   [6] The Function can be Pre-Defined Function or Lambda Function
#-------------------------------------------------------------------------



##  You Have to Import Reduce from functools

from functools import reduce


def sumAll(num1, num2) :

    return num1 + num2


numbers = [1, 8, 2, 9, 100]

# result = reduce(sumAll, numbers)
result = reduce( lambda num1, num2 : num1 + num2, numbers)

print(result)

##  =>  ((((1 + 8) + 2) + 9) + 100)