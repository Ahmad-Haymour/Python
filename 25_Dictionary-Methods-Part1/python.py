# ------------------------------
# -- Dictionary Methods Part 1--

#       1- .clear() 
#       2- .update()  
#       3- .copy()  
#       4- .keys()
#       5- .values()  
# ------------------------------

## clear()

user = {
    "name": "Ahmad"
}

print(user)
user.clear()
print(user)

print("-"*50)

## update()

member = {
    "name": "Ahmad"
}
print(member)

member['age'] = 28
print(member)

member.update({"country": 'Syria'})
print(member)

print("-"*50)

## copy()

main = {
    "name": "Shark"
}

b = main.copy()

main.update( { "skills": 'Biting' } )

print(main)
print(b)
print("-"*50)

## keys() + values()

print(b.keys())
print(main.values())