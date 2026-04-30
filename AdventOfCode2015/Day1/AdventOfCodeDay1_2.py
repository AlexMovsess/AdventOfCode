# --- Part Two ---

# Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

# For example:

#     ) causes him to enter the basement at character position 1.
#     ()()) causes him to enter the basement at character position 5.

# What is the position of the character that causes Santa to first enter the basement?

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay1.txt"))
content = f.read()

floor = 0

for i in range(0, len(content), 1):
    if content[i] == ")":
        floor -= 1
        if floor == -1:
            print(i + 1)
            break
    elif content[i] == "(":
        floor += 1
