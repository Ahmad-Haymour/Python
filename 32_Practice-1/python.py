# ------------------------------
#       -- Slice Email --
# ------------------------------

email = "Mr.Haymour@outlook.com"

print(email[ : email.index('@')])


## Practice

# theName = input('What\'s your Name? ').strip().capitalize()
# theEmail = input('What\'s your Email? ').strip()

# username = theEmail[  : theEmail.index('@')]
# website = theEmail[ theEmail.index('@') + 1 :  ]

# print(username)
# print(website)

# print("Hello {:s}, your Email is {:s}".format(theName, theEmail))
# print('Your UserName is: {:s}\nYour WebSite is {:s}'.format(username, website))

## Age Details

#  age = input('What\'s your Age? ').strip()        => Type String
# age = int(input('What\'s your Age? '))      # Type Number Integer

# print(age)
# print(type(age))

# months = age * 12
# weeks = months * 4

# print("Your Age is: {:,d} Weeks".format(weeks))

##  Calculate Age Advanced
print('#'*50)
print('-Please type a Time Unit-'.center( 50,'#'))
print('#'*50)
# Collect Age Data
age = int(input("What is Your Age? "))

# Collect Time Unit Data
unit = input("Please Choose a unit: ( Months, Weeks, Days)").strip().lower()

months = age * 12
weeks = 4 * months
days = age * 365

if unit == 'months' :
    print('You chose unit {}'.format(unit))
    print('Your age is: {}'.format(months))
elif unit == 'weeks' :
    print('You chose unit {}'.format(unit))
    print('Your age is: {:,d} {}'.format(weeks, unit))
elif unit == 'days' :
    print('You chose unit {}'.format(unit))
    print('Your age is: {}'.format(months))
else :
    print('You didn\'t chose any unit, {}'.format(unit))
    print('Your age is: {}'.format(age))