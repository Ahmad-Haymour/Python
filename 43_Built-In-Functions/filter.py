#-----------------------------------#
#  -- Built In Functions Part 5 --  #
#               Filter
#-----------------------------------#
#   [1] Filter take a Function & Iterator
#   [2] Filter run a Function every Element
#   [3] The Function need to Return (Boolean) Value
#   [4] The Function can be Pre-Defined Function or Lambda Function
#   [5] Filter out all Elements for which the Function Return True
#------------------------------------------------------------------

## Example      => You have to Return True to see the Value from Filter,  Filter Don't read the False Values

def check_number(num):

    if num > 10 :
        return True

my_numbers = [0, 0, 1, 20, 22, 67, 56, 0]

for number in filter(check_number, my_numbers) :

    print("*-  => {}".format(number))

print('><'*40)

# Example 2

def check_name(name):

    return name.startswith("A")

my_texts = ['Ahmad', 'Sam', "Sally", "Ali"]

data_result = filter(check_name, my_texts)

for person in data_result :

    print(person)


print('><'*40)


# Example 3         =>  Lambda Function & Filter


my_texts = ['Ahmad', 'Sam', "Sally", "Ali", "Omar", "Suzan", "Axe"]

for name in filter( lambda theText : theText.startswith("S") , my_texts) :

    print(name)