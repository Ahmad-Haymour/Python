#-----------------------------------#
#  -- Built In Functions Part 4 --  #
#           MAP
#-----------------------------------#
#   [1] Map take a Function & Iterator
#   [2] Map called Map because it Map the Function on every Element
#   [3] The Function can be Pre-Defined function or Lambda Function

##  Use Map with Predefined Function

#   Map( Function, List [ Iteration] )

def formatText(text):

    return "- {} -".format(text.strip().capitalize())

myTexts = [ "AhMAD", "SaLLY", "SaM"]

myFormatedData = map(formatText, myTexts) 

print(myFormatedData)

# for name in myFormatedData :
# for name in map(formatText, myTexts) :
# for name in list(map(formatText, myTexts)) :

for name in list(map( lambda text : "- {} -".format(text.strip().capitalize()) , myTexts)) :

    print(name)