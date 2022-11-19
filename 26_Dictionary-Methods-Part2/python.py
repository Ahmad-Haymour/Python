# ------------------------------
# -- Dictionary Methods Part 2--

#       1- .setdefault({a, b})            => Add a new Key + Value in myDictionary
#           .update({a : b})              => Same. Add Only One Key One Value
#       2- .popitem()                     => Return The Last Item Added To My Dictionary
#       3- .items()                       => Return Keys and Values Each in Separate Tuple
#       4- .fromkeys()                    => Iterable === (Loop)  #  
#        dict.fromkeys( A,  B )           => Make new Dictionary A is my Keys, B is my Values
# ------------------------------


## setdefault()     =>  

user = {
    "name": "Ahmad"
}

print(user)
# print(user.setdefault("name", "Ahmad"))    #    =>  It Won't Rename Cuz we already have a Value 
print(user.setdefault("age", 28))
# print(user.setdefault("age"))   => Value is "None" (Undefined)

print(user)

print('='*50)

## popitem()

member ={
    "name": "Osman",
    "skill": "PS5"
}

print(member)
member.update({"age": 36})
print(member.popitem())             # => Return The Last Item Added To My Dictionary

print('='*50)

## items()

view = {
    "name": "Espresso",
    "skill": "Cafe"
}

view['age'] = 50

print(view)

allItems = view.items()         # => Return Keys and Values Each in Separate Tuple
print(allItems)

print('='*50)

## fromkeys( Keys, Values )       => Iterable === (Loop)

a = ("MyKeyOne", "MyKeyTwo", "MyKeyThree")
b = "X"

print(dict.fromkeys(a, b))