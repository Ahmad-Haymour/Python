#-----------------------------------
# -- Practical Membership Control --
#-----------------------------------

# List Contains Admins
admins = ['Ahmad', 'Salam', 'Sally', 'Suzan', 'Sam']

# Login
name = input("Please type your name ").strip().capitalize()

if name in admins :
    print("You are admin")
    print("Hello {} welcome back".format(name))

    option = input("Delete or Update your name? ").strip().capitalize()
    print(option)

    if option == "Update" or option == "U" :
        theNewName = input('Your new name please ').strip().capitalize()
        admins[ admins.index("Sally") ] = theNewName
        print('Name Updated')
        print(admins)

    elif option == "Delete" or option == 'D':

        admins.remove(name)
        print('Name Deleted')
        print(admins)

    else : print('Wrong Option!')


else : 
    status = input('Wanna be an Admin? yes(y), no(n) ').strip().lower()

    if status == "Yes" or status == 'y' :
        print("You have been added.")
        admins.append(name)
        print(admins)

    else : print('You are not admin')