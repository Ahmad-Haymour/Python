# -------------------------------------------------------------
# -- Regular Expressions => Group Training and Flags Part 7 --
# -------------------------------------------------------------
#   I   => Ignore Case  =>   Search for Capital and Small Letter ( Ignor Upper & Lower Case )
#   VERBOSE  =>   Ignore All Comments in my Regex
#   DOTALL  =>   (.) Match Everything also New Lines
#   M   => MULTILINE  =>   Read Multiple Lines
# -------------------------------------------------------------


import re

my_web = 'https://www.google.com:8000/category.php?article=105?name=how-to-do'

search = re.search(r'(https?)://(www)?\.?(\w+)\.(\w+):(\d+)?/?(.+)', my_web)

print(search)
print(search.group())
print(search.group(1))      # => Print First group
print(search.groups())

for group in search.groups():       # => Loop on Each Group

    print(group)

print('><'*50)

print(f'Protocol: {search.group(1)}')
print(f'Sub Domain: {search.group(2)}')
print(f'Domain Name: {search.group(3)}')
print(f'Top Level domain: {search.group(4)}')
print(f'Port: {search.group(5)}')
print(f'Query String: {search.group(6)}')

print('><'*50)

# Flags:

search_flag_example1 = re.search(r'(https?)://(www)?\.?(\w+)\.(\w+):(\d+)?/?(.+)', my_web, re.M)
search_flag_example2 = re.search(r'(https?)://(www)?\.?(\w+)\.(\w+):(\d+)?/?(.+)', my_web, re.I)
search_flag_example3 = re.search(r'(https?)://(www)?\.?(\w+)\.(\w+):(\d+)?/?(.+)', my_web, re.DOTALL)
search_flag_example4 = re.search(r'(https?)://(www)?\.?(\w+)\.(\w+):(\d+)?/?(.+)', my_web, re.VERBOSE)

