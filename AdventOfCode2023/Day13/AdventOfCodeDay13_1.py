# --- Day 13: Point of Incidence ---

# With your help, the hot springs team locates an appropriate spring which launches you neatly and precisely up to the edge of Lava Island.
# There's just one problem: you don't see any lava.
# You do see a lot of ash and igneous rock; there are even what look like gray mountains scattered around. After a while, you make your way to a nearby cluster of mountains only to discover that the valley between them is completely full of large mirrors. Most of the mirrors seem to be aligned in a consistent way; perhaps you should head in that direction?
# As you move through the valley of mirrors, you find that several of them have fallen from the large metal frames keeping them in place. The mirrors are extremely flat and shiny, and many of the fallen mirrors have lodged into the ash at strange angles. Because the terrain is all one color, it's hard to tell where it's safe to walk or where you're about to run into a mirror.
# You note down the patterns of ash (.) and rocks (#) that you see as you walk (your puzzle input); perhaps by carefully analyzing these patterns, you can figure out where the mirrors are!

# For example:

# #.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#

# To find the reflection in each pattern, you need to find a perfect reflection across either a horizontal line between two rows or across a vertical line between two columns.
# In the first pattern, the reflection is across a vertical line between two columns; arrows on each of the two columns point at the line between the columns:

# 123456789
#     ><
# #.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.
#     ><
# 123456789

# In this pattern, the line of reflection is the vertical line between columns 5 and 6. Because the vertical line is not perfectly in the middle of the pattern, part of the pattern (column 1) has nowhere to reflect onto and can be ignored; every other column has a reflected column within the pattern and must match exactly: column 2 matches column 9, column 3 matches 8, 4 matches 7, and 5 matches 6.
# The second pattern reflects across a horizontal line instead:

# 1 #...##..# 1
# 2 #....#..# 2
# 3 ..##..### 3
# 4v#####.##.v4
# 5^#####.##.^5
# 6 ..##..### 6
# 7 #....#..# 7

# This pattern reflects across the horizontal line between rows 4 and 5. Row 1 would reflect with a hypothetical row 8, but since that's not in the pattern, row 1 doesn't need to match anything. The remaining rows match: row 2 matches row 7, row 3 matches row 6, and row 4 matches row 5.
# To summarize your pattern notes, add up the number of columns to the left of each vertical line of reflection; to that, also add 100 multiplied by the number of rows above each horizontal line of reflection. In the above example, the first pattern's vertical line has 5 columns to its left and the second pattern's horizontal line has 4 rows above it, a total of 405.
# Find the line of reflection in each of the patterns in your notes. What number do you get after summarizing all of your notes?

import os
import re
import numpy as np

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay13.txt"))
puzzleList = f.read().split("\n\n")

sum = 0


def findLineOfReflection(puzzle):

    for i in range(0, len(puzzle), 1):
        for j in range(i + 1, len(puzzle), 1):
            if np.array_equal(
                puzzle[i], puzzle[j]
            ):  # Find any two lines that are equals.
                k = 0
                while (
                    np.array_equal(puzzle[i + k], puzzle[j - k]) and i + k < j - k
                ):  # Pick and compare the two lines inside the previous ones
                    k += 1
                    if (
                        i + k >= len(puzzle) or j - k < 0
                    ):  # Do not go over the limit of the list
                        break
                if (
                    i + k - 1 == j - k
                    and np.array_equal(puzzle[i + k], puzzle[j - k])
                    and (i == 0 or j == len(puzzle) - 1)
                ):  # If the line we picked have crossed and one of the first line was at the extremity of the matrix, we found an axis of symmetry
                    return i + k


for item in puzzleList:
    puzzle = np.array(item.split("\n"))
    ReflectLine = findLineOfReflection(puzzle)
    if ReflectLine == None:
        puzzle = item.split("\n")
        for index, line in enumerate(puzzle):
            puzzle[index] = re.findall(".", puzzle[index])
        puzzle = np.transpose(np.array(puzzle))
        ReflectLine = findLineOfReflection(puzzle)
        sum += ReflectLine
    else:
        sum += 100 * ReflectLine

print("----- Total :", sum, "-----")

# Could probably be simplified, we do not need to go over ALL the lines in the matrix, only compare the most exterior one to the rest, as the axis of symmetry always goes all over to one side.
# Would need new if sentences in the fonction, to be done later.
