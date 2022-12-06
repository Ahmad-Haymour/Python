# --------------------------------------------------------
# -- Databases => SQLite => Very Important Information --
# --------------------------------------------------------

# Import SQLite
import sqlite3

# Create Database and Connect
db = sqlite3.connect('app-8.db')

# Setting UP the Cursor
cr = db.cursor()

# Create Tables
cr.execute("CREATE TABLE if not exists skills (name text, progress integer, user_id integer)")

# User ID
uid = 2

# Choose s, a, d, u
user_input = input('What do you want to do? ').strip().capitalize()

myTuple = (f"SQLite, 60, {uid}")

if user_input == 'A':
    # Inserting Data
    sk = input('Write your Skill: ').strip()
    prog = input('Write new progress => ').strip()
    cr.execute(f'insert into skills(name, progress, user_id) values("{sk}", {prog}, {uid})')
    cr.execute(f'insert into skills values("{sk}", {prog}, {uid})')
    cr.execute('insert into skills values(?, ?, ?)', myTuple)

elif user_input == 'D':
    sk = input('what do you want to Delete? ').strip()
    # Delete Row
    cr.execute(f'delete from skills where name = "{sk}" and user_id = {uid}')

elif user_input == 'U':
    sk = input('what do you want to Update? ').strip()
    prog = input('Write new progress => ').strip()
    # Update
    cr.execute(f'update skills set progress = {prog}  where name = "{sk}" and user_id = {uid}')

elif user_input == 'S':
    # Fetch Data from Database
    cr.execute('select * from skills')
    cr.execute('select * from skills order by user_id asc')     # Lower to Higher
    cr.execute('select * from skills order by user_id desc')    # Higher to Lower
    cr.execute('select * from skills order by name limit 2')    # First Two Elements
    cr.execute('select * from skills order by name limit 3 offset 2')    # Ignore First Two Elements,
                                                                         # and show the first 3 Elements Only.
    cr.execute('select * from skills where user_id > 1')          # Search in Database where id > 1
    cr.execute('select * from skills where user_id in (1, 3)')          # Search in Database where id = 1 and 3
    cr.execute('select * from skills where user_id not in (1, 3)')          # Search in Database where id != 1 and 3

    # Assign Data to Variable
    result = cr.fetchall()

    # Loop
    for skill in result:
        print(f'Skill => {skill[0]}, Progress => {skill[1]}%, User id => {skill[2]}')

print('><'*50)
# Fetch Data from Database
cr.execute('select * from skills')

# Assign Data to Variable
result = cr.fetchall()

# Loop
for skill in result:
    print(f'Skill => {skill[0]}, Progress => {skill[1]}%, User id => {skill[2]}')

# Save (Commit) Changes
db.commit()
# Close Database
db.close()

print('Database Committed and Closed Successfully.')

