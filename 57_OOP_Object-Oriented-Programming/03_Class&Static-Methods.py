# --------------------------------------------------------------------
# -- Object Oriented Programming => Class Methods & Static Methods --
# --------------------------------------------------------------------
# Class Methods:
#   - Marked with @classmethod Decorator to Flag it as Class Method
#   - It take cls Parameter nor self to point to the Class not to the Instance
#   - It doesn't require creation of a class instance
#   - Used when you want to use
# Instance Attributes: Instance Attributes Defined Inside the Constructor
# --------------------------------------------------------------------


class Member:

    not_allowed_names = ['Hell', 'Shit', 'Baloot']

    users_count = 0

    @classmethod
    def show_users_count(cls):
        print(f'We have {cls.users_count} users in our system.')

    @staticmethod
    def say_hello():
        print('Hello from static Method')

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
member_four = Member('Shit', 'Hell', 'Blabla', 'Male')

print(Member.users_count)
print(member_four.delete_user())
print(Member.users_count)

print('><'*40)

Member.show_users_count()

print('><'*40)

print(member_one.full_name())
# Background in Python will be =>
print(Member.full_name(member_one))

print('><'*40)

Member.say_hello()
