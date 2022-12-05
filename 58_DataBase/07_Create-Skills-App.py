# -----------------------------------------------
# -- Databases => SQLite => Create Skills App --
# -----------------------------------------------
# Input Big Message
input_message = """
What do you want to do ?
"s" => Show All Skills
"a" => Add NEw Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option:
"""

user_input = input(input_message).strip().lower()

print(user_input)

# Command List
command_list = ["s", "a", "d", "u", "q"]

def show_skill():
    print('Show Skill')
def add_new_skill():
    print(f'Add New Skill')


def delete_skill():
    print(f'Delete Skill')


def update_skill():
    print(f'Update Skill')


def quit_app():
    print(f'Quit The App')


if user_input in command_list:

    print(f'Command Found {user_input}')

    if user_input == "s":

        show_skill()

    elif user_input == "a":

        add_new_skill()

    elif user_input == "d":

        delete_skill()

    elif user_input == "u":

        print('Update Skill')

    else:
        print('App Is Closed.')

else:
    print(f'Command {user_input} Not Found')