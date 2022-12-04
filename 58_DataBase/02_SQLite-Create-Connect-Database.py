# ---------------------------------------------------------
# -- Databases => SQLite => Create Database and Connect --
# ---------------------------------------------------------
# - Connect     =>  Create and Connect Database =>  it take database
# - Execute     =>  Add Tables and Fields in my Database => CREATE TABLE if not exists SchemaName
# - Close       =>  You have to Close Database after finish
# ---------------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database and Connect
db = sqlite3.connect('app.db')

# Create the Tables and Fields # execute( Query String ) To Manipulate Database Data
# Tabla name is: => skills
# db.execute("create table skills (name text, progress integer, user_id integer)")
db.execute("CREATE TABLE if not exists skills (name text, progress integer, user_id integer)")

# Close Database
db.close()
