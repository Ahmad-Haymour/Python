#------------------------------#
#  -- File Handling Part 1 --  #
#------------------------------#
#     import os       =>      Using Operating System

#   - r         => [ Default Value ] Open File for Read, IF file not exist => ( Error )
#   - a         => Open File for Appending Values, Create File IF not Exist
#   - w         => Open File for Writing, Create File IF not Exist
#   - x         => Create File, IF File Exist => ( Error )
#-------------------------------------------------------------------------------------

# file = open( 'ahmad.txt', 'a')    =>  Append Values or Create File 

## The Absolute Path =>     r   =>  It is a Raw String => IGNORE all the [ \P \F \n \o ] Commands etc...

# file = open(r'/home/user/Desktop/Python/ahmad.txt')

## os => Operating System
#  os.getcwd()  => Get Current Working Directory

# import os               # =>    Operating System

# print(os.getcwd())      # =>    Current Working Directory

# print(os.path.abspath(__file__))        # =>    Opened File

# print(os.path.dirname(os.path.abspath(__file__)))      # => Opened File Directory   ( Parent File )

## Change Current Working Directory

# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# file = open('42_File-Handling-Intro/ahmad.txt','a')    # => Create New File If It's Not Exist

# file = open("ahmad.txt")

# print(os.getcwd())

file = open(r"/home/user/Desktop/Python/42_File-Handling-Intro/ahmad.txt")      # ( Absolute Path )   r ""   => Ignore command [ \ ]