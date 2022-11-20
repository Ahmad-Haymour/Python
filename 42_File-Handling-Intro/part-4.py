#-----------------------------------------#
#  -- File Handling => Important Info --  #
#-----------------------------------------#

# file = open("/home/user/Desktop/Python/42_File-Handling-Intro/fun.txt", "a")  # append
# file.truncate(13)         =>  Cut my TXT File

# file = open("/home/user/Desktop/Python/42_File-Handling-Intro/fun.txt", "a")  # append
# print(file.tell())      #  =>   Where my File End ( Mouse Cursor |  )

file = open("/home/user/Desktop/Python/42_File-Handling-Intro/fun.txt", "r")    # read
file.seek(2)              #  =>   Read From Index 6 to the End
                          #  =>   Move Text Cursor to Index 6
print(file.read())

import os

os.remove("/home/user/Desktop/Python/ahmad.txt")        #   =>  Delete File 