#--------------------------#
#   -- Function Scope --   #
#--------------------------#

# x = 1       #   Global Scope

def one():
    global x        #  => To Make Variable Global
    x = 2         #  => To Override the Global Scope
    print("Variable from function scope {}".format(x))

def two():
    x = 4
    print("Variable from function scope {}".format(x))

print(x)    # => 1
one()
two()
print(x)    # => 2
