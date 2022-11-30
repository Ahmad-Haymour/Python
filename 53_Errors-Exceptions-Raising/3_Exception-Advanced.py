# ------------------------------------------------ #
#           -- Exceptions Handling --  
#      -- Try | Except | Else | Finally -- 
#            -- Advanced Example --  
# ------------------------------------------------ #

the_file = None
the_tries = 5

while the_tries > 0:

    try:   # Try to open File

        print('Write the file name with absolute Path to Open')

        print('You have {} tries left'.format(the_tries))

        print('Path Example => \'/bla/bla\'')  

        file_name_and_path = input('File Name => ').strip()

        print('><'*40)

        the_file = open(file_name_and_path, 'r')

        print('After Open File')
        print('><'*40)

        print(the_file.read())

        break

    except FileNotFoundError:

        print('File Not Found! Please be Sure the name is valid')

        the_tries -= 1

    except:
        
        print('Error happen')

    finally:

        if the_file is not None:

            the_file.close()

            print('File Closed')

else:

    print('All tries are done.')
