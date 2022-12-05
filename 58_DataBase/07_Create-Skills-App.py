# -----------------------------------------------
# -- Databases => SQLite => Create Skills App --
# -----------------------------------------------

import sqlite3

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

db = sqlite3.connect('app.db')

cr = db.cursor()


def commit_close():

    db.commit()
    db.close()
    print('Connection to Database is Closed')


user_input = input(input_message).strip().lower()

print(user_input)

# Command List
command_list = ["s", "a", "d", "u", "q"]

user_id = 2


# def show_skill():
#     print('Show Skill')


def add_new_skill():
    sk = input('Add New Skill: ')
    prog = input("Add Progress: ")
    cr.execute(f'insert into skills (name, progress, user_id) values("{sk}", "{prog}", {user_id} )')
    commit_close()


def delete_skill():
    print(f'Delete Skill')
    sk = input('Write Skill Name: ')
    cr.execute(f'delete from skills where name = "{sk}" and user_id = {user_id} ')
    commit_close()


def update_skill():
    print(f'Update Skill')


def quit_app():
    print(f'Quit The App')


if user_input in command_list:

    print(f'Command Found {user_input}')

    if user_input == "s":

        # show_skill()
        pass

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
