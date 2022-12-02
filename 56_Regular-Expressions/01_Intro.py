# -------------------------------------------
#      -- Regular Expression => Part 1 --
# -------------------------------------------
# [1] Sequence of Characters that Define a search Pattern
# [2] Regular expression is not in Python its General Concept
# [3] Used in [Credit card Validation, IP Address Validation, Email Validation]
# [4] Test RegEx "https://pythex.org/"
# [5] Characters Sheet "https://www.debuggex.com/cheatsheet/regex/python"


#    amc        => Search for: 'amc' Word
#    [amc]      => Search for: all "a" & "m" & "c" Characters

#    [S]        => Search for S
#    [^S]       => All Except S

#    [a-z]      => Search for all small letters
#    [A-Z]      => Search for all Capital letters
#    [A-z]      => Search for all Capital and small letters

#    [0-9]      => Search for all Digits
#    [a-z0-9A-Z]    =>  All Digits, Small and Capital Letters

#   [^a-z]      =>  All except a-z
#   [^A-Z]      =>  All Except A-Z
#   [^0-9]      =>  All Except Digits

#   \d    =>   One Digit [0-9]
#   \w    =>   One Wod Character
#   \s    =>   One Whitespace

#   \D    =>    One Non-Digit
#   \W    =>    One Non-Word Character
#   \S    =>    One Non-Whitespace

# ------------------------------------------------
#  -- Regular Expression => Quantifiers Part 2 --
# ------------------------------------------------
# [6] Regular Expressions Generator "https://regex101.com"

#   * 0 or more
#   + 1 or more
#   ? 0 or 1
#   {2} Exactly 2
#   {2,5} Between 2 and 5
#   {2,} 2 or more
#   {,5} Up to 5

# ----------------------------------------------------
# -- Regular Expression => Character Classes Part 3 --
# ----------------------------------------------------

#   [ab-d]  One Character of: a, b, c, d
#   [^ab-d]  One Character except: a, b, c, d
#   [0-9]
#   [^0-9]
#   [A-Z]
#   [^A-Z]
#   [a-z]
#   [^a-z]
# -----------

#   Example

#   \s[A-Z]{2}\s[0-9]{3}\s\w{,6}

# =>  " SH 223 SAlamO"  


# ------------------------------------------------
# -- Regular Expression => Assertions Part 4 --
# ------------------------------------------------
#   ^       =>  Start of string
#   $       =>  End of string
#   ?       =>  Check the string if this character either way exist or not exist
#   +       =>  Or More like the Previous code
#   \.      =>  
# ------------------------------------------------

#   \d{3}\s\d{4}\s\d{3}
#   => 3 Numbers _ Space _ 4 Numbers _ Space _ 3 Numbers

#   ^\d{3}\s\d{4}-?\s?\d{3}$
#   => Start _ 3 Numbers _ Space _ 4 Numbers _ - or None _ Space or None _ 3 Numbers _ End

## Email Example

# ^[A-z0-9\.]+@[A-z0-9]+\.[A-z]+
# ^[A-z0-9\.]+@[A-z0-9]+\.(com)
# ^[A-z0-9\.]+@[A-z0-9]+\.(com|net|org)



# -----------------------------------------------------------
# -- Regular Expression => Logical Or and Escaping Part 5 --
# -----------------------------------------------------------
#   |       =>  Or
#   \       =>  Escape
#   ()      =>  Separate Groups
# ------------------------------------------------

#   Example 1       =>      (\d-|\d\)|\d>) (\w+)

#   1-HTML
#   2)CSS
#   3>Python

#   Example 2       =>      (\d{3}) (\d{4}) (\d{3}|(\d{3}))

#   Example 3       =>      ^(https?)://(www\.)?(\w+)\.(com|net|de|org)$
#   "https://www.google.com"
#   "http://google.de"