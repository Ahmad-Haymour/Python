#------------------------------#
#  -- File Handling Part 2 --  #
#       *- Read File
#------------------------------#

file = open("/home/user/Desktop/Python/42_File-Handling-Intro/ahmad.txt", "r")

# print(file)

# print(file.name)
# print(file.mode)
# print(file.encoding)

# print(file.read())    =>  Read All File
# print(file.read(5))   =>  Read First 5 Indexes
# print(file.read())    =>  Read the Rest of the File

# print(file.readline())      => Read First Lane
# print(file.readline(5))     => Read First 5 Indexes
# print(file.readline())      => Read the Rest of the Line

# print(file.readlines())         => Return List with all the Lines
# print(file.readlines(50))       => Return Lst with Specific Bytes
# print(type(file.readlines()))   => Type List

for line in file :
    print(line)
    
    if line.startswith('S') :
        break

file.close()            # => You have to Close the File Always