# ------------------------------------------------ #
#       -- Errors and Exceptions Raising --   
# ------------------------------------------------ #
# [1] Exceptions is a Runtime Error Reporting Mechanism
# [2] Exceptions Gives you the Message to understand the Problem
# [3] Traceback Gives you the Line to look for the Code in this Line
# [4] Exceptions have Types (SyntaxError, IndexError, KeyError, etc...)
# [5] Exceptions List https://docs.python.org/3/library/exceptions.html
# [6] Raise Keyword Used to Raise your own Exceptions
# ----------------------------------------------------

x = 10

if x < 0 :

    # print('The Number {} is less than Zero'.format(x))

    raise Exception('The Number {} is less than Zero'.format(x))  # => Make New Error If Condition Match

    print('This will not Print Because of Error')

else:
    print("{} is Good Number".format(x))

print('><'*40)

y = 'Ahmad'

if type(y) != int :

    raise ValueError('Only Numbers Allowed')

print('Print Message after If Condition')