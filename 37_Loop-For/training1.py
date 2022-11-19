#-----------------------------------
#       -- Loop  =>  For--
#        -- Trainings  --
#-----------------------------------

## Range

# myRange = range(1, 101)

# for r in myRange :
#     print(r)

##              =>      --  Dictionary  --

mySkills = {
    "HTML": "100%",
    "CSS": "80%",
    "JS": "90%",
    "Python": "45%",
    "PHP": "10%",
    "MySQL": "0%"
}

print(mySkills["JS"])
print(mySkills.get("Python"))

for skill in mySkills :
    print('My process in {} is {} '.format(skill, mySkills[skill]))

print('='*50)

##   Nested Loop         =>      --  List  --

# people = ['Ahmad', "Lara", 'Bart', "Homer"]
# skills = ["HTML", "CSS", "JS"]

# for person in people :
#     print('# '*3+person)

#     for skill in skills :
#         print('- '+skill)


##   Nested Loop         =>      --  Dictionary  --

peoples = {
    'Ahmad': {
        "Python": "50%",
        "SASS": "70%",
        "React": "80%",
    },
     'Lara': {
        "HTML": "50%",
        "CSS": "70%",
        "JS": "80%",
    },
     'Sam': {
        "PHP": "50%",
        "JQuery": "70%",
        "Java": "80%",
    },
}

# print(peoples['Ahmad'])
# print(peoples['Lara']['CSS'])


for person in peoples :
    # print('Skills and Progress for {} is => {}'.format( person, peoples[person]))
    print('Skills and Progress for {} is => \n'.format(person))

    for skill in peoples[person] :
        print("Skill {}, Progress => {}".format(skill.upper(), peoples[person][skill]))

    print('<>'*50)