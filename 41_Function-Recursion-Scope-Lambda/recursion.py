#------------------------------#
#   -- Function Recursion --   #
#------------------------------#
#       *- We Can Call The Function From Inside of It To Repeat The Same Steps If Condition Matched
#------------------------------#

#   Test Word [ WWWoooorrrldd ]

# x = "WWWoooorrrldd"

# print(x[1:])

def clean_word(word) :

    if len(word) == 1 :
        return word

    print('Function Started => {}'.format(word))
    if word[0] == word[1]:
        print('If Condition Match => {}'.format(word))
        return clean_word(word[1:])

    else :
        print('Else Return => {}'.format(word))
        return word[0] + clean_word(word[1:])
        
print(clean_word('WWWoooorrrldd'))