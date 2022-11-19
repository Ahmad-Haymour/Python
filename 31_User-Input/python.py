# ------------------------------
#       -- User Input --
# ------------------------------


firstname = input('What\'s Your First Name?')
lastname = input('What\'s Your Last Name?')
nickname = input('What\'s Your Nick Name?').strip().capitalize()

firstname = firstname.strip().upper()

print("Hello {1:s}, {2:.3s}, Happy To See You {0:s}".format(nickname, firstname, lastname.strip().lower()))

# print(f"Hello {firstname:.4s}, {nickname:s}, Happy To See You {lastname.strip().lower():s}")

### You need help in this => print(f"string {myVar}")