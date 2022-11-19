# --------------------------
#      -- Dictionary--

#       1- Dict Items Are Enclosed in Curly Braces {}
#       2- Dict Items Are Contains { Key : Value } 
#       3- Dict Key Must Be Immutable => (Number, String, Tuple) List:[] Not Allowed
#       4- Dict Values Can Have Any Data Type.
#       5- Dict Keys Need To Be Unique.
#       6- Dict Is Not Ordered You Access Its Elements with ["Key"] 
# --------------------------

## Dictionary

user = {
    "name": "Ahmad",
    "age": 28,
    "country": "Syria",
    "skills": ['Html', 'Css', "Js"],
    "rating": 10.5,
    10: "Number Ten"
}

print(user)
print(type(user))
print(user["country"])
print(user.get("country"))
print(user["skills"])

print(user.keys())
print(user.values())

print('-'*80)
## Two-Dimensional Dictionary

languages = {
    "One": {
        "name": "Html",
        "progress": "80%"
    },
    "Two": {
        "name": "Css",
        "progress": "90%"
    },
    "Three": {
        "name": "Js",
        "progress": "90%"
    }
}

print(languages)
print(languages["One"])
print(languages['Three']["name"])

## Dictionary Length

print(len(languages))
print(len(languages["Two"]))

## Create Dictionary from Variables

frameworkOne = {
    "name": "VueJs",
    "progress": "80%"
}
frameworkTwo = {
    "name": "ReactJs",
    "progress": "90%"
}

frameworkThree = {
    "name": "Angular",
    "progress": "60%"
}

allFramework = {
    "one": frameworkOne,
    "two": frameworkTwo,
    "three": frameworkThree,
    "four": {
        "name": 'Python',
        "progress": '100%'
    }
}

print(allFramework)

