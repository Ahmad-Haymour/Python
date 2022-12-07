# ---------------------------------------------------------
# -- Advanced_Lessons => Generate Random Serial Numbers --
# ---------------------------------------------------------

import string           # => All Numbers and Characters
import random

print(string.digits)        # => All Digits
print(string.ascii_letters)  # => small und Capital Letters
print(string.ascii_lowercase)   # => Small Letters
print(string.ascii_uppercase)   # => Capital Letters


def make_serial(count):
    all_chars = string.ascii_letters + string.digits
    print(all_chars)

    chars_count = len(all_chars)
    print(chars_count)

    serial_list = []

    while count > 0:

        random_number = random.randint(0, chars_count - 1)
        random_character = all_chars[random_number]
        serial_list.append(random_character)
        count -= 1

    print("".join(serial_list))


make_serial(20)
