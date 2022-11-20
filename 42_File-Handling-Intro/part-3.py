#------------------------------#
#  -- File Handling Part 3 --  #

#       *- Write File       => w
#       *- Append File      => a
#   - Write Will Override the File (Delete All Lines) then (Write The New Lines)
#   - Open Write File Will Delete the Contains first when you Open it.
#   - Open Append File Will Not Delete what our File contains 
#------------------------------#

funFile = open("/home/user/Desktop/Python/42_File-Handling-Intro/fun.txt", "w")

# myFile.write('Hello From Python With Love\n')
# myFile.write('Second Line')
# myFile.write('Third Line')

funFile.write("I Will Success\n"*100)

print('><'*40)

##  writelines()       =>    To Add a List

# myList = ["Ahmad\n", "Shamus\n", "Randy"]
# myFile = open("/home/user/Desktop/Python/42_File-Handling-Intro/ahmad.txt", "w")

# myFile.writelines(myList)

## 
myList = ["Ahmad\n", "Shamus\n", "Randy\n"]
myFile = open("/home/user/Desktop/Python/42_File-Handling-Intro/ahmad.txt", "a")

myFile.write("Hallo There\n")
myFile.write("We are appending new Line\n")
myFile.write("Without Deleting anything")
