#-----------------------------------
#   -- Loop  =>  While Training--
#    -- Simple Password Guess--

# *- While Else     => -If while condition didn't match (False) => else will run, otherwise it will never run.
#-----------------------------------

tries = 4

mainPassword = "Ahmad@123"

inputPassword = input("Write your password: ")

while inputPassword != mainPassword :       ## If this Condition True => else will never run   
                                            ## Else will be used to do the opposite of (While) Condition => ( inputPassword == mainPassword )
    tries -= 1

    print('Wrong Password {} Chance left'.format( 'Last' if tries == 0 else tries))

    inputPassword = input('Write your password: ')

    if tries == 0 :

        print("All Tries are Finished")

        break
        
        print('IT WILL NOT PRINT ANYTHING After (BREAK')


else : print('Correct Password')        ##  It will run if while Condition is False 