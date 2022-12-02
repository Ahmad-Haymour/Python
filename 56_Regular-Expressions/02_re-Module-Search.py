# -----------------------------------------------------------------
# -- Regular Expressions => Re Module Search and FindAll Part 6 --
# -----------------------------------------------------------------
#    search()      =>  Search a String for Match and Return the First Match Only
#    findall()     =>  Returns a List of All Matches and Empty List if no Match
# -----------------------------------------------------------------
#    () Group Brackets Search a String for Match and Return the First Match Only

import re

my_search = re.search( r"[A-Z]{2}\d\s\w{3}-?", 'abcd(AH2 abc-)<Blabla123' )
#   re.search(r" r => (Row) Help to read Code without Errors")

print(my_search)
print(my_search.span())
print(my_search.string)
print(my_search.group())

print('><'*40)

is_email = re.search(r"^[A-z0-9]+@[0-9A-z]+\.(com|net|de)$", "ahMad@abcd123.com")

if is_email:

    print('The email is valid')
    print(is_email)
    print(is_email.span())
    print(is_email.string)
    print(is_email.group())

else:
    
        print('The email is not valid')


print('><'*40)


email_input = input('Write your Email   ')

search = re.findall('^[A-z0-9]+@[A-z0-9]+\.com|net', email_input)
## With group brackets() it will Return the last Group Only

empty_container_list = []

if search != []:

    empty_container_list.append(search)
    print('Email Added')

else:

    print('Invalid Email')


for email in empty_container_list:

    print(email)