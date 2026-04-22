# --- Day 14: Parabolic Reflector Dish ---

# You reach the place where all of the mirrors were pointing: a massive parabolic reflector dish attached to the side of another large mountain.
# The dish is made up of many small mirrors, but while the mirrors themselves are roughly in the shape of a parabolic reflector dish, each individual mirror seems to be pointing in slightly the wrong direction. If the dish is meant to focus light, all it's doing right now is sending it in a vague direction.
# This system must be what provides the energy for the lava! If you focus the reflector dish, maybe you can go where it's pointing and use the light to fix the lava production.
# Upon closer inspection, the individual mirrors each appear to be connected via an elaborate system of ropes and pulleys to a large metal platform below the dish. The platform is covered in large rocks of various shapes. Depending on their position, the weight of the rocks deforms the platform, and the shape of the platform controls which ropes move and ultimately the focus of the dish.
# In short: if you move the rocks, you can focus the dish. The platform even has a control panel on the side that lets you tilt it in one of four directions! The rounded rocks (O) will roll when the platform is tilted, while the cube-shaped rocks (#) will stay in place. You note the positions of all of the empty spaces (.) and rocks (your puzzle input). For example:

# O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....

# Start by tilting the lever so all of the rocks will slide north as far as they will go:

# OOOO.#.O..
# OO..#....#
# OO..O##..O
# O..#.OO...
# ........#.
# ..#....#.#
# ..O..#.O.O
# ..O.......
# #....###..
# #....#....

# You notice that the support beams along the north side of the platform are damaged; to ensure the platform doesn't collapse, you should calculate the total load on the north support beams.
# The amount of load caused by a single rounded rock (O) is equal to the number of rows from the rock to the south edge of the platform, including the row the rock is on. (Cube-shaped rocks (#) don't contribute to load.) So, the amount of load caused by each rock in each row is as follows:

# OOOO.#.O.. 10
# OO..#....#  9
# OO..O##..O  8
# O..#.OO...  7
# ........#.  6
# ..#....#.#  5
# ..O..#.O.O  4
# ..O.......  3
# #....###..  2
# #....#....  1

# The total load is the sum of the load caused by all of the rounded rocks. In this example, the total load is 136.
# Tilt the platform so that the rounded rocks all roll north. Afterward, what is the total load on the north support beams?

import os
import re
import numpy as np

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay14.txt"))
puzzleList = f.read().split("\n")

for index, line in enumerate(puzzleList):
    puzzleList[index] = re.findall(".", puzzleList[index])

sum = 0
for line in np.rot90(puzzleList, 1):
    previousSharp = -1
    countZeros = 0
    i = 0
    while i <= len(line):
        if i == len(line):  # End of line needs to be modified too
            line[previousSharp + 1 : i] = [
                "O" for k in range(previousSharp, previousSharp + countZeros, 1)
            ] + ["." for k in range(previousSharp + countZeros + 1, i, 1)]
        elif line[i] == "O":
            countZeros += 1
        elif line[i] == "#":
            if previousSharp == -1:  # Start of line need to be modified too
                line[0:i] = ["O" for k in range(0, countZeros, 1)] + [
                    "." for k in range(countZeros, i, 1)
                ]
            else:
                line[previousSharp + 1 : i] = [
                    "O" for k in range(previousSharp, previousSharp + countZeros, 1)
                ] + ["." for k in range(previousSharp + countZeros + 1, i, 1)]
            previousSharp = i
            countZeros = 0
        i += 1
    for i in range(0, len(line), 1):
        if line[i] == "O":
            sum += len(line) - i

print("----- Total :", sum, "-----")

# Rotate the input so that every block rolls left. Then go over each lines doing the rolling blocks transformation. Go over the line another time adding up the relative load of each block.
