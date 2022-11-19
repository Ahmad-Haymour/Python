# ----------------
# Escape Sequences Characters
#  0-     \          =>  Ignore next (-2-) "ignore_new_line"
#  1-     \b         =>  Escape Back Space
#  2-     \new_line  =>  Escape new Line
#  3-     \\         =>  Escape Back Slash
#  4-     \'         =>  Escape Single Quote
#  5-     \"         =>  Escape Double Quote
#  6-     \n         =>  Line Feed 
#  7-     \r         =>  Carriage Return
#  8-     \t         =>  Horizontal Tab
#  9-     \xhh       => Character Hex Value
# ----------


# Back Space
print("Hello\bWorld")

# Escape new Line
print("Hello \
I Love \
Python")

# Escape Back Slash
print("HelloWorld \\")

# Escape Single Quote
print('I Love single Quote \'Test\'')

# Escape Double Quote
print("I Love double Quote \"Test\"")

# Line Feed
print("Hello World\nSecond Line")

# Carriage Return
print("123456\rABCD")

# Horizontal Tab
print("Hello\tPython")

# Character Hex Value
print("\x41\x48\x4D\x41\x44")