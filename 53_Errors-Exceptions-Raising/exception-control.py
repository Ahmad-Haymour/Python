# ------------------------------------------------ #
#           -- Exceptions Handling --  
#      -- Try | Except | Else | Finally -- 
# ------------------------------------------------ #
#   Try     =>  Test the Code For Errors
#   Except  =>  Handle the Errors
# ------------------------------------------------ #
#   Else    =>  If No Errors found
#   Finally =>  Run The Code
# ------------------------------------------------ #

# number = int(input('Write your age: '))

# print(number)
# print(type(number))

# try :           # Try the Code and Test Errors
#     number = int(input('Write your age: '))

#     print('Good this is Integer from => Try')

# except :        # Handle the Errors if its Found
#     print('This is not Integer')

# else :          # If there is No Errors

#     print('Good this is Integer from => Else')

# finally :       # Run this Code anyway

#     print('Print from finally whatever happens')

print('><'*40)

## Specific Errors
# print(10/0)

try : 

    # print(10/0)
    # print(x)
    print(int('abcd'))

except ZeroDivisionError:

    print('Can\'t Divide')

except NameError :

    print('Identifier Not Found!')

except ValueError :
    print('Value Error happens')

except :

    print('Show if there is more Errors did not match the previous Exceptions')