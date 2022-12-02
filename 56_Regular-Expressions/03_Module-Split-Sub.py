# -------------------------------------------------------------
# -- Regular Expressions => Re Module Split and Sub Part 6 --
# -------------------------------------------------------------
#    split( Pattern, String, MaxSplit )              =>  Return a List of Elements Splitted on Each Match
#    sub( Pattern, Replace, String, ReplaceCount )   =>  Replace Matches with what you want

import re

string_one = "I Love Python"

search_one = re.split(r'\s', string_one)

print(search_one)

print('><'*40)

string_two = 'How-To_Write_A_Very-Good-Article'

search_two = re.split(r'-|_', string_two, 3)

print(search_two)

# Get Words From URL

for counter, word in enumerate(search_two, 1):

    if len(word) == 1:

        continue

    print('Word Number: {} => {}'.format(counter, word.lower()))

print('><'*40)


## sub(Pattern, Replace, String, Replace Count)

my_string = 'I Love Python and Django'

print(re.sub(r'\s','<(^_^)>', my_string, 2))
  