# ---------------------------------------------------------
#  -- Databases => SQLite => Insert Data Into Database --
# ---------------------------------------------------------
# - cursor      =>  All Operation in SQL Done by Cursor not the Connection Itself
# - commit      =>  Save All Changes
# ------------------------------------

# Import SQLite Module
import sqlite3

# Create Database and Connect
# db = sqlite3.connect('app.db')
db = sqlite3.connect('app-2.db')


# Settings up the Cursor
cr = db.cursor()

# Create Table and Fields
cr.execute("create table if not exists users (user_id integer, name text)")
cr.execute("create table if not exists skills (name text, progress integer, user_id integer)")

# Inserting Data
# cr.execute('insert into users(user_id, name) values(1, "Ahmad")')
# cr.execute('insert into users(user_id, name) values(2, "Sally")')
# cr.execute('insert into users(user_id, name) values(3, "Rama")')

myList = ['Ahmad', 'Lara', 'Salam', 'Sally', 'Rami', 'Huda', 'Elham']

for count, user in enumerate(myList):
    cr.execute(f'INSERT INTO users(user_id, name) VALUES({count}, "{user}")')
# for counter, element in enumerate(myList):
#     print(f'-{counter + 1} => {element}')

# Save (Commit) Changes
db.commit()

# Close Database
db.close()
