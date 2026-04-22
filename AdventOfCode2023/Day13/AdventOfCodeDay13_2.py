# --- Part Two ---

# You resume walking through the valley of mirrors and - SMACK! - run directly into one. Hopefully nobody was watching, because that must have been pretty embarrassing.
# Upon closer inspection, you discover that every mirror has exactly one smudge: exactly one . or # should be the opposite type.
# In each pattern, you'll need to locate and fix the smudge that causes a different reflection line to be valid. (The old reflection line won't necessarily continue being valid after the smudge is fixed.)
# Here's the above example again:

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

# The first pattern's smudge is in the top-left corner. If the top-left # were instead ., it would have a different, horizontal line of reflection:

# 1 ..##..##. 1
# 2 ..#.##.#. 2
# 3v##......#v3
# 4^##......#^4
# 5 ..#.##.#. 5
# 6 ..##..##. 6
# 7 #.#.##.#. 7

# With the smudge in the top-left corner repaired, a new horizontal line of reflection between rows 3 and 4 now exists. Row 7 has no corresponding reflected row and can be ignored, but every other row matches exactly: row 1 matches row 6, row 2 matches row 5, and row 3 matches row 4.
# In the second pattern, the smudge can be fixed by changing the fifth symbol on row 2 from . to #:

# 1v#...##..#v1
# 2^#...##..#^2
# 3 ..##..### 3
# 4 #####.##. 4
# 5 #####.##. 5
# 6 ..##..### 6
# 7 #....#..# 7

# Now, the pattern has a different horizontal line of reflection between rows 1 and 2.
# Summarize your notes as before, but instead use the new different reflection lines. In this example, the first pattern's new horizontal line has 3 rows above it and the second pattern's new horizontal line has 1 row above it, summarizing to the value 400.
# In each pattern, fix the smudge and find the different line of reflection. What number do you get after summarizing the new reflection line in each pattern in your notes?

import os
import re
import numpy as np

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay13.txt"))
puzzleList = f.read().split("\n\n")

sum = 0


def findLineOfReflectionwithModifiedChar(puzzle, rowX):
    for i in range(0, len(puzzle), 1):
        for j in range(i + 1, len(puzzle), 1):
            if np.array_equal(puzzle[i], puzzle[j]):
                k = 0
                while np.array_equal(puzzle[i + k], puzzle[j - k]) and i + k < j - k:
                    k += 1
                    if i + k >= len(puzzle) or j - k < 0:
                        break
                if (
                    i + k - 1 == j - k
                    and np.array_equal(puzzle[i + k], puzzle[j - k])
                    and (i == 0 or j == len(puzzle) - 1)
                    and i <= rowX <= j
                ):  # Add a condition that the line of the modified char must be between or equal to the very first line of symmetry found
                    return i + k


def findSmudge(puzzle):
    for i in range(0, len(puzzle), 1):
        for j in range(0, len(puzzle[i]), 1):
            newPuzzle = puzzle
            if puzzle[i][j] == "#":
                newPuzzle[i][j] = "."
            else:
                newPuzzle[i][j] = "#"
            reflectLine = findLineOfReflectionwithModifiedChar(newPuzzle, i)
            if reflectLine != None:
                return (0, reflectLine)
            else:
                if puzzle[i][j] == "#":
                    newPuzzle[i][j] = "."
                else:
                    newPuzzle[i][j] = "#"
    if reflectLine == None:
        puzzle = np.transpose(puzzle)
        for i in range(0, len(puzzle), 1):
            for j in range(0, len(puzzle[i]), 1):
                newPuzzle = puzzle
                if puzzle[i][j] == "#":
                    newPuzzle[i][j] = "."
                else:
                    newPuzzle[i][j] = "#"
                reflectLine = findLineOfReflectionwithModifiedChar(newPuzzle, i)
                if reflectLine != None:
                    return (1, reflectLine)
                else:
                    if puzzle[i][j] == "#":
                        newPuzzle[i][j] = "."
                    else:
                        newPuzzle[i][j] = "#"


count = 1
for item in puzzleList:
    puzzle = item.split("\n")
    for index, line in enumerate(puzzle):
        puzzle[index] = re.findall(".", puzzle[index])
    index, reflectLine = findSmudge(np.array(puzzle))
    if index == 0:
        sum += 100 * reflectLine

    else:
        sum += reflectLine
    print(sum)
    count += 1

print("----- Total :", sum, "-----")
