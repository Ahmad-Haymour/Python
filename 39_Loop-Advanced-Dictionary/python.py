#-----------------------------------
#  -- Advanced Dictionary Loop --
#-----------------------------------

mySkills = {
    "HTML": "100%",
    "CSS": "90%",
    "JS": "80%",
    "Python": "50%",
}

print(mySkills)
print(mySkills.items())         #  =>  Keys & Values

for skill in mySkills :
    print("Skill is => {} -- Value is => {}".format(skill, mySkills[skill]))

print('<>'*50)

## For Loop with (Key & Value) => Dictionary

for skill_key, skill_value in mySkills.items() :
    print('my Skill => {}, Progress => [ {} ]'.format(skill_key, skill_value))

print('<>'*50)

myUltimateSkills = {
    "HTML": {
        "Main": "80%",
        "Pugjs": "80%"
    },
    "CSS": {
        "Main": "90%",
        "Sass": "70%"
    }
}

for key_primary, value_primary  in myUltimateSkills.items() :

   print("{} Progress is: ".format(key_primary, value_primary))

   for second_Key, second_Value in value_primary.items() :
   # for key_secondary, value_secondary in myUltimateSkills[key_primary].items() :      ## Same Case

        print('- {}  =>  {}'.format(second_Key, second_Value))
        # print('- {}  =>  {}'.format(key_secondary, value_secondary))                  ## Same Case