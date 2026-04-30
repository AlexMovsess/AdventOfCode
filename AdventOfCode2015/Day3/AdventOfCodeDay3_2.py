# --- Part Two ---

# The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.
# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.
# This year, how many houses receive at least one present?

# For example:

#     ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
#     ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
#     ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

import os
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay3.txt"))
content = f.read()

coordinatesSanta = (0, 0)
coordinatesRobot = (0, 0)
visitedDict = {}
visitedDict[coordinatesSanta] = 1

for index, character in enumerate(re.findall(r"(.)", content)):
    if index % 2 == 0:
        if character == ">":
            coordinatesSanta = (coordinatesSanta[0], coordinatesSanta[1] + 1)
        if character == "<":
            coordinatesSanta = (coordinatesSanta[0], coordinatesSanta[1] - 1)
        if character == "^":
            coordinatesSanta = (coordinatesSanta[0] - 1, coordinatesSanta[1])
        if character == "v":
            coordinatesSanta = (coordinatesSanta[0] + 1, coordinatesSanta[1])
        try:
            visitedDict[coordinatesSanta] += 1
        except KeyError:
            visitedDict[coordinatesSanta] = 1
    else:
        if character == ">":
            coordinatesRobot = (coordinatesRobot[0], coordinatesRobot[1] + 1)
        if character == "<":
            coordinatesRobot = (coordinatesRobot[0], coordinatesRobot[1] - 1)
        if character == "^":
            coordinatesRobot = (coordinatesRobot[0] - 1, coordinatesRobot[1])
        if character == "v":
            coordinatesRobot = (coordinatesRobot[0] + 1, coordinatesRobot[1])
        try:
            visitedDict[coordinatesRobot] += 1
        except KeyError:
            visitedDict[coordinatesRobot] = 1

print(len(visitedDict))
