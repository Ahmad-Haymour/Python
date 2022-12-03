# --------------------------------------------------------------------
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# Self: Point to Instance Created from Class
# Instance Attributes: Instance Attributes Defined Inside the Constructor
# --------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point to Instance Created from Class
# Instance Methods can have more than one Parameter Like any Function
# Instance Methods can freely access Attributes and Methods on the same Object
# Instance Methods can access the Class Itself
# --------------------------------------------------------------------

class Member:

    not_allowed_names = ['Hell', 'Shit', 'Baloot']

    users_count = 0

    def __init__(self, first_name, middle_name, last_name, gender):

        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender

        Member.users_count += 1

    def full_name(self):

        return f'{self.fname} {self.mname} {self.lname}'

    def name_with_title(self):

        if self.gender == 'Male':
            return f'Hello Mrs {self.fname}'

        elif self.gender == 'Female':
            return f'Hello Miss {self.fname}'

        else:
            return f'Hello {self.fname}'

    def get_all_info(self):

        if self.fname in Member.not_allowed_names:
            raise ValueError('Name not allowed')

        return f'{self.name_with_title()}, your Fullname is => {self.full_name()}'

    def delete_user(self):
        Member.users_count -= 1
        return f'User {self.fname} deleted'


print(Member.users_count)
member_one = Member('Ahmad', 'Mohammed', 'Rami', 'Male')
member_two = Member('Osama', 'Mohammed', 'Alsayed', 'Male')
member_three = Member('Lara', 'Philip', 'Möller', 'Female')
member_four = Member('Hell', 'Shit', 'Blabla', 'Male')

print(Member.users_count)
print(member_four.delete_user())
print(Member.users_count)

print(dir(member_one))

print(member_one.fname, member_one.mname, member_one.lname)
print(member_two.fname, member_two.lname )
print(member_three.fname)

print(member_one.full_name())
print(member_one.name_with_title())

print(member_one.get_all_info())
print(member_three.get_all_info())

# print(member_four.get_all_info())