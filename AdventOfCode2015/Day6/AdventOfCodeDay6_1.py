# --- Day 6: Probably a Fire Hazard ---

# Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.
# Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.
# Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.
# To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

# For example:

#     turn on 0,0 through 999,999 would turn on (or leave on) every light.
#     toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
#     turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

# After following the instructions, how many lights are lit?

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
        lightGrid[x1 : x2 + 1, y1 : y2 + 1] = np.ones([x2 + 1 - x1, y2 + 1 - y1])
    elif action == "turn off":
        lightGrid[x1 : x2 + 1, y1 : y2 + 1] = np.zeros([x2 + 1 - x1, y2 + 1 - y1])
    else:
        with np.nditer(
            lightGrid[x1 : x2 + 1, y1 : y2 + 1], op_flags=["readwrite"]
        ) as it:
            for x in it:
                if x == 1:
                    x[...] = 0
                else:
                    x[...] = 1

print(np.sum(lightGrid))
