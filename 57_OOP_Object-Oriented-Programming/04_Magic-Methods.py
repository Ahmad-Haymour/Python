# -----------------------------------------------------
# -- Object Oriented Programming => Magic Methods --
# -----------------------------------------------------
#   Every thing in Python is an Object
#   __init__ called automatically when instantiating Class
#   self.__clas__ to which class instance belong
#   __str__ Give you Human-Readable Output
#   __len__ Returns the Length of the Container
#           Called when we use the Built-in len() Function on the Object
# -----------------------------------------------------------------------

#   => Self is the Instance
class Skill:

    def __init__(self):

        self.skills = ['Html', 'Css', 'Js']

    def __str__(self):

        return f'This is my Skills => {self.skills}, Length => {len(self.skills)}'

    # Use __len__ Method to have access to USE len( instance ) => on your Instance
    def __len__(self):

        return len(self.skills)


profile = Skill()

print(profile)
print(profile.__class__)
print(profile.skills)


my_string = "Ahmad"
print(type(my_string))
print(my_string.__class__)
print(dir(my_string))
print(dir(str))
print(dir(type))
print(dir(int))
print(dir(float))

#   We can do like the Previous Part in Class Instance on a String cuz its a Class too and have Methods
# print(member_one.full_name())
# print(Member.full_name(member_one))

print(str.upper(my_string))

print('><'*50)

print(profile)
print(len(profile))

profile.skills.append('PHP')
profile.skills.append('Python')

print(len(profile))
