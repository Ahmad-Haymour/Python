# -----------------------------------------------------
# -- Databases => SQLite => Training  on Everything --
# -----------------------------------------------------

import sqlite3


def get_all_data():

    try:
        # Connect to Database
        db = sqlite3.connect('app-4.db')

        # Setting up the Cursor to Manipulate Database
        cr = db.cursor()

        # Fetch Data from Database
        cr.execute('select * from users')

        # Assign Data to Variable
        result = cr.fetchall()  # List
        # result = cr.fetchone() # Tuple

        print(result)

        # Print Number of Rows
        print(f'Database has => {len(result)} Rows')

        # Loop on Result
        for row in result:

            print(f'User ID => {row[0]}', end=' - ')
            print(f'Username => {row[1]}')
            # print(f'ID -> {row[0]} => Username is: {row[1]}')

    except sqlite3.Error as er:

        print(f'Error Reading Data {er}')

    finally:

        if db:
            # Close Database Connection
            cr.close()

            print('Database Closed')


get_all_data()
