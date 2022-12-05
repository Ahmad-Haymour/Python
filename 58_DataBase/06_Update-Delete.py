# -----------------------------------------------
# -- Databases => SQLite => Update and Delete --
# -----------------------------------------------

import sqlite3

db = sqlite3.connect('app.db')

cr = db.cursor()

# Update Data
# cr.execute('update users set name = \'Sonia\' where user_id = 1')
# cr.execute('update users set name = \'Lara\' where user_id = 2')
# cr.execute('update users set name = \'Ahmad\' where user_id = 3')

# Delete Database Schema
# cr.execute('delete from users')

# Delete single Element from Schema, Depends on Element Match
cr.execute('delete from users where name = \'Badee\' ')
cr.execute('delete from users where user_id = 1')

# Fetch Database
cr.execute('select * from users')

result = cr.fetchall()

print(result)

# Save/Commit Changes
db.commit()

# Close Database
db.close()