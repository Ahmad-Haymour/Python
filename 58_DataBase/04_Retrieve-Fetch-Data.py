# -----------------------------------------------------------------
# -- Databases => SQLite => Retrieve (Fetch) Data from Database --
# -----------------------------------------------------------------
# - fetchone     =>  Return a single record or None if no more rows are available
# - fetchall     =>  Fetches all the rows of query result. It returns all the rows
#                    as a List of Tuples, An Empty List is returned if there is no record to fetch.
# - fetchmany(size)    =>
# ---------------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database and Connect
db = sqlite3.connect('app-4.db')

cr = db.cursor()
# Create the Tables and Fields # execute( Query String ) To Manipulate Database Data
# Table name is: => skills
# db.execute("create table skills (name text, progress integer, user_id integer)")
cr.execute("CREATE TABLE if not exists users (user_id integer, name text)")
cr.execute("CREATE TABLE if not exists skills (name text, progress integer, user_id integer)")

# # Inserting Data
# cr.execute('insert into users(user_id, name) values(1, "Ahmad")')
# cr.execute('insert into users(user_id, name) values(2, "Sally")')
# cr.execute('insert into users(user_id, name) values(3, "Rama")')

# Fetch Data
cr.execute('select user_id, name from users')
# Fetch One by One
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())

print('><'*40)
# Fetch Everything in this Schema
# print(cr.fetchall())

print('><'*40)
# Fetch the First Two Elements from Schema Users
print(cr.fetchmany(2))

# Save (Commit) Changes
db.commit()

# Close Database
db.close()
