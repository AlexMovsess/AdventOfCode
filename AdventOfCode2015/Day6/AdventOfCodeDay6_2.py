# --- Part Two ---

# You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.
# The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.
# The phrase turn on actually means that you should increase the brightness of those lights by 1.
# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.
# The phrase toggle actually means that you should increase the brightness of those lights by 2.
# What is the total brightness of all lights combined after following Santa's instructions?

# For example:

#     turn on 0,0 through 0,0 would increase the total brightness by 1.
#     toggle 0,0 through 999,999 would increase the total brightness by 2000000.

import os
import numpy as np
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay6.txt"))
content = f.read()
puzzleList = re.findall(r"(.+) (\d+),(\d+) through (\d+),(\d+)", content)

lightGrid = np.zeros([1000, 1000], dtype=np.int8)

for instruction in puzzleList:
    action, x1, y1, x2, y2 = (
        instruction[0],
        int(instruction[1]),
        int(instruction[2]),
        int(instruction[3]),
        int(instruction[4]),
    )
    if action == "turn on":
        with np.nditer(
            lightGrid[x1 : x2 + 1, y1 : y2 + 1], op_flags=["readwrite"]
        ) as it:
            for x in it:
                x[...] += 1
    elif action == "turn off":
        with np.nditer(
            lightGrid[x1 : x2 + 1, y1 : y2 + 1], op_flags=["readwrite"]
        ) as it:
            for x in it:
                if x > 0:
                    x[...] -= 1
    else:
        with np.nditer(
            lightGrid[x1 : x2 + 1, y1 : y2 + 1], op_flags=["readwrite"]
        ) as it:
            for x in it:
                x[...] += 2

print(np.sum(lightGrid))
