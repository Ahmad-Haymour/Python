# ----------------------------------------------#
#           -- Debugging Code --
# ----------------------------------------------#

my_list = [1, 2, 3, 4, 5]

my_dictionary = {"Name": 'Ahmad', 'Age': 28, 'Country': "Syria"}

for num in my_list:
    print(num)

for key, value in my_dictionary.items():
    print('{} => {}'.format(key, value))
    print("In Box => {}".format(my_dictionary[key]))


def function_one():
    print('From Function One')


function_one()