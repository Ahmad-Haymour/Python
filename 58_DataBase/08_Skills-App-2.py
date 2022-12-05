# ----------------------------------------------------
# -- Databases => SQLite => Create Skills App 2-3-4 --
# ----------------------------------------------------

import sqlite3

db = sqlite3.connect('app.db')

cr = db.cursor()


def commit_close():
    db.commit()
    db.close()
    print('Database Committed and Closed')


# Input Big Message
input_message = """
What do you want to do ?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option:
"""

user_input = input(input_message).strip().lower()

# Command List
command_list = ["s", "a", "d", "u", "q"]

user_id = 2


def show_skill():
    cr.execute(f'select * from skills where user_id = {user_id}')
    result = cr.fetchall()

    print(f"You have => {len(result)} Skills")

    if len(result) > 0:
        print('Showing Skills with Progress')

    for row in result:
        print(f'Skill is => {row[0]}', end=' ')
        print(f'Progress is => {row[1]}')
    commit_close()


def add_new_skill():
    sk = input('Write Your Skill => ')
    cr.execute(f'select name from skills where name = "{sk}" and user_id = {user_id}')
    result = cr.fetchone()

    if result is None:

        prog = input('Write Your Progress => ')
        cr.execute(f'insert into skills (name, progress, user_id) values("{sk}", "{prog}", {user_id})')
    else:
        print(f"Skill => {result} is Exists, You Cannot Add it.")
        answer = input('Would you Like to Update Its Progress ? y=Yes/No=n')

        if answer == "y":
            progress = input('Write New Progress => ').strip()
            cr.execute(f'update skills set progress = "{progress}" where name = "{sk}" and user_id = {user_id}')
            print('Updated successfully from AddNewSkill Function')

    commit_close()


def delete_skill():
    sk = input('Write Your Skill to Delete => ')
    cr.execute(f'delete from skills where name = "{sk}" and user_id = {user_id}')
    print('Deleted Success')
    commit_close()


def update_skill():

    sk = input('Write Skill to Update').strip()
    prog = input('Add Skill Progress to Update').strip()

    cr.execute(f'update skills set progress = "{prog}" where name = "{sk}" and user_id = {user_id}')
    commit_close()


if user_input in command_list:

    print(f'Command Found {user_input}')

    if user_input == "s":
        show_skill()

    elif user_input == "a":
        add_new_skill()

    elif user_input == "d":
        delete_skill()

    elif user_input == "u":
        update_skill()

    else:
        print('App Is Closed.')

else:
    print(f'Command {user_input} Not Found')

