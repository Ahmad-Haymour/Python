#-----------------------------------
#       -- Loop  =>  For--
#-----------------------------------
#  for items in iterable_object :
#       Do Something With ITEM
#-----------------------------------
#   item is a variable you create and call whenever you want
#   itm refer to the current position and will run and visit all items to the end
#   iterable_object  => Sequence [ list, tuple, set, dict, string of characters, etc ...]

myName = 'Ahmad'

for item in myName:
    print("[ {} ]".format(item.upper()))

print('loop is  done')

##

myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in myNumbers :
    # print(num * 2)
    if num % 2 != 0 :       # => (ODD)        => else num % 2 == 0 : (EVEN)
        print('The Number {} is Odd'.format(num))
    else : print('The Number {} is Even'.format(num))

else : print("The Loop is Finished")

## => else will print anyway CUZ ( for loop ) has no Condition
## => while loop has Condition