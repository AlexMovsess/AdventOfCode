# --- Day 18: Lavaduct Lagoon ---

# Thanks to your efforts, the machine parts factory is one of the first factories up and running since the lavafall came back. However, to catch up with the large backlog of parts requests, the factory will also need a large supply of lava for a while; the Elves have already started creating a large lagoon nearby for this purpose.
# However, they aren't sure the lagoon will be big enough; they've asked you to take a look at the dig plan (your puzzle input). For example:

# R 6 (#70c710)
# D 5 (#0dc571)
# L 2 (#5713f0)
# D 2 (#d2c081)
# R 2 (#59c680)
# D 2 (#411b91)
# L 5 (#8ceee2)
# U 2 (#caa173)
# L 1 (#1b58a2)
# U 2 (#caa171)
# R 2 (#7807d2)
# U 3 (#a77fa3)
# L 2 (#015232)
# U 2 (#7a21e3)

# The digger starts in a 1 meter cube hole in the ground. They then dig the specified number of meters up (U), down (D), left (L), or right (R), clearing full 1 meter cubes as they go. The directions are given as seen from above, so if "up" were north, then "right" would be east, and so on. Each trench is also listed with the color that the edge of the trench should be painted as an RGB hexadecimal color code.
# When viewed from above, the above example dig plan would result in the following loop of trench (#) having been dug out from otherwise ground-level terrain (.):

# #######
# #.....#
# ###...#
# ..#...#
# ..#...#
# ###.###
# #...#..
# ##..###
# .#....#
# .######

# At this point, the trench could contain 38 cubic meters of lava. However, this is just the edge of the lagoon; the next step is to dig out the interior so that it is one meter deep as well:

# #######
# #######
# #######
# ..#####
# ..#####
# #######
# #####..
# #######
# .######
# .######

# Now, the lagoon can contain a much more respectable 62 cubic meters of lava. While the interior is dug out, the edges are also painted according to the color codes in the dig plan.
# The Elves are concerned the lagoon won't be large enough; if they follow their dig plan, how many cubic meters of lava could it hold?

import os
import re
import numpy as np
import sys

sys.setrecursionlimit(33837)

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay18.txt"))
puzzleList = re.findall(r"(\w) (\d+) ", f.read())
puzzleList = list(map(lambda x: (x[0], int(x[1])), puzzleList))

yLength = 0
xLength = 0

for item in puzzleList:
    if item[0] == "L":
        xLength += item[1]
    elif item[0] == "D":
        yLength += item[1]
# calculate the size of the map of the trench

print(xLength, yLength)
digArray = np.zeros([xLength * 2, yLength * 2])
pos = (xLength, yLength)
# Multiply by two and start at center point to be sure to fit it no matter where it goes (up, down, left or right)

digArray[pos] = 1
for item in puzzleList:  # Trace the border trench on the map
    if item[0] == "L":
        digArray[pos[0], pos[1] - item[1] : pos[1]] = 1
        pos = (pos[0], pos[1] - item[1])
    elif item[0] == "R":
        digArray[pos[0], pos[1] : pos[1] + item[1] + 1] = 1
        pos = (pos[0], pos[1] + item[1])
    elif item[0] == "U":
        digArray[pos[0] - item[1] : pos[0], pos[1]] = 1
        pos = (pos[0] - item[1], pos[1])
    elif item[0] == "D":
        digArray[pos[0] : pos[0] + item[1] + 1, pos[1]] = 1
        pos = (pos[0] + item[1], pos[1])


def fillInArray(
    x, y
):  # Fill in. Huge recursion. If the point is a zero, fill it and examine neighbour. If neighbours are zeros, call function on them.
    digArray[x, y] = 1
    for i in [-1, 1]:
        if digArray[x + i, y] == 0:
            fillInArray(x + i, y)
    for j in [-1, 1]:
        if digArray[x, y + j] == 0:
            fillInArray(x, y + j)


fillInArray(
    xLength - 1, yLength - 1
)  # Need to start on the in side of the border trench.

print("----- Total :", np.count_nonzero(digArray), "-----")
