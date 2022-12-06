# -------------------------------------------------------
# -- Advanced_Lessons => Timing Your Code With Timeit --
# -------------------------------------------------------
# - timeit - Get Execution Time of Code By Running 1M Time and Give you Minimal Time
# -        - It used for Performance by Testng All Functionality
# - timeit(stmt, setup, timer, number)
# - timeit(pass, pass, default, 1.000.000) Default Values
# --------------------------------------------------------
# - stmt: Code you want to Measure the Execution Time
# - setup: Setup done before the Code Execution (Import Module or Anything)
# - timer: The Timer Value
# - number: How many Execution Tht will run
# --------------------------------------------------------

import timeit
# import random
# we Import Random in Function setup

print(dir(timeit))

print(timeit.timeit("'Ahmad' * 1000"))  # How Long this Function will take(Time)

# name = 'Ahmad'
# print(name * 1000)

print(timeit.timeit("name = 'Ahmad'; name * 1000"))

print(random.randint(0, 50))

print(timeit.timeit(stmt="random.randint(0, 100)", setup="import random"))

print(timeit.timeit(stmt="random.randint(0, 100)", setup="import random", repeat=4))
# It will repeat this Module Function 4 Times and will show you the less result