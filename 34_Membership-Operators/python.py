# ------------------------------
#   -- Membership Operators --

#   => in
#   => not in
# ------------------------------

## String
name = "Ahmad"
print("A" in name)
print("s" in name)
print("m" in name)

print('='*50)

## List
friends = ['Salam', 'Sally', 'Suzan']
print("Ahmad" in friends)
print("Sally" in friends)
print("Suzan" not in friends)

print('='*50)

##  Using ( in - not in ) With Condition

# myVariable in myList
countriesOne =['Syria', "Egypt", "Qatar", 'Lebanon']
countriesOneDiscount = 80

countriesTwo = ['Germany', "Italy"]
countriesTwoDiscount = 50

myCountry = "Holland"

if myCountry in countriesOne :
    print("Hello you have a discount equal of {:d}".format(countriesOneDiscount))

elif myCountry in countriesTwo :
    print("Hello you have a discount equal of {:d}".format(countriesTwoDiscount))

else : print("You have no Discount")