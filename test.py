# Kata – Print the first 10 even numbers
# The first 10 even numbers are 2 through 20, so we check 1 through 20.

LAST_NUMBER = 20

for NUMBER in range(1, LAST_NUMBER +1):
    # a NUMBER IS EVEN WHEN DIVIDING BY 2 LEAVES NOTHING OVER
    if NUMBER % 2 == 0:
        print(NUMBER)