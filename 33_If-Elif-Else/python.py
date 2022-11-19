# ------------------------------
#   -- IF - Else If - Else --
#        -- Nested If --

#   if 'A' == 'B' :
#       print()
#   elif 'A' != 'B' :
#       print()
#   elif 'A' == 'B' :
#       print()
#   else  :
#       print()
# ------------------------------

uName = "Ahmad"
uCountry = "Nowhere"
cName = "Python Course"
cPrice = 100
cDiscount = 30
cDiscount1 = 80

if uCountry == "Syria" :
    print("Hallo {} because you are from {}".format(uName, uCountry))
    print("Hello {0:} the Course \"{1}\" Price is ${2:}".format(uName, cName, (cPrice - 90)))

elif uCountry == "Egypt" :
    print("Hallo {} because you are from {}".format(uName, uCountry))
    print("Hello {0:} the Course \"{1}\" Price is ${2:}".format(uName, cName, (cPrice - 70)))

elif uCountry == "Kuwait" :
    print("Hallo {} because you are from {}".format(uName, uCountry))
    print("Hello {0:} the Course \"{1}\" Price is ${2:}".format(uName, cName, (cPrice - 50)))

else :
    print("Hallo {} because you are from {}".format(uName, uCountry))
    print("Hello {0:} the Course \"{1}\" Price is ${2:}".format(uName, cName, (cPrice - 10)))
  
print('='*50)

## Nested If

uName = "Ahmad"
uCountry = "Lebanon"
cName = "Python Course"
cPrice = 100
isStudent = True

if uCountry == "Syria" or uCountry == "Egypt" or uCountry == "Lebanon":
    if isStudent :
        print("Hallo {} because you are from {}".format(uName, uCountry))
        print("Hello {0:} the Course \"{1}\" Price is ${2:}".format(uName, cName, (cPrice - 99)))
    else :
        print("Hallo {} because you are from {}".format(uName, uCountry))
        print("Hello {0:} the Course \"{1}\" Price is ${2:}".format(uName, cName, (cPrice - 90)))

elif uCountry == "Kuwait" or uCountry == "Qatar":
    print("Hallo {} because you are from {}".format(uName, uCountry))
    print("Hello {0:} the Course \"{1}\" Price is ${2:}".format(uName, cName, (cPrice - 70)))

else :
    print("Hallo {} because you are from {}".format(uName, uCountry))
    print("Hello {0:} the Course \"{1}\" Price is ${2:}".format(uName, cName, (cPrice - 10)))

print('='*50)

## Ternary Conditional Operator

country = "Egypt"

if country == "Egypt" : print("The Weather in {} is 35".format(country))
elif country == "Syria" : print("The Weather in {} is 15".format(country))
else : print('Country is not in the list')

## Short IF

movieRate = 18
age = 20

print("Movie is not good for you" if age < movieRate else "Movie is good for u happy watching")

## Condition IF True | IF Condition | Else | Condition if False 