#------------------------------------------------------#
# -- Function Packing, Unpacking Arguments Training -- #
#------------------------------------------------------#
#   *Tuple
#   **Dictionary
#------------------------------------------------------#

myTuple = ("HTML", "CSS", "JS")
mySkills = {
    "Python": "50%",
    "JAVA": "10%",
    "mySQL": "80%"
}

def show_skills(user, *skills, **skillsAndProgress) :
    print("Hello {}\nSkills without Progress is =>".format(user))

    for skill in skills :
        print('*- {}'.format(skill))

    print("Skills with Progress is =>")

    for skill_key, skill_value in skillsAndProgress.items() :
        print('*- {} => {}'.format(skill_key, skill_value))


show_skills('Ahmad', "HTML", "CSS", "JS", Python='60%', JAVA = "20%")


show_skills("Lara", *myTuple, **mySkills)